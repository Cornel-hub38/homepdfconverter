
from docx2pdf import convert
import tkinter as tk
import simpleGUISSelectfile as choiceMenu


root = tk.Tk()
# set teh title
root.title('word to pdf converter')
# set the window size
root.geometry('800x300+100+100')
root.resizable(True, True)



# Add widgets
title = tk.Label(
    root,
    text='As advertised',
    font=('Arial 16 bold'),
    bg='brown',
    fg='#FF0'
)


word2pdf_btn = tk.Button(root, text='word2pdf converter')
excel2pdf_btn = tk.Button(root, text='excel2pdf converter')
csv2pdf_btn = tk.Button(root, text='csv2pdf converter')
epub2pdf_btn = tk.Button(root, text='epub2pdf converter')
pdfback2word_btn = tk.Button(root, text='pdf2word converter')




"""
# convert a single file
convert("example.docx", "outputconverted_2.pdf")

# convert an entire folder
#convert("folder with docs")
        """



title.grid(columnspan=2)
word2pdf_btn.grid(row=1, column=1, sticky=(tk.W + tk.E))
excel2pdf_btn.grid(row=1, column=2, sticky=(tk.W + tk.E))
csv2pdf_btn.grid(row=1, column=3, sticky=(tk.W + tk.E))
epub2pdf_btn.grid(row=1, column=4, sticky=(tk.W + tk.E))
pdfback2word_btn.grid(row=1, column=5, sticky=(tk.W + tk.E))




def onpressDocx2pdf():
    message = (
        f"Convert word to pdf has been pressed"
    )
    print(message)
    choiceMenu.menu()
    return "Success"

def word2pdfConversion():





word2pdf_btn.configure(command=onpressDocx2pdf)


root.mainloop()