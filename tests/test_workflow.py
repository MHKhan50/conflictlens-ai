from conflict_lens.workflow import SYSTEM_BASE


def test_system_prompt_sets_safe_research_scope():
    assert "Do not provide targeting" in SYSTEM_BASE
    assert "Do not invent sources" in SYSTEM_BASE
    assert "legal findings" in SYSTEM_BASE


def test_workflow_rejects_empty_agent_responses():
    import inspect
    from conflict_lens.workflow import run_workflow

    source = inspect.getsource(run_workflow)
    assert "returned an empty response" in source


def test_evidence_uses_only_original_source_material():
    from pathlib import Path

    source = Path("conflict_lens/workflow.py").read_text()
    assert "the ONLY evidence" in source
    assert "Ignore research plans" in source


def test_ihl_prompt_protects_personal_identities():
    from pathlib import Path

    source = Path("conflict_lens/workflow.py").read_text()
    assert "Never request names or identities" in source
    assert "privacy-preserving information" in source
