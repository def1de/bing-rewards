import random
import pyperclip
import keyboard
import json
import time

isOn = False
count = 0 

def select_random_word_txt():
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
        random_word = random.choice(words)
        return random_word

def select_random_word_json():
    with open("words.json", "r") as file:
        words = json.load(file)
        random_word = random.choice(words)
        return random_word

def copy_random_word():
    random_word = select_random_word_json()
    pyperclip.copy(random_word)
    keyboard.press_and_release("ctrl+a")
    keyboard.press_and_release("ctrl+v")
    keyboard.press_and_release("enter")

def switch():
    global isOn
    isOn = not isOn
    if isOn:
        print("Auto copy is on")
    else:
        print("Auto copy is off")

def auto_copy():
    keyboard.press_and_release("ctrl+w")
    keyboard.press_and_release("ctrl+t")
    time.sleep(1)
    copy_random_word()

if __name__ == "__main__":
    number_of_times = int(input("Enter the number of times to run: "))
    keyboard.add_hotkey("ctrl+b", switch)
    print("Hotkeys initialized\nPress 'ctrl+b' to start/stop auto-copying a random word to your clipboard.")
    while True:
        while isOn and count < number_of_times:
            auto_copy()
            time.sleep(6)
            count += 1
        if count >= number_of_times:
            print("Completed")
            break
    input("Press Enter to exit...")

