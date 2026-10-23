# Agreement between LLMs and human coders on psychological and clinical text: meta-analysis
# (protocol v1.0, sections 13 and 15-17; deviations.md D7, D8).
#
# Reads forms/estimates.csv, forms/tasks.csv, forms/studies.csv and forms/human_reliability.csv
# (extraction/finalize.py) and writes the results to analysis/results/.
# Primary outcome: chance-corrected agreement (kappa family) on its original scale. Model: CHE (random effects for
# studies and for estimates within studies, assumed within-study correlation 0.6) with CR2 cluster-robust inference
# (section 15b). Secondary outcome: ICC and correlations on Fisher's z.
# Standard errors of kappa: from the reported CI; otherwise from n and the chance agreement p_e (Cohen, 1960), with
# p_e from the observed agreement of the same configuration when reported, else the median p_e (flagged, section 13).
#
# Run from the repository root: Rscript papers/llm-coder-agreement-meta/analysis/analysis.R

suppressPackageStartupMessages({
  library(metafor); library(clubSandwich); library(dplyr); library(readr); library(tidyr); library(jsonlite)
})

root <- "papers/llm-coder-agreement-meta"
res_dir <- file.path(root, "analysis", "results")
dir.create(res_dir, showWarnings = FALSE, recursive = TRUE)
RHO <- 0.6; MIN_K <- 3; MIN_K_MOD <- 10; SE_FLOOR <- 0.005
KAPPA <- c("cohen_kappa", "fleiss_kappa", "weighted_kappa_linear", "weighted_kappa_quadratic", "weighted_kappa",
           "krippendorff_alpha", "gwet_ac1", "pabak")
CORR <- c("icc", "pearson", "spearman", "kendall", "ccc")
LK <- c(-Inf, 0, 0.20, 0.40, 0.60, 0.80, Inf)   # Landis and Koch (1977) bands, descriptive only
band <- function(x) as.integer(cut(x, LK, labels = FALSE))

rd <- function(f) read_csv(file.path(root, "forms", f), col_types = cols(.default = "c"), na = character())
num_first <- function(x) {
  x <- gsub("(?<=\\d),(?=\\d{3})", "", x, perl = TRUE)
  ok <- grepl("[0-9]", x)
  out <- rep(NA_real_, length(x))
  out[ok] <- suppressWarnings(as.numeric(sub("^[^0-9]*([0-9]+(\\.[0-9]+)?).*$", "\\1", x[ok])))
  out
}
n_cat <- function(x) {
  x <- tolower(x)
  out <- ifelse(grepl("binary", x), 2, NA_real_)
  m <- regmatches(x, regexec("([0-9]+)\\s*x\\s*([0-9]+)", x))
  out <- ifelse(is.na(out), vapply(m, function(z) if (length(z) == 3) as.numeric(z[3]) else NA_real_, 1), out)
  r <- regmatches(x, regexec("([0-9]+)\\s*-\\s*([0-9]+)", x))
  rng <- vapply(r, function(z) if (length(z) == 3) as.numeric(z[3]) - as.numeric(z[2]) + 1 else NA_real_, 1)
  out <- ifelse(is.na(out), rng, out)
  out <- ifelse(is.na(out), num_first(x), out)
  ifelse(!is.na(out) & out >= 2 & out <= 101, out, NA_real_)
}

studies <- rd("studies.csv"); tasks <- rd("tasks.csv"); hr_raw <- rd("human_reliability.csv")
excl_studies <- studies$study_id[studies$excluded_r1 != ""]
tasks <- tasks |> mutate(n_task = num_first(n_units), n_categories_n = n_cat(n_categories),
                         english = case_when(language == "en" ~ "English", language %in% c("", "NR") ~ NA_character_,
                                             TRUE ~ "other"))
est_all <- rd("estimates.csv") |>
  filter(include == "yes", !study_id %in% excl_studies) |>
  mutate(v = as.numeric(value), lo = as.numeric(ci_low), hi = as.numeric(ci_high), n_e = num_first(n_units)) |>
  left_join(tasks |> select(study_id, task_id, n_task, n_categories_n, construct_type, english, text_source,
                            human_expertise, reference_type, dataset_public, excluded_r1_task = excluded_r1),
            by = c("study_id", "task_id")) |>
  filter(is.na(excluded_r1_task) | excluded_r1_task == "") |>
  left_join(studies |> select(study_id, pub_status, all_configs_reported, rob_1, rob_2, rob_3, rob_4, rob_5, own_study,
                              year), by = "study_id") |>
  mutate(n = coalesce(n_e, n_task),
         rel = as.Date(ifelse(release_date == "", NA, release_date)),
         years = as.numeric(rel - as.Date("2020-06-01")) / 365.25,
         prompt = case_when(grepl("fine-tun|lora|sft|grpo|qlora", tolower(prompting)) ~ "fine-tuned",
                            grepl("few-shot", tolower(prompting)) ~ "few-shot", TRUE ~ "zero-shot"),
         ref2 = case_when(reference %in% c("single-coder", "each-of-several") ~ "single coder",
                          reference %in% c("consensus-or-adjudicated", "majority-vote", "mean-of-raters") ~ "aggregate of coders",
                          TRUE ~ NA_character_),
         peer = pub_status %in% c("journal", "conference"))

# ------------------------------------------------------------------------------------------------- kappa SEs
pairs_po <- est_all |> filter(statistic %in% c("accuracy", "percent_agreement"), pool == "yes", !is.na(v)) |>
  group_by(study_id, task_id, model_name, configuration) |> summarise(po = mean(v), .groups = "drop")
kap <- est_all |> filter(pool == "yes", statistic %in% KAPPA, !is.na(v)) |>
  left_join(pairs_po, by = c("study_id", "task_id", "model_name", "configuration")) |>
  mutate(pe_obs = ifelse(statistic %in% c("cohen_kappa", "fleiss_kappa") & !is.na(po) & v < 1, (po - v) / (1 - v), NA),
         pe_obs = ifelse(!is.na(pe_obs) & pe_obs >= 0 & pe_obs < 1, pe_obs, NA))
PE_MED <- median(kap$pe_obs, na.rm = TRUE)
se_kappa <- function(k, n, pe) {
  po <- pmin(pmax(k * (1 - pe) + pe, 0.001), 0.999)
  sqrt(po * (1 - po) / (n * (1 - pe)^2))
}
kap <- kap |>
  mutate(se_ci = ifelse(!is.na(lo) & !is.na(hi) & hi > lo, (hi - lo) / (2 * qnorm(0.975)), NA),
         pe = coalesce(pe_obs, PE_MED),
         se_n = ifelse(!is.na(n) & n >= 5, se_kappa(v, n, pe), NA),
         se = pmax(coalesce(se_ci, se_n), SE_FLOOR),
         se_source = case_when(!is.na(se_ci) ~ "CI", !is.na(pe_obs) & !is.na(se_n) ~ "n and observed p_e",
                               !is.na(se_n) ~ "n and imputed p_e", TRUE ~ "none"),
         yi = v, vi = se^2) |>
  filter(se_source != "none") |>
  mutate(es_id = row_number())
write_csv(kap |> count(se_source), file.path(res_dir, "kappa_se_sources.csv"))

# ------------------------------------------------------------------------------------------------- models
fit_che <- function(dat, mods = NULL, rho = RHO) {
  dat <- dat |> arrange(study_id) |> mutate(es_id = row_number())
  V <- vcalc(vi, cluster = study_id, obs = es_id, rho = rho, data = dat)
  m <- if (is.null(mods)) rma.mv(yi, V, random = ~ 1 | study_id / es_id, data = dat, sparse = TRUE, test = "t")
       else rma.mv(yi, V, mods = mods, random = ~ 1 | study_id / es_id, data = dat, sparse = TRUE, test = "t")
  list(m = m, dat = dat, rob = coef_test(m, vcov = "CR2", cluster = dat$study_id),
       ci = conf_int(m, vcov = "CR2", cluster = dat$study_id))
}
# I-squared per level (Cheung, 2014): sigma2 of the level over the total of the sigma2s and the typical sampling variance
i2 <- function(f) {
  w <- 1 / f$dat$vi; k <- length(w)
  v_typ <- (k - 1) * sum(w) / (sum(w)^2 - sum(w^2))
  100 * f$m$sigma2 / (sum(f$m$sigma2) + v_typ)
}
pooled <- function(dat, label, rho = RHO, back = identity) {
  k_s <- n_distinct(dat$study_id)
  if (k_s < MIN_K) return(tibble(analysis = label, k_studies = k_s, k_estimates = nrow(dat)))
  f <- fit_che(dat, rho = rho)
  est <- f$ci$beta[1]; se <- f$ci$SE[1]
  tau <- sqrt(sum(f$m$sigma2)); dfp <- max(k_s - 2, 1)
  tibble(analysis = label, k_studies = k_s, k_estimates = nrow(dat),
         est = back(est), ci_lb = back(f$ci$CI_L[1]), ci_ub = back(f$ci$CI_U[1]), df_cr2 = f$ci$df[1],
         pi_lb = back(est - qt(0.975, dfp) * sqrt(se^2 + tau^2)),
         pi_ub = pmin(back(est + qt(0.975, dfp) * sqrt(se^2 + tau^2)), 1),   # agreement cannot exceed 1
         tau2_study = f$m$sigma2[1], tau2_estimate = f$m$sigma2[2],
         i2_study = i2(f)[1], i2_estimate = i2(f)[2],
         reliable = f$ci$df[1] >= 4)
}
moderator <- function(dat, var, label) {
  d <- dat |> filter(!is.na(.data[[var]]))
  if (is.factor(d[[var]])) {   # levels informed by fewer than three studies are dropped
    keep <- names(which(sapply(split(d$study_id, d[[var]]), function(s) length(unique(s))) >= MIN_K))
    d <- d |> filter(.data[[var]] %in% keep) |> mutate(across(all_of(var), droplevels))
  }
  k_s <- n_distinct(d$study_id)
  if (k_s < MIN_K_MOD) return(tibble(moderator = label, k_studies = k_s, note = "fewer than 10 studies"))
  f <- fit_che(d, mods = as.formula(paste("~", var)))
  wt <- Wald_test(f$m, constraints = constrain_zero(2:length(coef(f$m))), vcov = "CR2", cluster = f$dat$study_id)
  lev <- if (is.factor(d[[var]]) || is.character(d[[var]]))
    paste(sapply(split(d$study_id, d[[var]]), function(s) length(unique(s))), collapse = " / ") else ""
  tibble(moderator = label, k_studies = k_s, k_estimates = nrow(d), studies_per_level = lev,
         term = names(coef(f$m)), b = f$ci$beta,
         ci_lb = f$ci$CI_L, ci_ub = f$ci$CI_U, df = f$ci$df, p = f$rob$p_Satt, reliable = f$ci$df >= 4,
         wald_F = wt$Fstat, wald_p = wt$p_val, wald_df_denom = wt$df_denom)
}

# RQ1: pooled kappa overall and by task type
rq1 <- bind_rows(pooled(kap, "all"),
                 lapply(c("T1", "T2", "T3", "T4"), function(t) pooled(kap |> filter(task_type == t), t)))
write_csv(rq1, file.path(res_dir, "rq1_pooled_kappa.csv"))
mod_task <- moderator(kap |> mutate(task_type = factor(task_type)), "task_type", "task type (G4)")

# RQ2 / G1: matched human-human comparisons
hr <- hr_raw |> filter(pool == "yes", statistic %in% KAPPA, same_units %in% c("yes", "partial"), !study_id %in% excl_studies) |>
  mutate(h = as.numeric(value), hlo = as.numeric(ci_low), hhi = as.numeric(ci_high), hn = num_first(n_units),
         side = ifelse(comparison == "coder-vs-consensus", "aggregate of coders", "single coder")) |>
  left_join(tasks |> select(study_id, task_id, n_task), by = c("study_id", "task_id")) |>
  mutate(hn = coalesce(hn, n_task),
         hse = coalesce(ifelse(!is.na(hlo) & !is.na(hhi) & hhi > hlo, (hhi - hlo) / (2 * qnorm(0.975)), NA),
                        ifelse(!is.na(hn) & hn >= 5, se_kappa(h, hn, PE_MED), NA))) |>
  filter(!is.na(h), !is.na(hse)) |>
  group_by(study_id, task_id, side) |> summarise(h = mean(h), hse = sqrt(mean(hse^2)), .groups = "drop")
delta <- function(matched = TRUE) {
  d <- kap |> filter(!is.na(ref2)) |>
    inner_join(hr, by = c("study_id", "task_id"), relationship = "many-to-many")
  d <- if (matched) d |> filter(side == ref2) else d |> group_by(es_id) |> slice(1) |> ungroup()
  d |> mutate(yi = v - h, vi = se^2 + hse^2)
}
d_m <- delta(TRUE); d_all <- delta(FALSE)
g1 <- bind_rows(pooled(d_m, "delta kappa, matched"), pooled(d_all, "delta kappa, matched and unmatched"),
                lapply(c("T1", "T2", "T3", "T4"), function(t) pooled(d_m |> filter(task_type == t), paste("delta, matched,", t))))
recent <- d_m |> filter(!is.na(rel), rel >= as.Date("2025-01-01"))
g1b <- if (n_distinct(recent$study_id) >= MIN_K) {
  f <- fit_che(recent); ci90 <- conf_int(f$m, vcov = "CR2", cluster = f$dat$study_id, level = 0.90)
  tibble(analysis = "G1b equivalence, models from 2025", k_studies = n_distinct(recent$study_id),
         k_estimates = nrow(recent), est = ci90$beta, ci90_lb = ci90$CI_L, ci90_ub = ci90$CI_U,
         equivalent_within_0.10 = ci90$CI_L > -0.10 & ci90$CI_U < 0.10)
} else tibble(analysis = "G1b", k_studies = n_distinct(recent$study_id))
write_csv(bind_rows(g1, g1b), file.path(res_dir, "g1_delta_kappa.csv"))

# G2: LLM-human kappa on human-human kappa of the same task
g2_dat <- kap |> inner_join(hr |> group_by(study_id, task_id) |> summarise(hh = mean(h), .groups = "drop"),
                            by = c("study_id", "task_id"))
g2 <- moderator(g2_dat, "hh", "human-human kappa (G2)")

# G3: model release date, generation, reasoning; within-study newer minus older
kap3 <- kap |> filter(!is.na(years))
g3 <- bind_rows(moderator(kap3, "years", "release date, years since 2020-06 (G3)"),
                moderator(kap3 |> mutate(generation = factor(generation, levels = c("to 2023-03", "GPT-4 era (to 2024-04)",
                          "GPT-4o era (to 2024-12)", "2025-2026"))), "generation", "generation (G3)"),
                moderator(kap3 |> mutate(reasoning_model = factor(reasoning_model)), "reasoning_model", "reasoning model (G3)"))
within <- kap3 |> group_by(study_id, task_id, statistic, reference) |> filter(n_distinct(rel) > 1) |>
  summarise(yi = v[which.max(rel)] - v[which.min(rel)], vi = se[which.max(rel)]^2 + se[which.min(rel)]^2,
            .groups = "drop")
g3w <- pooled(within, "within-study contrast, newest minus oldest model (G3)")
write_csv(bind_rows(g3, tibble()), file.path(res_dir, "g3_release.csv"))
write_csv(g3w, file.path(res_dir, "g3_within_study.csv"))

# G4-G10 and other moderators
mods <- bind_rows(
  mod_task,
  moderator(kap |> mutate(construct_type = factor(ifelse(construct_type %in% c("manifest", "latent"), construct_type, NA))),
            "construct_type", "construct type (G4)"),
  moderator(kap |> mutate(prompt = factor(prompt, levels = c("zero-shot", "few-shot", "fine-tuned"))), "prompt", "prompting (G5)"),
  moderator(kap |> mutate(log_cat = log(n_categories_n)), "log_cat", "log number of categories (G6)"),
  moderator(kap |> mutate(ref2 = factor(ref2)), "ref2", "reference: aggregate vs single coder (G7)"),
  moderator(kap |> mutate(sel = factor(ifelse(all_configs_reported == "no", "best only", "all or single"))), "sel",
            "configurations reported (G9)"),
  moderator(kap |> mutate(rob2 = factor(ifelse(rob_2 %in% c("low", "high"), rob_2, NA))), "rob2", "risk of bias, configuration (G9)"),
  moderator(kap |> mutate(english = factor(english)), "english", "language (G10)"),
  moderator(kap |> mutate(open = factor(ifelse(open_weights %in% c("yes", "no"), open_weights, NA))), "open", "open weights"),
  moderator(kap |> mutate(expert = factor(ifelse(human_expertise %in% c("clinician-or-expert", "trained-coder", "crowd"),
                                                  human_expertise, NA))), "expert", "human expertise"),
  moderator(kap |> mutate(src = factor(ifelse(text_source %in% c("real", "synthetic"), text_source, NA))), "src", "real vs synthetic texts"),
  moderator(kap |> mutate(rob4 = factor(ifelse(rob_4 %in% c("low", "high"), rob_4, NA))), "rob4", "contamination (risk of bias 4)"),
  moderator(kap |> mutate(peer = factor(peer)), "peer", "peer-reviewed"))
write_csv(bind_rows(mods, g2), file.path(res_dir, "moderators.csv"))

# G8: observed agreement minus kappa within the same configuration
g8 <- kap |> filter(!is.na(po), statistic %in% c("cohen_kappa", "fleiss_kappa")) |>
  mutate(yi = po - v, vi = se^2)
write_csv(pooled(g8, "G8: observed agreement minus kappa, same configuration"), file.path(res_dir, "g8.csv"))

# Sensitivity analyses (section 15c)
one_per_study <- kap |> group_by(study_id) |>
  arrange(desc(authors_primary == "yes"), desc(rel), .by_group = TRUE) |> slice(1) |> ungroup()
hk <- rma(yi, vi, data = one_per_study, method = "REML", test = "knha")
sens <- bind_rows(
  pooled(kap |> filter(se_source != "n and imputed p_e"), "excluding imputed p_e"),
  pooled(kap |> filter(se_source == "CI" | se_source == "n and observed p_e"), "SE from CI or observed p_e only"),
  pooled(kap |> filter(!grepl("weighted", statistic)), "excluding weighted kappa"),
  pooled(kap |> filter(!statistic %in% c("krippendorff_alpha", "gwet_ac1", "pabak")), "excluding alpha, AC1, PABAK"),
  pooled(kap |> filter(peer), "peer-reviewed only"),
  pooled(kap, "within-study correlation 0.3", rho = 0.3),
  pooled(kap, "within-study correlation 0.8", rho = 0.8),
  tibble(analysis = "one estimate per study, REML with Knapp-Hartung", k_studies = hk$k, k_estimates = hk$k,
         est = as.numeric(hk$b), ci_lb = hk$ci.lb, ci_ub = hk$ci.ub,
         pi_lb = predict(hk)$pi.lb, pi_ub = predict(hk)$pi.ub),
  pooled(kap |> filter(rob_4 != "high"), "excluding high contamination risk"),
  pooled(kap |> filter(text_source != "synthetic"), "excluding synthetic texts"),
  pooled(kap |> filter(own_study != "yes"), "excluding R1's own study"))
loo <- bind_rows(lapply(unique(kap$study_id), function(s) pooled(kap |> filter(study_id != s), s)))
sens <- bind_rows(sens, tibble(analysis = "leave-one-study-out: range of pooled kappa",
                               est = NA, ci_lb = min(loo$est), ci_ub = max(loo$est)))
write_csv(sens, file.path(res_dir, "sensitivity.csv"))
write_csv(loo |> select(left_study = analysis, est, ci_lb, ci_ub), file.path(res_dir, "leave_one_out.csv"))

# Small-study effects (section 16): SE as moderator in the CHE model with CR2 inference
egger <- bind_rows(lapply(c("all", "T1", "T2", "T3", "T4"), function(t) {
  d <- if (t == "all") kap else kap |> filter(task_type == t)
  if (n_distinct(d$study_id) < MIN_K_MOD) return(tibble(subset = t, k_studies = n_distinct(d$study_id)))
  f <- fit_che(d |> mutate(sei = sqrt(vi)), mods = ~ sei)
  tibble(subset = t, k_studies = n_distinct(d$study_id), slope_se = f$ci$beta[2], p = f$rob$p_Satt[2])
}))
write_csv(egger, file.path(res_dir, "small_study_effects.csv"))

# Secondary outcome: ICC and correlations on Fisher's z (ICC: Bonett, 2002, k = 2 raters)
sec <- est_all |> filter(pool == "yes", statistic %in% CORR, !is.na(v), abs(v) < 1, !is.na(n), n > 4) |>
  mutate(yi = atanh(v), vi = ifelse(statistic == "icc", 1 / (n - 2), 1 / (n - 3)))
rq1_sec <- bind_rows(pooled(sec, "all", back = tanh),
                     lapply(c("T1", "T2", "T3", "T4"), function(t) pooled(sec |> filter(task_type == t), t, back = tanh)))
write_csv(rq1_sec, file.path(res_dir, "rq1_pooled_icc_r.csv"))

# Descriptive: studies by statistics reported
by_study <- est_all |> filter(pool == "yes") |> group_by(study_id) |>
  summarise(kappa = any(statistic %in% KAPPA), corr = any(statistic %in% CORR),
            descriptive_only = !any(statistic %in% c(KAPPA, CORR)), .groups = "drop")
desc <- list(studies_included = n_distinct(est_all$study_id), studies_kappa = sum(by_study$kappa),
             studies_icc_r = sum(by_study$corr), studies_descriptive_only = sum(by_study$descriptive_only),
             kappa_estimates = nrow(kap), kappa_dropped_no_se = sum(est_all$pool == "yes" & est_all$statistic %in% KAPPA) - nrow(kap),
             pe_median = PE_MED, pe_observed = sum(!is.na(kap$pe_obs)),
             studies_human_reliability = n_distinct(hr$study_id), delta_matched_estimates = nrow(d_m),
             delta_matched_studies = n_distinct(d_m$study_id))

# GRADE indicators for pooled kappa per task type (section 17)
grade <- rq1 |> filter(!is.na(est)) |> rowwise() |> mutate(
  d = list(if (analysis == "all") kap else kap |> filter(task_type == analysis)),
  share_high_rob = mean((d |> distinct(study_id, rob_1, rob_2, rob_3) |>
                           mutate(h = rob_1 == "high" | rob_2 == "high" | rob_3 == "high"))$h),
  share_english = mean(d$english == "English", na.rm = TRUE),
  rob_down = share_high_rob > 0.5, inconsistency_down = band(pi_lb) != band(pi_ub),
  imprecision_down = band(ci_lb) != band(ci_ub), indirectness_down = share_english > 0.8,
  # only a positive slope (smaller studies, higher kappa) points to small-study bias; for kappa the SE also falls as
  # kappa rises (p_o near 1), so a negative slope is expected from the statistic itself
  pub_bias_down = { e <- egger |> filter(subset == analysis)
                    nrow(e) == 1 && !is.na(e$p) && e$p < 0.10 && e$slope_se > 0 },
  downgrades = sum(c(rob_down, inconsistency_down, imprecision_down, indirectness_down, pub_bias_down)),
  certainty = c("high", "moderate", "low", "very low")[min(downgrades, 3) + 1]) |>
  ungroup() |> select(-d)
write_csv(grade, file.path(res_dir, "grade.csv"))

write(toJSON(list(descriptive = desc, rq1_kappa = rq1, rq1_icc_r = rq1_sec, g1 = bind_rows(g1, g1b), g3_within = g3w),
             auto_unbox = TRUE, pretty = TRUE, digits = 4), file.path(res_dir, "summary.json"))
saveRDS(list(kap = kap, sec = sec, d_m = d_m, g2_dat = g2_dat, hr = hr), file.path(res_dir, "analysis_data.rds"))
writeLines(capture.output(sessionInfo()), file.path(root, "analysis", "sessionInfo.txt"))
cat("done\n")
