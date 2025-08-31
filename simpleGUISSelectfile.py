from typing import final

import PySimpleGUI4 as sg
from pathlib import Path
from docx2pdf import convert


class GetInput:

    def __init__(self):
        self.chosen_file = None
        self.directory = None

    def menu(self):
        select_source_folder = sg.FileBrowse("1.  Select source file",
                                             button_color=('#0f2', 'firebrick3'), key="source_file")
        #choosen_folder = sg.FolderBrowse("destination of PDF", key="dest_folder")
        Convert_button = sg.Button("2.  Word2pdf conversion", button_color=('white', 'firebrick3'),
                                   key='Word2pdf_converter')
        layout = [[select_source_folder], [Convert_button]]


        window = sg.Window('Word2pdf converter', layout)
        event, values = window.read()
        window.close()

        if event == "Word2pdf_converter" and values["source_file"]:
            self.directory = values["source_file"]
            self.chosen_file = Path(self.directory).stem
            print(f"Chosen file: {self.directory}")
            print(f"File name without extension: {self.chosen_file}")


            print("Looks like progress mate")
##############################################################################


        else:
            print("No file selected")




    def doWord2fdfConversion(self):
        if not self.directory:
            print("No file was chosen for word to pdf conversion")
            return

        word_file = self.directory
        pdf_file = str(Path(self.directory).with_suffix(".pdf"))

        print("Converting .......")
        print("Word file: ", word_file)
        print("PDF output", pdf_file)
        convert(word_file, pdf_file)  # Actual file conversion

        print("Conversion done")




if __name__ == "__main__":
    print("Starting program\n")
    app = GetInput()
    app.menu()
    app.doWord2fdfConversion()
    print("done as done can be nate")
