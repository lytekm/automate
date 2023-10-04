import pyautogui as pag
from pynput import mouse, keyboard as kb
from functools import partial
import keyboard
import json
import os
import time


class Macro:
    def __init__(self):
        self.config = {}
        self.macro_name = ""
        try:
            if os.path.getsize('config.json') != 0:
                with open('config.json', 'r') as f:
                    self.config = json.load(f)
        except FileNotFoundError:
            pass

    def terminate_recording(self, mouse_listener, keyboard_listener):
        mouse_listener.stop()
        keyboard_listener.stop()
        with open("config.json", 'w') as f:
            json.dump(self.config, f)

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.config["macros"][self.macro_name].append([x, y])
            print([x, y])

    def on_press(self, key):
        if key == kb.Key.esc:
            return False
        try:
            self.config["macros"][self.macro_name].append(key.char)
            print(key.char)
        except AttributeError:
            self.config["macros"][self.macro_name].append(key.name)
            print(key.name)

    def on_esc(self, key):
        if key == kb.Key.esc:
            return False

    def command_line(self):
        print("Welcome to Macros!")
        while True:
            command = input("> ")
            command = command.lower()
            command = command.split(' ')
            if command[0] == 'record':
                self.record_macro()

            elif command[0] == 'run':
                self.run_macro(command[1])
                
            elif command[0] == 'exit':
                with open("config.json", 'w') as f:
                    json.dump(self.config, f)
                break
            else:
                print("Invalid command")

    def record_macro(self):
        name = input("Enter the name of the macro: ")
        self.config["macros"][name] = []
        self.macro_name = name
        print("Recording macro: click the screen to record a click, "
              "press any key to record keystrokes, press ESC to stop recording")

        mouse_listener = mouse.Listener(on_click=self.on_click)
        mouse_listener.start()
        keyboard_listener = kb.Listener(on_press=self.on_press)
        keyboard_listener.start()

        with kb.Listener(on_press=self.on_esc) as listener:
            listener.join()

        self.terminate_recording(mouse_listener, keyboard_listener)

    def run_macro(self, macro_name):
        if macro_name in self.config["macros"]:
            for action in self.config["macros"][macro_name]:
                if type(action) == list:
                    print(action[0], action[1])
                    # move to mouse position and then click
                    pag.moveTo(action[0], action[1])
                    pag.click()
                    time.sleep(1)

                else:
                    pag.keyDown(action)
        else:
            print("Macro not found")
