from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator

root = Tk()
root.title('Google Translator')
root.geometry('1000x400')
root.resizable(False, False)
root.configure(bg='white')

def lang_selector():
    lbl1 = primary_lang_combo.get()
    lbl2 = secondary_lang_combo.get()
    primary_lang_combo_label.configure(text=lbl1)
    secondary_lang_combo.configure(text=lbl2)
    root.after(1000, lang_selector)


def translate_text():
    input_text = primary_text.get(1.0, END)
    output_text = Translator()
    translated_text = output_text.translate(input_text,src = primary_lang_combo.get(), dest=secondary_lang_combo.get())
    translated_text = translated_text.text

    secondary_text.delete(1.0, END)
    secondary_text.insert(END, translated_text)
#icon
window_icon = PhotoImage(file='icon.png')
root.iconphoto(False, window_icon)

#switch
switch_image =PhotoImage(file='switch.png')
switch_label = Label(root, image = switch_image, bg='white')
switch_label.place(x=440, y=100)

#language
lang = googletrans.LANGUAGES
lang_list = list(lang.values())
lang2 = lang.keys()

#primary language combo box
primary_lang_combo = ttk.Combobox(root, values = lang_list, font='Calibri 14', state='r')
primary_lang_combo.place(x=20, y=20)
primary_lang_combo.set('ENGLISH')

#primary language combo label
primary_lang_combo_label = Label(root, text='English', font='Calibri 20 bold', bg='white', width=8, bd=5, relief=FLAT)
primary_lang_combo_label.place(x=5, y=50)

#secondary language combo box
secondary_lang_combo = ttk.Combobox(root, values = lang_list, font='Calibri 14', state='r')
secondary_lang_combo.place(x=640, y=20)
secondary_lang_combo.set('Select Language')

#secondary language combo label
secondary_lang_combo_label = Label(root, text='SELECT LANGUAGE', font='Calibri 20 bold', bg='white', width=18, bd=5, relief=FLAT)
secondary_lang_combo_label.place(x=610, y=50)

#primary language frame
primary_lang_frame = Frame(root, bg='black', bd=3)
primary_lang_frame.place(x=20, y=115, width=360, height=207)

#primary text body
primary_text = Text(primary_lang_frame, font='Calibri 16', bg='white', bd=2,relief=FLAT, wrap=WORD)
primary_text.place(x=2, y=0, width=350, height=200)

#primary scroll bar
primary_scroll = Scrollbar(primary_text, cursor='hand2')
primary_scroll.pack(side='right', fill='y')

primary_scroll.config(command=primary_text.yview)
primary_text.config(yscrollcommand=primary_scroll.set)

#secondary language frame
secondary_lang_frame = Frame(root, bg='black', bd=3)
secondary_lang_frame.place(x=620, y=115, width=350, height=207)

#secondary text body
secondary_text = Text(secondary_lang_frame, font='Calibri 16', bg='white', bd=2,relief=FLAT, wrap=WORD)
secondary_text.place(x=600, y=0, width=350, height=200)

#secondary scroll bar
secondary_scroll = Scrollbar(secondary_text, cursor='hand2')
secondary_scroll.pack(side='right', fill='y')

secondary_scroll.config(command=secondary_text.yview)
secondary_text.config(yscrollcommand=secondary_scroll.set)

#translate button
translate = Button(root, text='Translate', font=('Calibri', 14), activebackground='white', cursor='hand2', bd=1, width=10, height=2, bg='black', fg='white', command=translate_text)
translate.place(x=450, y=250)

lang_selector()

root.mainloop()
