import sys
from pathlib import Path
import re
from collections import Counter

def parse_log_line(line: str) -> dict:
    pattern = r"(?P<date>\S+)\s(?P<time>\S+)\s(?P<level>\S+)\s(?P<message>\S+)"
    match = re.search(pattern, line)
    return {
        "date": match.group("date"),
        "time": match.group("time"),
        "level": match.group("level"),
        "message": match.group("message")
    }

def load_logs(file_path: str) -> list:
     with open(file_path, "r") as f:
        return [parse_log_line(line.strip()) for line in f]

def filter_logs_by_level(logs: list, level: str, key = "level") -> list:
    return [log for log in logs if log[key] == level]

def count_logs_by_level(logs: list, key = "level") -> dict:
    return Counter([item[key] for item in logs])



def main():

    args = sys.argv

    if len(args) < 2:
        return print("file name required")
   
    path = Path(__file__).parent.resolve() / args[1]
    level = None

    if not path.exists():
        return print("file not found")
    
    if len(args) > 2:
        level = args[2].upper()
    

    logs = load_logs(path)

    levels_count = count_logs_by_level(logs)

    # Заголовок
    print(f"\n{'Рівень логування':<16} | {'Кількість'}")
    print("-" * 17 + "|" + "-" * 10)
    # Дані
    for level_type, count in levels_count.items():
        print(f"{level_type:<16} | {count}")

    if level:
        print(f"\nДеталі логів для рівня '{level}':")
        specific_level_logs = filter_logs_by_level(logs, level)
        for log in specific_level_logs:
            date, time, level, message = log.values()
            print(f"{date} {time} {level} {message}")

if __name__ == "__main__":
    main()
