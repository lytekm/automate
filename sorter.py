import shutil
import os
import json
import CLI
# "hello"try:tkinter p[elif:hiiii import tkinter as tk    ] - my gf


def substring_search(s, t):
    if len(s) < len(t):
        return False
    for i in range(len(s) - len(t) + 1):
        if s[i:i + len(t)] == t:
            return True
    return False


class FileSorter:
    def __init__(self):
        self.config = {}
        try:
            if os.path.getsize('config.json') != 0:
                with open('config.json', 'r') as f:
                    self.config = json.load(f)
        except FileNotFoundError:
            pass

    def sort_folder(self, sort_folder):
        print('Sorting folder ' + sort_folder)
        file_list = os.listdir(sort_folder)
        for folder in self.config["sorting"]:
            sort_type = self.config["sorting"][folder][0]
            name_or_extension = self.config["sorting"][folder][1]
            for file in file_list:
                extension = file.split('.')[-1]
                name = file.split('.')[0]
                name = name.lower()
                if sort_type == 'name':
                    if substring_search(name, name_or_extension):
                        shutil.move(sort_folder + "//" + file,
                                    folder + "//" + file)
                    else:
                        pass
                elif sort_type == 'extension':
                    if extension == name_or_extension:
                        shutil.move(sort_folder + "//" + file,
                                    folder + "//" + file)
                    else:
                        pass

    def add_folder(self, path, sort_by, name_or_extension):
        if sort_by not in ['name', 'extension']:
            print('Invalid sort_by argument')
            return
        self.config["sorting"][path] = [sort_by.lower(), name_or_extension.lower()]
        with open('config.json', 'w') as f:
            json.dump(self.config, f)

        print("Added folder " + path)

    def show_config(self):
        print(self.config)

    def command_line(self):
        print('Welcome to FileSorter!')
        while True:
            command = input(">")
            command = command.split(' ')
            if command[0] == 'help':
                print(
                    "addfolder (path, sort by [name, extension], "
                    "name or extension): add a folder to have files sorted to")
                print("sort (folder): sort all files in the folder")
                print("show: show your configuration for the program")
                print("exit: exit the program")
            elif command[0] == 'addfolder':
                if len(command) != 4:
                    print("Invalid number of arguments")
                    continue
                self.add_folder(command[1], command[2], command[3])
            elif command[0] == 'sort':
                if len(command) != 2:
                    print("Invalid number of arguments")
                    continue
                self.sort_folder(command[1])
            elif command[0] == 'show':
                self.show_config()
            elif command[0] == 'exit':
                with open('config.json', 'w') as f:
                    json.dump(self.config, f)
                    CLI.CLI().command_line()
                break
            else:
                print("Invalid command")
