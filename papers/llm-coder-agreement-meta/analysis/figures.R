# Figures for the manuscript (analysis.R must run first). Writes PDF and 300-dpi TIFF to analysis/figures/.
# Colours: categorical slots 1-4 of the validated default palette (dataviz skill, light surface; all checks pass, contrast
# below 3:1 for slots 3-4, so every mark is also labelled by axis text or direct labels).
# Run from the repository root: Rscript papers/llm-coder-agreement-meta/analysis/figures.R

suppressPackageStartupMessages({ library(ggplot2); library(dplyr); library(readr) })
root <- "papers/llm-coder-agreement-meta"
res <- file.path(root, "analysis", "results"); fig <- file.path(root, "analysis", "figures")
dir.create(fig, showWarnings = FALSE)
COL <- c(T1 = "#2a78d6", T2 = "#eb6834", T3 = "#1baf7a", T4 = "#eda100", All = "#52514e")
LAB <- c(All = "All tasks", T1 = "T1 Codebook coding", T2 = "T2 Assessment scoring", T3 = "T3 Clinical state rating",
         T4 = "T4 LLM-as-a-judge")
theme_paper <- theme_minimal(base_size = 10) +
  theme(panel.grid.minor = element_blank(), panel.grid.major.y = element_blank(),
        panel.grid.major.x = element_line(colour = "#e6e5e1", linewidth = 0.3),
        axis.text = element_text(colour = "#52514e"), plot.background = element_rect(fill = "white", colour = NA),
        legend.position = "none", strip.text = element_text(face = "bold", hjust = 0))
save <- function(p, name, w, h) {
  ggsave(file.path(fig, paste0(name, ".pdf")), p, width = w, height = h, device = cairo_pdf)
  ggsave(file.path(fig, paste0(name, ".tiff")), p, width = w, height = h, dpi = 300, compression = "lzw", bg = "white")
}
d <- readRDS(file.path(res, "analysis_data.rds"))

# Figure 2: pooled agreement by task type (kappa; ICC and correlations), CI thick, prediction interval thin
pool <- bind_rows(read_csv(file.path(res, "rq1_pooled_kappa.csv"), show_col_types = FALSE) |> mutate(outcome = "Kappa family (primary)"),
                  read_csv(file.path(res, "rq1_pooled_icc_r.csv"), show_col_types = FALSE) |> mutate(outcome = "ICC and correlations (secondary)")) |>
  mutate(task = ifelse(analysis == "all", "All", analysis), label = factor(LAB[task], levels = rev(LAB)),
         outcome = factor(outcome, levels = c("Kappa family (primary)", "ICC and correlations (secondary)")),
         txt = sprintf("%.2f [%.2f, %.2f]  k = %d", est, ci_lb, ci_ub, k_studies))
p2 <- ggplot(pool, aes(y = label, colour = task)) +
  geom_linerange(aes(xmin = pmax(pi_lb, -0.4), xmax = pi_ub), linewidth = 0.5, alpha = 0.6) +
  geom_linerange(aes(xmin = ci_lb, xmax = ci_ub), linewidth = 2.2) +
  geom_point(aes(x = est), size = 2.6, colour = "white") + geom_point(aes(x = est), size = 1.8) +
  geom_text(aes(x = 1.05, label = txt), hjust = 0, size = 2.7, colour = "#0b0b0b") +
  scale_colour_manual(values = COL) + scale_x_continuous(limits = c(-0.4, 1.75), breaks = seq(-0.2, 1, 0.2)) +
  facet_wrap(~ outcome, ncol = 1) + labs(x = "Pooled agreement with the human reference", y = NULL) + theme_paper
save(p2, "figure2_pooled", 7, 4.6)

# Figure 3: LLM-human kappa vs human-human kappa on the same task (G2), with the line of equality
g2 <- d$g2_dat |> group_by(study_id, task_id, task_type) |> summarise(llm = mean(v), hh = mean(hh), n = n(), .groups = "drop")
p3 <- ggplot(g2, aes(hh, llm, colour = task_type)) +
  geom_abline(slope = 1, intercept = 0, linetype = "dashed", colour = "#52514e", linewidth = 0.4) +
  geom_point(aes(size = n), alpha = 0.85, stroke = 0) +
  annotate("text", x = 0.97, y = 0.99, label = "equal agreement", hjust = 1, vjust = -0.4, size = 2.7, colour = "#52514e") +
  scale_colour_manual(values = COL, labels = LAB[c("T1", "T2", "T3", "T4")], name = NULL) + scale_size_area(max_size = 5, guide = "none") +
  guides(colour = guide_legend(nrow = 2, override.aes = list(size = 3, alpha = 1))) +
  coord_equal(xlim = c(0, 1), ylim = c(-0.1, 1)) +
  labs(x = "Human-human kappa (same task)", y = "LLM-human kappa (mean per task)") +
  theme_paper + theme(legend.position = "bottom", panel.grid.major.y = element_line(colour = "#e6e5e1", linewidth = 0.3))
save(p3, "figure3_human_ceiling", 5.2, 5.6)

# Figure 4: kappa by model release date (G3)
g3 <- d$kap |> filter(!is.na(rel))
p4 <- ggplot(g3, aes(rel, v, colour = task_type)) +
  geom_point(alpha = 0.55, size = 1.4, stroke = 0) +
  geom_smooth(aes(group = 1), method = "lm", formula = y ~ x, colour = "#0b0b0b", linewidth = 0.6, se = FALSE) +
  scale_colour_manual(values = COL, labels = LAB[c("T1", "T2", "T3", "T4")], name = NULL) +
  scale_y_continuous(limits = c(-0.3, 1)) +
  guides(colour = guide_legend(nrow = 2, override.aes = list(size = 3, alpha = 1))) +
  labs(x = "Model release date", y = "LLM-human kappa",
       caption = "Line: unweighted linear trend for display; the CHE meta-regression slope is reported in the text.") +
  theme_paper + theme(legend.position = "bottom", panel.grid.major.y = element_line(colour = "#e6e5e1", linewidth = 0.3),
                      plot.caption = element_text(colour = "#52514e", size = 7))
save(p4, "figure4_release_date", 6.5, 4.2)
cat("figures written\n")
