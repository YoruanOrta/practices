import time

# Creating a heart shape with a name inside it

class Color:
    RED = '\x1b[0;31;50m'
    BOLD_RED = '\x1b[1;31;50m'
    NORMAL = '\x1b[0m'

def charge_heart():
    with open('heart.txt', 'r') as f:
        return f.read()

def romanticize(name):
    heart = charge_heart()
    letter = list(name)
    i = 0
    while '@' in heart:
        heart = heart.replace('@', letter[i % len(letter)], 1)
        i += 1
    return heart

def main():
    name = input("Enter your name: ").strip() or "Love"
    heart = romanticize(name)

    print(f"\n{Color.BOLD_RED} Making a heart... {Color.NORMAL}\n")

    for line in heart.split('\n'):
        if line.strip():
            print(f"{Color.RED}{line}{Color.NORMAL}")
            time.sleep(0.3)

    print(f"\n{Color.BOLD_RED} Love U {name}! {Color.NORMAL}\n")

if __name__ == "__main__":
    main()
# This script creates a heart shape with a name inside it.
