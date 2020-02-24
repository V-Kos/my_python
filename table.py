value = input("Введите N элемента: ")
if value:
    N= float(value)
    if N == 3:
        print("Литий(Li)")
    elif N==25:
        print("Марганец(Mn)")
    elif N==80:
        print("Ртуть(Hg)")
    elif N==17:
        print("Хлор(Cl)")
    else:
        print("Элемент не обнаружен =(")
