import sqlite3


class MissionQueue:
    # Design decision: SQLite (in memory) is our choice, not something the
    # tests demand yet. A plain list would also pass the current tests.
    def __init__(self):
        self._connection = sqlite3.connect(":memory:")
        self._connection.execute(
            "CREATE TABLE missions ("
            "id INTEGER PRIMARY KEY, "
            "title TEXT NOT NULL)"
        )

    def enqueue(self, title):
        self._connection.execute(
            "INSERT INTO missions (title) VALUES (?)", (title,)
        )

    def is_empty(self):
        row = self._connection.execute(
            "SELECT COUNT(*) FROM missions"
        ).fetchone()
        return row[0] == 0


def show_table(queue):
    # Demo only: peeks at the private connection so we can see the database.
    rows = queue._connection.execute("SELECT id, title FROM missions").fetchall()
    print(f"  is_empty() -> {queue.is_empty()}")
    if not rows:
        print("  missions table: (no rows)")
    for mission_id, title in rows:
        print(f"  missions table: id={mission_id}  title={title!r}")


if __name__ == "__main__":
    print("Chapter 1: A brand new mission queue")
    queue = MissionQueue()
    show_table(queue)

    print("\nChapter 2: The first mission is added")
    queue.enqueue("Scan Nebula-7")
    show_table(queue)

    print("\nChapter 3: A second mission joins the line behind it")
    queue.enqueue("Survey Kepler-442b")
    show_table(queue)
