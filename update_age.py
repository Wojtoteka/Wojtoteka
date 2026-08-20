import re
from datetime import date

BIRTH_YEAR = 2011
BIRTH_MONTH = 9
BIRTH_DAY = 5

def compute_age():
    today = date.today()
    age = today.year - BIRTH_YEAR
    if (today.month, today.day) < (BIRTH_MONTH, BIRTH_DAY):
        age -= 1
    return age

def main():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    age = compute_age()
    new_content = re.sub(
        r"<!--AGE_START-->.*?<!--AGE_END-->",
        f"<!--AGE_START-->{age}<!--AGE_END-->",
        content,
        flags=re.S,
    )

    if new_content != content:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"README updated: age is now {age}")
    else:
        print("No update needed.")

if __name__ == "__main__":
    main()
