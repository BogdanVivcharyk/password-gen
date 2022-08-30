from tkinter import *
import string
from random import choice

#Пароль нельзя скопировать в буфер, это еще одна степень защиты)

window = Tk()

def passgen():
    password = ''
    pas = string.ascii_lowercase
    pas += string.ascii_uppercase
    if nums.get():
        pas += string.digits
    if sig.get():
        pas += string.punctuation
    for i in range(length.get()):
        password += choice(pas)
    generated.config(text=f'Ваш сгенерированный пароль: \n{password}')


nums = IntVar()
nums.set(0)
sig = IntVar()
sig.set(0)

window.title('Password Generator')
window.geometry('500x200')
window.resizable(width=True, height=False)

C = CENTER
frame = Frame(window)
frame.place(relheight=1, relwidth=1)
numbers = Checkbutton(frame, text='Добавить цифры', variable=nums, onvalue=1, offvalue=0)
signs = Checkbutton(frame, text='Добавить спецсимволы', variable=sig, onvalue=1, offvalue=0)
length = Scale(frame, from_=6, to=100, length=200, orient=HORIZONTAL)
generate = Button(frame, text='Сгенерировать пароль', command=passgen)
generated = Label(frame, text=f'Ваш сгенерированный пароль: \n')

numbers.pack(anchor=C)
signs.pack(anchor=C)
length.pack(anchor=C)
generate.pack(anchor=C)
generated.pack(anchor=C, pady=10)

window.mainloop()