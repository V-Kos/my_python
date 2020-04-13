import tkinter
import json
s=[]
def click():
    s.append({ "Задача:":entry_zadaji.get(),"Категория:":entry_categ.get(),"Время":entry_time.get()})
    s1=json.dumps(s)
    with open("Spisok_zadaj.json", "w") as file:
        file.write(s1)

def click2():
    print(s)

window = tkinter.Tk()
window.title('Задачник')
frame1 = tkinter.Frame(window)
frame1.pack()
frame2 = tkinter.Frame(window)
frame2.pack()
label = tkinter.Label(frame1,text="Менеджер задач")
label.pack()

zadaji = tkinter.Label(frame2,text='Задача')
zadaji.pack()
entry_zadaji = tkinter.Entry(frame2)
entry_zadaji.pack()

categ = tkinter.Label(frame2,text='Категории')
categ.pack()
entry_categ = tkinter.Entry(frame2)
entry_categ.pack()

time = tkinter.Label(frame2,text='Время',)
time.pack()
entry_time = tkinter.Entry(frame2)
entry_time.pack()

button1=tkinter.Button(frame2,text='Ввод',command=click,bg='white',fg='black')
button1.pack()
button2=tkinter.Button(frame2,text='Список задач',command=click2,bg='blue',fg='black')
button2.pack()
button3=tkinter.Button(frame2,text='Выход',command=window.destroy,bg='red',fg='black')
button3.pack()
window.mainloop()
