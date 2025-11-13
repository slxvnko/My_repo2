import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalizes a phone number to the standard international format for Ukraine.

    :param phone_number: String representing a phone number in any format
    :return: Normalized phone number as a string (digits only, starts with '+')
    """
    # Remove all characters except digits and '+'
    cleaned = re.sub(r"[^\d+]", "", phone_number.strip())

    # If the number starts with '+', ensure it’s in correct format
    if cleaned.startswith("+"):
        return cleaned
    
    # If it starts with '380' (Ukraine code but without '+')
    if cleaned.startswith("380"):
        return "+" + cleaned
    
    # Otherwise, assume it’s a local number and add '+38' prefix
    return "+38" + cleaned
