from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    """
    Returns a list of users who have birthdays in the next 7 days (including today).
    If a birthday falls on a weekend, it is moved to the following Monday.

    :param users: List of dictionaries with keys 'name' and 'birthday' (format 'YYYY.MM.DD')
    :return: List of dictionaries with 'name' and 'congratulation_date'
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Convert string to date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        # If this year's birthday has passed, consider next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Calculate the difference in days
        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year

            # Move to Monday if birthday falls on weekend
            if congratulation_date.weekday() == 5:      # Saturday
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:    # Sunday
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays