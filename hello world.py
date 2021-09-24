import sys, time, os, string, random
def typewriter(message, speed = 0.1, pause = 1):
    '''
    Info: this function types out string a
    :param message: takes a string
    :return: types out the string
    '''
    for char in message:
        sys.stdout.write(f'\u001b[92m{char}')
        sys.stdout.flush
        if char !="\n":
            time.sleep(speed)
        else:
            time.sleep(pause)
typewriter("HELLO, WORLD!")