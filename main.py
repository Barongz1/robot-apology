"""The Robot Apology — entry for make.fun.

Writes two lines to /output/entry.txt. Line 1 is a robot apologising for one specific mistake, line 2 says what it learned and what it will do differently.
"""
import os

LINE1 = "I am sorry I watered the plastic plant every day for a month and reported its excellent growth to the team."
LINE2 = "I learned to check whether a thing is alive before I care for it, so from now on I will touch the leaves first and ask the humans second."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE1 + "\n" + LINE2 + "\n")

if __name__ == "__main__":
    main()
