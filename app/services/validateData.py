from datetime import datetime


def validateData(date_str: str) -> datetime:
    """Validates and converts a date string to a datetime object."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Expected YYYY-MM-DD.")