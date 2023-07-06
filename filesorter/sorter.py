import shutil
import os
import json


class FileSorter:
    def __init__(self):
        self.config = {}
        try:
            with open('config.json', 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            with open('config.json', 'w') as f:
                pass

        print(self.config)

    def subStringSearch(self, s, t):
        if (len(s) < len(t)):
            return False
        for i in range(len(s) - len(t) + 1):
            if s[i:i + len(t)] == t:
                return True
        return False

    def sort_folder(self, sort_folder):
        print('Sorting folder ' + sort_folder)
        fileList = os.listdir(sort_folder)
        for folder in self.config:
            sort_type = self.config[folder][0]
            name_or_extension = self.config[folder][1]
            for file in fileList:
                extension = file.split('.')[-1]
                name = file.split('.')[0]
                name = name.lower()
                if sort_type == 'name':
                    if self.subStringSearch(name, name_or_extension):
                        shutil.move(sort_folder + "//" + file,
                                    folder + "//" + file)
                elif sort_type == 'extension':
                    if extension == name_or_extension:
                        shutil.move(sort_folder + "//" + file,
                                    folder + "//" + file)

    def add_folder(self, path, sort_by, name_or_extension):
        if sort_by not in ['name', 'extension']:
            print('Invalid sort_by argument')
            return
        self.config[path] = [sort_by, name_or_extension].lower()
        with open('config.json', 'w') as f:
            json.dump(self.config, f)

        print("Added folder " + path)

    def command_line(self):
        print('Welcome to FileSorter!')
        while True:
            command = input(">")
            command = command.split(' ')
            if command[0] == 'help':
                print(
                    "addfolder (path, sort by [name, extension], name or extension): add a folder to have files sorted to")
                print("sort (folder): sort all files in the folder")
                print("exit: exit the program")
            elif command[0] == 'addfolder':
                self.add_folder(command[1], command[2], command[3])
            elif command[0] == 'sort':
                self.sort_folder(command[1])
            elif command[0] == 'exit':
                break


if __name__ == "__main__":
    fs = FileSorter()
    fs.command_line()
