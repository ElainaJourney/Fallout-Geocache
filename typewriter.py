#! /usr/bin/env python3

import sys, time, os, string, random
from tabulate import tabulate
from blessed import Terminal
os.system('clear')
username = ""
password = ""
term = Terminal()
def typewriter(message, speed = 0.1, pause = 1):
    for char in message:
        sys.stdout.write(f'\u001b[92m{char}')
        sys.stdout.flush
        if char !="\n":
            time.sleep(speed)
        else:
            time.sleep(pause)
def dif_select():
    pass
def check_password(attempts = 0):
    typewriter(f"\nPlease enter your password: ")
    password = input()
    typewriter("\nPlease confirm your password: ")
    pass_check = input()
    if attempts >= 2:
        typewriter("Haxor!")
        return
    if pass_check != password:
        typewriter("Please try again\n...\n")
        check_password(attempts+1)
    else:
        pass_censor = '*' * len(password)
        print(f'Thank you for logging in, {username}.  Your password, {pass_censor}, is {len(password)} characters long.')

class Password:
    def __init__(self, difficulty = 4):
        pass

class FillerWord:
    pass
class Junk:
    pass
class MemoryChunk:
    def __init__(self, word = False):
        self.string = ""
        if word:
            self.location = random.randint(4095, 65500)
            self.string = word
        else:
            self.location = str(random.randint(4096, 65500))
            for x in range(15):
                self.string += random.choice(symbols)


def term_startup():
    term.fullscreen()
    typewriter("SECURITY RESET...\n\nWELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\n\n>SET TERMINAL/INQUIRE\n\nRIT-V300\n\n")
    time.sleep(2)
    print(term.clear())

def term_lock():
    term.clear()
    print("TERMINAL LOCKED \n\n PLEASE CONTACT ADMINISTRATOR")
symbols = string.punctuation
test_dump = []
for x in range(15):
    y = MemoryChunk()
    z = MemoryChunk()
    test_dump.append([y.location, y.string, z.location, z.string])
term_startup()
username = input('\nUSERNAME: ')
typewriter(f"Hello {username}\n")
typewriter(tabulate(test_dump), 0.01, 0.05)

check_password()
typewriter("Have a nice day!\n.\n.\n...\n You're still here?\n There's nothing left...\nThat's the app.\n\n\n\n\n\n\n\n\n\n\n If you aren't going to shut it down.....\nI guess I wi")
print("\n-------------------------------")
