import sys
from time import sleep
import time 

def print_colored_text(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m", end='')

def print_lyrics():
    lines = [
        ("Mama, we're all gonna die", 0.1),
        ("Stop asking me questions, i'd hate to see you cry", 0.1),
        ("Mama, we're all gonna die", 0.1),
        ("'And when we go don't blame us-, yeah! We'll let the fire just bathe us-, yeah! ", 0.1),
        ("is leaving you", 0.14)
    ]

    delays = [1.4, 1.5, 0.1,1.4, 6]
    colors = [97, 97, 97, 97, 91]

    for i, ((line, char_delay), color) in enumerate(zip(lines, colors)):
        for char in line:
            print_colored_text(char, color)
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()