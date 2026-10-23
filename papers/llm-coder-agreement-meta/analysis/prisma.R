# PRISMA 2020 flow diagram: databases, search engines and repositories; citation searching (deviations.md D6).
#
# Reads fulltext/prisma_counts.json (fulltext/ft_summary.py), the citation-search files (chase_log.json, the AI labels,
# fulltext/retrieval_log.csv, fulltext/decisions/ft_R1_chase.csv) and forms/studies.csv, forms/estimates.csv;
# writes analysis/figures/prisma.pdf and prisma.tiff and analysis/results/prisma_flow.json.
# Template: papers/ai-dependence-correlates/analysis/prisma.R.
# Run from the repository root: Rscript papers/llm-coder-agreement-meta/analysis/prisma.R

suppressPackageStartupMessages({ library(ggplot2); library(jsonlite) })
paper <- "papers/llm-coder-agreement-meta"
pc <- fromJSON(file.path(paper, "fulltext", "prisma_counts.json"))
fig_dir <- file.path(paper, "analysis", "figures")
fmt <- function(x) prettyNum(x, big.mark = ",")
rd <- function(f) read.csv(file.path(paper, f), colClasses = "character", check.names = FALSE, encoding = "UTF-8")

src_names <- c(pubmed = "PubMed", europepmc = "Europe PMC", openalex = "OpenAlex", s2 = "Semantic Scholar",
               arxiv = "arXiv", psyarxiv = "PsyArXiv (OSF)", crossref = "Crossref", datacite = "DataCite", core = "CORE")
by_src <- unlist(pc$records_per_source)
src_txt <- paste(sprintf("%s (n = %s)", src_names[names(by_src)], fmt(by_src)), collapse = "\n")
excl_names <- c(E3_not_psychological = "No psychological or clinical construct", no_human_coding = "No human coding of the same units",
                E5_no_generative_llm = "No generative LLM", E2_external_criterion = "External criterion, not coders",
                other = "Other", E4_theme_level_only = "Theme-level agreement only", E1_humans_rate_llm = "Humans rate LLM output",
                E6_design = "Design (review, protocol)", E7_duplicate = "Duplicate report")
lines_excl <- function(x) { x <- x[order(-x)]; paste(sprintf("%s (n = %s)", excl_names[names(x)], fmt(x)), collapse = "\n") }
excl <- unlist(pc$reports_excluded_full_text)

# citation searching
cl <- fromJSON(file.path(paper, "search", "runs", "2026-10-23-citations", "chase_log.json"))
lab <- lapply(c("opus", "sonnet"), function(p) stream_in(file(file.path(paper, "screening", "llm",
                                                                       sprintf("chase_2026-10-23_%s.jsonl", p))), verbose = FALSE))
dec <- merge(data.frame(id = lab[[1]]$conv_id, a = lab[[1]]$codes$decision),
             data.frame(id = lab[[2]]$conv_id, b = lab[[2]]$codes$decision))
kept <- dec$id[dec$a != "exclude" | dec$b != "exclude"]
rl <- rd("fulltext/retrieval_log.csv")
retrieved <- intersect(kept, rl$rec_id[rl$status == "retrieved"])
fc <- rd("fulltext/decisions/ft_R1_chase.csv")
cex <- table(fc$reason[fc$decision == "not_eligible"])
ch <- list(new = cl$new_unique_records, auto = sum(unlist(cl$auto_removed)), screened = cl$to_screen,
           excluded = cl$to_screen - length(kept), sought = length(kept), not_retrieved = length(kept) - length(retrieved),
           assessed = length(retrieved), excluded_ft = sum(cex), included = sum(fc$decision == "eligible"))

# included studies
st <- rd("forms/studies.csv"); es <- rd("forms/estimates.csv")
st_in <- st[st$excluded_r1 == "", ]
pooled <- es[es$include == "yes" & es$pool == "yes" & !(es$study_id %in% st$study_id[st$excluded_r1 != ""]), ]
kap_s <- unique(pooled$study_id[pooled$outcome == "primary"])
cor_s <- unique(pooled$study_id[pooled$outcome == "secondary"])
rep_in <- length(unique(unlist(strsplit(st_in$report_ids, ";"))))
excluded_extraction <- st$study_id[st$excluded_r1 != ""]
flow <- list(main = pc[c("records_identified", "duplicates_removed", "records_screened_title_abstract",
                         "records_excluded_title_abstract", "reports_sought_for_retrieval", "reports_not_retrieved",
                         "reports_assessed_for_eligibility", "reports_included")],
             removed_by_automation = pc$removed_by_automation, citation_searching = ch,
             excluded_at_extraction = list(studies = excluded_extraction, reasons = st$excluded_r1[st$excluded_r1 != ""]),
             studies_included = nrow(st_in), reports_of_included_studies = rep_in,
             studies_with_kappa = length(kap_s), studies_with_icc_or_r = length(cor_s),
             studies_with_kappa_or_icc_r = length(union(kap_s, cor_s)))
write(toJSON(flow, auto_unbox = TRUE, pretty = TRUE), file.path(paper, "analysis", "results", "prisma_flow.json"))

boxes <- data.frame(
  x = c(1, 3, 1, 3, 1, 3, 1, 3, 1), y = c(9, 9, 7, 7, 5, 5, 3, 3, 1), w = 1.8,
  h = c(1.9, 1.0, 0.7, 0.7, 0.7, 0.7, 0.7, 1.55, 1.45),
  label = c(
    paste0("Records identified (n = ", fmt(pc$records_identified), "):\n", src_txt),
    paste0("Records removed before screening:\nDuplicate records (n = ", fmt(pc$duplicates_removed),
           ")\nNon-study records (n = ", fmt(pc$removed_by_automation$non_study_records),
           ")\nNo exact search-term match (n = ", fmt(pc$removed_by_automation$no_exact_search_term_match), ")"),
    paste0("Records screened\n(n = ", fmt(pc$records_screened_title_abstract), ")"),
    paste0("Records excluded\n(n = ", fmt(pc$records_excluded_title_abstract), ")"),
    paste0("Reports sought for retrieval\n(n = ", fmt(pc$reports_sought_for_retrieval), ")"),
    paste0("Reports not retrieved\n(no open full text; n = ", fmt(pc$reports_not_retrieved), ")"),
    paste0("Reports assessed for eligibility\n(n = ", fmt(pc$reports_assessed_for_eligibility), ")"),
    paste0("Reports excluded (n = ", fmt(sum(excl)), "):\n", lines_excl(excl)),
    sprintf(paste0("Studies included in review (n = %d)\nReports of included studies (n = %d)\n",
                   "Excluded at data extraction: %d studies\n\nStudies with kappa-family estimates (n = %d)\n",
                   "Studies with ICC or correlations (n = %d)"),
            nrow(st_in), rep_in, length(excluded_extraction), length(kap_s), length(cor_s))),
  stringsAsFactors = FALSE)
arrows <- data.frame(x = c(1, 1.9, 1, 1.9, 1, 1.9, 1, 1.9), y = c(9 - 0.95, 9, 7 - 0.35, 7, 5 - 0.35, 5, 3 - 0.35, 3),
                     xend = c(1, 2.1, 1, 2.1, 1, 2.1, 1, 2.1), yend = c(7 + 0.35, 9, 5 + 0.35, 7, 3 + 0.35, 5, 1 + 0.73, 3))
other <- data.frame(
  x = c(5, 7, 5, 7, 5, 7, 5, 7), y = c(9, 9, 7, 7, 5, 5, 3, 3), w = 1.8, h = c(1.0, 0.9, 0.7, 0.7, 0.7, 0.7, 0.7, 1.4),
  label = c(
    paste0("Records identified from citation\nsearching (not in the database set;\nn = ", fmt(ch$new), ")"),
    paste0("Removed by the same automatic\nrules (before 2020, non-study,\nno exact term match; n = ", fmt(ch$auto), ")"),
    paste0("Records screened\n(n = ", fmt(ch$screened), ")"),
    paste0("Records excluded\n(n = ", fmt(ch$excluded), ")"),
    paste0("Reports sought for retrieval\n(n = ", fmt(ch$sought), ")"),
    paste0("Reports not retrieved\n(no open full text; n = ", fmt(ch$not_retrieved), ")"),
    paste0("Reports assessed for eligibility\n(n = ", fmt(ch$assessed), ")"),
    paste0("Reports excluded (n = ", fmt(ch$excluded_ft), "):\n", lines_excl(cex),
           "\nReports included (n = ", ch$included, ")")),
  stringsAsFactors = FALSE)
boxes <- rbind(boxes, other)
arrows <- rbind(arrows, data.frame(x = c(5, 5.9, 5, 5.9, 5, 5.9, 5.9), y = c(9 - 0.5, 9, 7 - 0.35, 7, 5 - 0.35, 5, 3),
                                   xend = c(5, 6.1, 5, 6.1, 5, 6.1, 6.1), yend = c(7 + 0.35, 9, 5 + 0.35, 7, 3 + 0.35, 5, 3)))
arrows <- rbind(arrows, data.frame(x = 5, y = 3 - 0.35, xend = 1.9, yend = 1.2))

p <- ggplot() +
  geom_rect(data = boxes, aes(xmin = x - w / 2, xmax = x + w / 2, ymin = y - h / 2, ymax = y + h / 2),
            fill = "white", colour = "black", linewidth = 0.3) +
  geom_text(data = boxes, aes(x = x, y = y, label = label), size = 2.2, lineheight = 0.95) +
  geom_segment(data = arrows, aes(x = x, y = y, xend = xend, yend = yend),
               arrow = arrow(length = unit(0.12, "cm"), type = "closed"), linewidth = 0.3) +
  annotate("text", x = -0.25, y = c(9, 6, 1), label = c("Identification", "Screening", "Included"),
           angle = 90, size = 2.8, fontface = "bold") +
  annotate("text", x = c(2, 6), y = 10.35, label = c("Databases, search engines and repositories", "Citation searching"),
           size = 2.8, fontface = "bold") +
  coord_cartesian(xlim = c(-0.4, 8), ylim = c(0.2, 10.6)) + theme_void()
ggsave(file.path(fig_dir, "figure1_prisma.pdf"), p, width = 12, height = 8.3)
ggsave(file.path(fig_dir, "figure1_prisma.tiff"), p, width = 12, height = 8.3, dpi = 600, bg = "white", compression = "lzw")
cat("PRISMA ->", fig_dir, "\n")
