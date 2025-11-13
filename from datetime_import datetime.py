from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Calculates the number of days between the given date and today's date.

    :param date: A string representing a date in the format 'YYYY-MM-DD' (e.g., '2020-10-09')
    :return: An integer representing the number of days between the given date and today.
             If the given date is in the future, the result will be negative.
    """
    try:
        # Convert the string into a date object
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        
        # Get today's date
        today = datetime.today().date()
        
        # Calculate the difference in days
        delta = today - target_date
        
        return delta.days
    
    except ValueError:
        # Handle incorrect date format
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
    



