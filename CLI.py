import macro
import sorter
import json
import os


class CLI:
    def __init__(self):
        self.sorter = sorter.FileSorter()
        self.macro = macro.Macro()
        self.config = {
            "macros": {},
            "sorting": {}
        }
        try:
            if os.path.getsize('config.json') != 0:
                with open('config.json', 'r') as f:
                    self.config = json.load(f)
        except FileNotFoundError:
            with open('config.json', 'w') as f:
                json.dump(self.config, f)

    def keyboard_callback(self, event, keybind):
        name = event.name
        self.config[keybind].append(name) 

    def command_line(self):
        while True:
            print("Welcome to Automation Tools!")
            print("Services: ")
            print("1. File Sorter")
            print("2. Macro")
            print("3. Create Keyboard Shortcut")
            print("4. Exit")
            command = input("> ")
            if command == "1":
                self.sorter.command_line()
            elif command == "2":
                self.macro.command_line()
            elif command == "3":
                pass
            elif command == "4":
                exit()


if __name__ == "__main__":
    CLI().command_line()
    input("Press enter to exit...")
