from re import search, IGNORECASE


search_pattern = r"(?P<command>[^\s]+)\s?(?P<name>[\w]+)?\s?(?P<phone>[\+0-9]+)?"

def parse_input(input: str):
    parsed = search(search_pattern, input, flags=IGNORECASE)
    return parsed

