def is_palindrome(text):
    """
    Checks if a given string text is a palindrome.
    """
    s = str(text).lower()
    return s == s[::-1]

# Example usage
print(is_palindrome("mam"))
