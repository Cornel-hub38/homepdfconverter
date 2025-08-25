import PySimpleGUI4 as sg

def menu():
 #   select_compress = sg.Text("Select files to compress")
    select_source_folder = sg.FileBrowse("Select source file")
    chooseButton2 = sg.FolderBrowse("Select destintion of converted document")
    Convert_button = sg.Button("Word2pdf conversion")

    window = sg.Window('Word2pdf converter', layout=[[select_source_folder],
                                                 [chooseButton2],
                                                 [Convert_button]])
    window.read()
    window.close()






if __name__ == "__main__":
    print("well done")