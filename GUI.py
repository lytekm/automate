import PySimpleGUI as gui
import sorter
import macro
import os
import json


class GUI:
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

    def main_page(self):

        # ------------------------------------- LAYOUTS --------------------------------------
        home_layout = [[gui.Text("Main Menu")], [gui.Button("Sorter"), gui.Button("Macro")]]

        add_folder_layout = [[gui.Input("Folder Path", key="folder-path")], [gui.Radio("Name", group_id="sorter-radios", key="file-name"),
                                                          gui.Radio("Extension", group_id="sorter-radios", key='file-ext'), gui.Input("Name or extension", key="criteria")],
                                                            [gui.Button("Add")]]
        sort_folder_layout = [[gui.Input("Folder to be sorted", key="folder"), gui.Button("Sort")]]
        sorter_layout = [[gui.Text("Sorter")], [gui.Button("Add folder"), gui.Button("Sort Folder")], [gui.Column(add_folder_layout, visible=False, key="add_folder_layout"),
                                                                                                       gui.Column(sort_folder_layout, visible=False, key="sort_folder_layout")]]

        macro_layout = [[gui.Text("Macro")], [gui.Button("Record macro")], [gui.Text("Macros")]]

        layout = [[gui.Column(home_layout, key="home_layout"), gui.Column(sorter_layout, visible=False,
                                                                          key="sorter_layout"), gui.Column(macro_layout, visible=False, key="macro_layout")]]
        # window
        window = gui.Window(title="Window", layout=layout, margins=(300, 300))
        # Create an event loop
        while True:
            event, values = window.read()
            # Sorter events
            if event == "Sorter":
                window["home_layout"].update(visible=False)
                window["sorter_layout"].update(visible=True)
            elif event == "Add folder":
                window["add_folder_layout"].update(visible=True)
            elif event == "Add":
                if values["file-name"]:
                    sortby = "name"
                else:
                    sortby = "extension"
                self.sorter.add_folder(values["folder-path"], sortby, values["criteria"])
            elif event == "Sort Folder":
                window["sort_folder_layout"].update(visible=True)
            elif event == "Sort":
                self.sorter.sort_folder(values["folder"])

            # Macro events
            elif event == "Macro":
                window["home_layout"].update(visible=False)
                window["macro_layout"].update(visible=True)
            elif event == gui.WIN_CLOSED:
                break

        window.close()


if __name__ == "__main__":
    GUI().main_page()

