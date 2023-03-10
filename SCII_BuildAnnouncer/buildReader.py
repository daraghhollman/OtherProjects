import pyttsx3
import time
import numpy as np
from pynput import keyboard

voiceEngine = pyttsx3.init()
voiceEngine.setProperty("rate", 180)
voiceEngine.setProperty("voice", "english")

buildPath = "tripleOracleAttack.txt"
scaleFactor = 1 # seconds in starcraft 2 are 1.4 seconds faster, this isnt true anymore?

def ReadBuild(file):

    startTime = time.time()

    data = np.genfromtxt(file, dtype=str, delimiter="-")

    for line in data[1:]:
        line[0] = int(line[0]) / scaleFactor

    i = 1
    for line in data[1:]: # ignores first line containing titles

        Speak(line[1])

        if line[0] == data[-1][0]:
            break

        currentTime = time.time() - startTime

        targetTime = float(data[i+1][0])

        waiting = True
        while waiting:
            currentTime = time.time() - startTime
            if currentTime >= targetTime:
                waiting = False
            else: time.sleep(0.1)

        i += 1


def Speak(sentance):
    voiceEngine.say(sentance)
    voiceEngine.runAndWait()

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.home:
        # Stop listener
        return False

def main():

    print("Welcome to buildreader, a python script for sc2 to read instructions at specified time intervals.")

    print("Current selected build: " + str(buildPath))

    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
            listener.join()

    ReadBuild(buildPath)
    

if __name__ == "__main__":
    main()