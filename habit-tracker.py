from datetime import date, timedelta


class Habit:
    """Class representing a habit with a name and a its streak of consecutive days."""
    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("Habit name cannot be empty.")

        self._name = name
        self._streak = 0
        self._checked_days: list[date] = []

    @property
    def name(self) -> str:
        """Returns the name of the habit."""
        return self._name

    def _is_consecutive(self, last_date: date, current_date: date) -> bool:
        """Checks if the current date is consecutive to the last date."""
        return current_date == last_date + timedelta(days=1)

    def check(self) -> None:
        """Marks the habit as checked for today and updates the streak."""
        today = date.today()
        if today in self._checked_days:
            raise ValueError("Habit already checked for today.")
        self._checked_days.append(today)

    def show_streak(self) -> int:
        """Returns the current streak of the habit."""
        if not self._checked_days:
            return 0
        last_date = date.today() - timedelta(days=1)
        for current_date in self._checked_days:
            is_consecutive = self._is_consecutive(last_date, current_date)
            if is_consecutive:
                self._streak += 1
            else:
                self._streak = 0
        return self._streak
