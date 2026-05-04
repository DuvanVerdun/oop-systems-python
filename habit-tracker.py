from datetime import date, timedelta


class Habit:
    """Class representing a habit with a name and a its streak of consecutive days."""
    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("Habit name cannot be empty.")
        self._name = name
        self._checked_days: set[date] = set()

    @property
    def name(self) -> str:
        """Returns the name of the habit."""
        return self._name

    def _count_streak(self) -> int:
        """Counts the current streak of consecutive checked days."""
        if not self._checked_days:
            return 0
        streak = 0
        current_day = date.today()
        while current_day in self._checked_days:
            streak += 1
            current_day -= timedelta(days=1)
        return streak

    def check(self) -> None:
        """Marks the habit as checked for today and updates the streak."""
        today = date.today()
        if today in self._checked_days:
            raise ValueError("Habit already checked for today.")
        self._checked_days.add(today)

    def get_streak(self) -> int:
        """Returns the current streak of the habit."""
        return self._count_streak()
