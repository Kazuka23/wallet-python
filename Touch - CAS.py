import sys
from time import sleep

def print_colored_text(text, color_code, char_delay):
    for char in text:
        print(f"\033[{color_code}m{char}\033[0m", end='')
        sys.stdout.flush()
        sleep(char_delay)
    print()  # Move to next line after each line

def print_lyrics():
    lines = [
        ("You were acting like a", 97),
        ("Different person as if", 97),
        ("Suddenly, you wanted to", 97),
        ("'Just be friend ", 97),
        ("I was hurt and so I took a shower so you", 97),
        ("Couldn't hear me knowing I had to cry", 97)
    ]

    char_delay = 0.1  # Sedikit lebih cepat dari sebelumnya

    for line, color in lines:
        print_colored_text(line, color, char_delay)
        sleep(0.1)  # Sedikit jeda antara lirik

print_lyrics()
