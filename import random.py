import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Generates a sorted list of unique random numbers for a lottery ticket.

    :param min: Minimum possible number (>= 1)
    :param max: Maximum possible number (<= 1000)
    :param quantity: Number of unique numbers to generate
    :return: Sorted list of unique random numbers or an empty list if parameters are invalid
    """
    # Validate parameters
    if not (1 <= min <= max <= 1000) or quantity > (max - min + 1) or quantity <= 0:
        return []

    # Generate unique random numbers
    numbers = random.sample(range(min, max + 1), quantity)
    
    # Sort and return
    return sorted(numbers)

