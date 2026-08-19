import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/cs2_production.py"
LAUNCHER = ROOT / "sidecar/launch_flo.sh"
spec = importlib.util.spec_from_file_location("cs2_production", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def test_contract_round_trips_real_course_metadata():
    assert module._contract() == {
        "title": "Computer Science II",
        "section_identity": "COMSC-1053-1417",
        "term": "Fall 2026",
        "instructor": "Dr. Jeremy P. Evert",
    }


def test_candidate_match_requires_name_section_and_fall_2026_term():
    contract = {
        "title": "Computer Science II",
        "section_identity": "COMSC-1053-1417",
        "term": "Fall 2026",
        "instructor": "Dr. Jeremy P. Evert",
    }
    good = {
        "name": "Computer Science II",
        "course_code": "COMSC-1053-1417",
        "sis_course_id": "",
        "term": {"name": "Fall 2026"},
    }
    assert module._candidate_matches(good, contract)
    assert module._candidate_matches({**good, "name": "COMSC-1053 Computer Science 2"}, contract)
    assert not module._candidate_matches({**good, "course_code": "COMSC-1053-9999"}, contract)
    assert not module._candidate_matches({**good, "name": "Computer Science I"}, contract)
    assert not module._candidate_matches({**good, "term": {"name": "Fall 2025"}}, contract)


def test_authorization_token_is_bound_to_exact_dry_run_log():
    target = {"id": 123, "name": "Computer Science II", "course_code": "COMSC-1053-1417"}
    states = {"computer_science_2": {"head": "a" * 40, "branch": "main"}}
    dry = {
        "created_count": 1,
        "updated_count": 2,
        "deleted_count": 0,
        "log": [{"module_title": "Week 2", "object_title": "X", "action": "create"}],
    }
    first = module._authorization_token(
        target=target, source_states=states, plan_digest="b" * 64, dry_run=dry
    )
    changed = dict(dry)
    changed["log"] = [{"module_title": "Week 2", "object_title": "Y", "action": "create"}]
    second = module._authorization_token(
        target=target, source_states=states, plan_digest="b" * 64, dry_run=changed
    )
    assert first != second
    assert len(first) == 24


def test_status_path_handles_plain_and_rename_porcelain_lines():
    assert module._status_path("?? sidecar/runs/foo.json") == "sidecar/runs/foo.json"
    assert module._status_path("R  old.txt -> new.txt") == "new.txt"


def test_savnac_acceptance_shape_is_pinned():
    assert module.EXPECTED_MODULE_COUNT == 16
    assert module.EXPECTED_OBJECT_COUNT == 155
    assert module.EXPECTED_ASSIGNMENT_GROUP_COUNT == 14


def test_flo_launcher_provisions_every_repo_cs2_compiler_reads():
    text = LAUNCHER.read_text()
    for repo in (
        "computer_science_2",
        "course_foundry",
        "harbor",
        "imprint",
        "local_ai_lab_setup",
        "ai_fluency",
        "professional_minds",
        "computer_science_1",
    ):
        assert repo in text
