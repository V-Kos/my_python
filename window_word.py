import tkinter
import random
d ={'bag':'сумка','ball':'мяч','sun':'солнце','apple':'яблоко','error':'ошибка','up':'вверх','last':'последний','book':'книга','moon':'луна','milk':'молоко','three':'три','queen':'королева'}
d[random.choice(list(d.keys()))]
l1=list(d.keys())
l2=list(d.values())
rtext=l1[random.choice(range(len(l1)))]

def click():
    if entry.get()==d[rtext]:
        label.config(text='Угадали')
    else:
        label.config(text='Учи!(Ну или я плохо прописал программу)')


window = tkinter.Tk()

window.title('Угадайка')

frame = tkinter.Frame(window)
frame.pack()

label = tkinter.Label(frame,text="Переведите на русский язык(желательно с маленькой буквы)")
label.pack()

entry = tkinter.Entry(frame)
entry.pack()

label1 = tkinter.Label(frame,text=rtext)
label1.pack()

button = tkinter.Button(frame, text='Ввод', command=click,bg='red',fg='white') 
button.pack()
Button1=tkinter.Button(frame, text="Quit", command=window.destroy,bg='blue',fg='white').pack()
window.mainloop()