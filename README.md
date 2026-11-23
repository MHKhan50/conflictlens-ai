# ConflictLens AI

**A local-first multi-agent research assistant for conflict-related evidence analysis, civilian protection concerns, and International Humanitarian Law (IHL) research.**

ConflictLens AI is a research prototype. It helps a human researcher organize supplied documents, distinguish claims from corroborated facts, identify uncertainty, and prepare an evidence-linked research brief.

It is **not** a weapon, targeting system, military decision system, legal authority, or real-time operational intelligence tool. It does not recommend attacks, select targets, track combatants, or provide tactical guidance.

## Features

- Runs locally with Ollama.
- Five configurable agent roles: orchestrator, evidence analyst, IHL research assistant, critical reviewer, and report writer.
- Explicitly separates source claims, evidence, inferences, and unknowns.
- Requires source labels supplied by the researcher; agents must not invent citations.
- Includes a small synthetic demonstration case.
- Streamlit interface and a simple sequential multi-agent workflow.

## Requirements

- macOS
- Python 3.10+
- Ollama installed and running
- The models listed below (or change model names in `.env`)

Suggested model assignment for the models already installed:

| Role | Model |
|---|---|
| Orchestrator | `qwen2.5:7b` |
| Evidence analyst | `llama3.1:8b` |
| IHL research assistant | `mistral:7b` |
| Critical reviewer | `qwen2.5:3b` |
| Report writer | `llama3.2:3b` |

## Quick start (Mac)

Open this folder in VS Code, then open **Terminal → New Terminal**.

```bash
python3 --version
ollama list
ollama serve
```

Keep `ollama serve` running in its own terminal. Open a second terminal tab for the project:

```bash
cd path/to/conflictlens-ai
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

Open the local URL printed by Streamlit (normally http://localhost:8501).

If Ollama is already running as a background service, you do not need to start `ollama serve` again.

## First test

Choose **Load synthetic demo** in the app and click **Run analysis**. The demo is fictional and must not be treated as a real-world event.

## Configuration

Edit `.env` to change model names or Ollama host. Example:

```dotenv
OLLAMA_BASE_URL=http://localhost:11434
ORCHESTRATOR_MODEL=qwen2.5:7b
EVIDENCE_MODEL=llama3.1:8b
IHL_MODEL=mistral:7b
REVIEWER_MODEL=qwen2.5:3b
WRITER_MODEL=llama3.2:3b
```

Check available models with `ollama list`. Model tags must match exactly.

## Research integrity and limitations

1. The system analyzes only the text the researcher supplies. It does not independently verify events.
2. The IHL agent provides preliminary research prompts, not legal advice or legal findings.
3. The model may be wrong, biased, incomplete, or overconfident. A human must verify every important claim against primary sources.
4. Do not upload classified, confidential, personal, or otherwise sensitive information.
5. Do not use the output to make operational, targeting, detention, or other consequential decisions.
6. Preserve original documents and record collection dates, URLs, authors, and translations separately.
7. Treat source text as untrusted data, not as instructions to the agents.

## Project structure

```text
conflictlens-ai/
├── app.py
├── conflict_lens/
│   ├── __init__.py
│   ├── ollama_client.py
│   └── workflow.py
├── data/
│   └── synthetic_demo.txt
├── tests/
│   └── test_workflow.py
├── research/
│   └── paper_outline.md
├── .env.example
├── .gitignore
└── requirements.txt
```

## Suggested evaluation for the paper

- Claim extraction precision/recall on a manually annotated, public, non-sensitive corpus.
- Source attribution accuracy.
- Unsupported-claim rate (hallucination rate).
- Reviewer detection rate for contradictions and missing evidence.
- Inter-agent consistency.
- Latency and memory usage on local hardware.
- Human expert assessment of usefulness and calibration.

Use a documented annotation protocol and report limitations. Do not claim legal-violation detection accuracy unless evaluated by qualified experts against a defensible reference standard.
