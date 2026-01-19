import os
import requests
from dotenv import load_dotenv

load_dotenv()
SESSION = os.getenv("AOC_SESSION")

def download_input(year: int, day: int):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {"Cookie": f"session={SESSION}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    day_folder = f"{year}/day{day:02d}"
    os.makedirs(day_folder, exist_ok=True)
    with open(f"{day_folder}/input.txt", "w") as f:
        f.write(response.text.strip())

    print(f"Input downloaded to {day_folder}/input.txt")

print("Session loaded:", SESSION[:10], "..." if SESSION else "❌ None")

if __name__ == "__main__":
    import sys
    y, d = map(int, sys.argv[1:3])
    download_input(y, d)

    