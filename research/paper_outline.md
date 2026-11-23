# Proposed Research Paper

## Working title
**ConflictLens AI: A Local Multi-Agent Framework for Evidence-Grounded Humanitarian Conflict Analysis**

## Abstract (to be written after evaluation)
Describe the research problem, system design, dataset, evaluation protocol, main
results, and limitations. Do not write performance claims before experiments.

## 1. Introduction
- Information fragmentation in conflict-related humanitarian reporting.
- Risks of unsupported claims, source confusion, and overconfident summaries.
- Research question: can a local multi-agent workflow improve evidence traceability
  and uncertainty reporting compared with a single-model baseline?

## 2. Related Work
- Retrieval-augmented generation and source attribution.
- Multi-agent LLM systems and critique workflows.
- Humanitarian information management.
- IHL documentation and the limits of automated legal analysis.

## 3. System Design
- Local Ollama inference and model configuration.
- Orchestrator, evidence analyst, IHL research assistant, reviewer, report writer.
- Data flow, prompts, provenance, safety boundaries, and human oversight.

## 4. Dataset and Annotation
- Use public, non-sensitive, appropriately licensed reports.
- Define a source and claim annotation protocol.
- Have at least two annotators label claims, evidence links, contradictions,
  uncertainty, and humanitarian-protection themes.
- Resolve disagreements and report inter-annotator agreement.
- Exclude personal data and operationally sensitive details.

## 5. Experimental Setup
Compare:
1. Single-model summarization baseline.
2. Multi-agent workflow without critical reviewer.
3. Full ConflictLens workflow.

Keep model versions, prompts, hardware, decoding settings, and dataset splits fixed
and documented.

## 6. Evaluation Metrics
- Claim extraction precision, recall, and F1.
- Evidence attribution accuracy.
- Unsupported-claim / hallucination rate.
- Contradiction detection precision and recall.
- Calibration and uncertainty quality (human rubric).
- Expert-rated usefulness and readability.
- Runtime, tokens, and memory footprint.

## 7. Results
Insert measured results only. Include confidence intervals where appropriate,
error analysis, and examples of failures.

## 8. Discussion
- What multi-agent review improves and what it does not.
- Local deployment trade-offs.
- Bias, translation, source reliability, and automation risks.
- Why model outputs cannot establish legal responsibility or violations.

## 9. Limitations and Ethics
- Synthetic demo is not an evaluation dataset.
- Public reports can be incomplete or politically framed.
- No autonomous legal determinations or operational use.
- Human expert review is mandatory.

## 10. Conclusion
Summarize evidence from the evaluation and future research directions.

## Reproducibility checklist
- [ ] Dataset provenance and license documented
- [ ] Annotation guide published
- [ ] Model tags and Ollama version recorded
- [ ] Prompts and configuration archived
- [ ] Train/test separation documented if applicable
- [ ] Evaluation scripts and metrics released
- [ ] Failure cases and limitations reported
