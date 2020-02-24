def call_tel(code,d):
    if code==343:
        return d*15
    elif code==381:
        return d*18
    elif code==473:
        return d*13
    elif code==485:
        return d*11
    else:
        print("Нет данных")
