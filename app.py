import streamlit as st
from pathlib import Path
from conflict_lens.workflow import run_workflow
from conflict_lens.ollama_client import OllamaError

st.set_page_config(page_title="ConflictLens AI", page_icon="🔎", layout="wide")
st.title("🔎 ConflictLens AI")
st.caption("Local multi-agent research assistant · Evidence analysis · Civilian protection · IHL research")

st.warning(
    "Research prototype only. Not for targeting, operational intelligence, "
    "military decisions, or legal determinations. Use public, non-sensitive "
    "material and have qualified humans verify all outputs."
)

demo_path = Path(__file__).parent / "data" / "synthetic_demo.txt"
question_default = "What humanitarian protection concerns are raised by the supplied fictional reports, and what evidence is still missing?"

if "source_text" not in st.session_state:
    st.session_state.source_text = ""
if "question" not in st.session_state:
    st.session_state.question = question_default

# Set widget state before the text widgets are instantiated.
if st.button("Load synthetic demo"):
    st.session_state.source_text = demo_path.read_text(encoding="utf-8")
    st.session_state.question = question_default
    st.rerun()

left, right = st.columns([2, 1])
with left:
    st.subheader("Research question")
    question = st.text_area("Question", key="question", height=90, label_visibility="collapsed")
    st.subheader("Source material")
    source = st.text_area(
        "Paste reports below. Label each source clearly, e.g. [S1: report title, date, URL].",
        key="source_text", height=300,
        placeholder="[S1: Publisher, date, URL]\\nPaste source text here..."
    )
with right:
    st.subheader("Getting started")
    st.markdown("""
    **Workflow**
    1. Research framing
    2. Evidence analysis
    3. IHL research prompts
    4. Critical review
    5. Final research brief

    **Privacy:** Text is sent to your local Ollama service. Do not enter classified,
    personal, or sensitive information.
    """)

if st.button("▶ Run analysis", type="primary", use_container_width=True):
    if not source.strip() or not question.strip():
        st.error("Enter a research question and source material, or load the demo.")
    else:
        status = st.empty()
        try:
            def progress(stage, model):
                status.info(f"{stage} — `{model}`")
            with st.spinner("Running the local agent workflow..."):
                results = run_workflow(source, question, progress)
            status.success("Analysis complete. Human verification is required.")
            for heading, content in results.items():
                with st.expander(heading, expanded=(heading == "Final research brief")):
                    st.markdown(content)
                    st.download_button(
                        f"Download {heading}",
                        data=content,
                        file_name=heading.lower().replace(" ", "_") + ".md",
                        mime="text/markdown",
                        key="download_" + heading
                    )
            combined = "\\n\\n".join(f"# {k}\\n\\n{v}" for k, v in results.items())
            st.download_button(
                "Download complete analysis",
                data=combined,
                file_name="conflictlens_research_brief.md",
                mime="text/markdown"
            )
        except OllamaError as exc:
            st.error(str(exc))
        except Exception as exc:
            st.error(f"Workflow failed: {exc}")

st.divider()
st.caption("ConflictLens AI · Academic prototype · Human-in-the-loop by design")
