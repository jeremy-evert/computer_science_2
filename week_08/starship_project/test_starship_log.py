import runpy
import subprocess
import sys
from pathlib import Path

from starship_log import MissionQueue, show_table


def test_new_queue_is_empty():
    queue = MissionQueue()
    assert queue.is_empty()


def test_queue_is_not_empty_after_enqueue():
    queue = MissionQueue()
    queue.enqueue("Scan Nebula-7")
    assert not queue.is_empty()


# --- Catch-up tests (characterization): written after the code existed ---


def stored_rows(queue):
    return queue._connection.execute(
        "SELECT id, title FROM missions ORDER BY id"
    ).fetchall()


def test_enqueue_stores_the_title_in_the_missions_table():
    queue = MissionQueue()
    queue.enqueue("Scan Nebula-7")
    assert stored_rows(queue) == [(1, "Scan Nebula-7")]


def test_enqueue_keeps_missions_in_insertion_order_with_rising_ids():
    queue = MissionQueue()
    queue.enqueue("Scan Nebula-7")
    queue.enqueue("Survey Kepler-442b")
    assert stored_rows(queue) == [
        (1, "Scan Nebula-7"),
        (2, "Survey Kepler-442b"),
    ]


def test_enqueue_treats_sql_in_a_title_as_plain_text():
    queue = MissionQueue()
    nasty = "x'); DROP TABLE missions;--"
    queue.enqueue(nasty)
    assert stored_rows(queue) == [(1, nasty)]


def test_each_queue_has_its_own_separate_database():
    first = MissionQueue()
    second = MissionQueue()
    first.enqueue("Scan Nebula-7")
    assert second.is_empty()


def test_show_table_reports_an_empty_queue(capsys):
    show_table(MissionQueue())
    out = capsys.readouterr().out
    assert "is_empty() -> True" in out
    assert "(no rows)" in out


def test_show_table_lists_each_mission_with_its_id(capsys):
    queue = MissionQueue()
    queue.enqueue("Scan Nebula-7")
    queue.enqueue("Survey Kepler-442b")
    show_table(queue)
    out = capsys.readouterr().out
    assert "is_empty() -> False" in out
    assert "id=1  title='Scan Nebula-7'" in out
    assert "id=2  title='Survey Kepler-442b'" in out


def test_running_the_module_tells_the_three_chapter_story(capsys):
    runpy.run_module("starship_log", run_name="__main__")
    out = capsys.readouterr().out
    chapters = [
        "Chapter 1: A brand new mission queue",
        "Chapter 2: The first mission is added",
        "Chapter 3: A second mission joins the line behind it",
    ]
    positions = [out.index(chapter) for chapter in chapters]
    assert positions == sorted(positions)
    assert out.count("is_empty() -> True") == 1
    assert out.count("is_empty() -> False") == 2
    assert "id=2  title='Survey Kepler-442b'" in out


def test_data_survives_a_separate_python_process(tmp_path):
    db_file = tmp_path / "starship.db"
    writer = (
        "import sys; from starship_log import MissionQueue; "
        "q = MissionQueue(sys.argv[1]); q.enqueue('Scan Nebula-7'); q.close()"
    )
    subprocess.run(
        [sys.executable, "-c", writer, str(db_file)],
        check=True,
        cwd=Path(__file__).parent,
    )
    assert db_file.exists()
    reopened = MissionQueue(db_file)
    assert not reopened.is_empty()
