def film(f,date,time,k):
    if f==str("Паразиты"):
        if date==str("Сегодня"):
            if k<20:
                if time==12:
                    return 250*k
                elif time==16:
                    return 350*k
                elif time==20:
                    return 450*k
                else:
                    print("Такого времени нет")
            else:
                if time==12:
                    return 250*k*0.8
                elif time==16:
                    return 350*k*0.8
                elif time==20:
                    return 450*k*0.8
                else:
                    print("Такого времени нет")
        elif date==str("Завтра"):
            if k<20:
                    if time==12:
                            return 250*k*0.95
                    elif time==16:
                        return 350*k*0.95
                    elif time==20:
                        return 450*k*0.95
                    else:
                        print("Такого времени нет")
            else:
                if time==12:
                    return 250*k*0.8*0.95
                elif time==16:
                    return 350*k*0.8*0.95
                elif time==20:
                    return 450*k*0.8*0.95
                else:
                    print("Такого времени нет")
        else:
            print("На другие дни купить нельзя")
    elif f==str("1917"):
        if date==str("Сегодня"):
            if k<20:
                if time==10:
                    return 250*k
                elif time==13:
                    return 350*k
                elif time==16:
                    return 350*k
                else:
                    print("Такого времени нет")
            else:
                if time==10:
                    return 250*k*0.8
                elif time==13:
                    return 350*k*0.8
                elif time==16:
                    return 350*k*0.8
                else:
                    print("Такого времени нет")
        elif date==str("Завтра"):
            if k<20:
                    if time==10:
                            return 250*k*0.95
                    elif time==13:
                        return 350*k*0.95
                    elif time==16:
                        return 350*k*0.95
                    else:
                        print("Такого времени нет")
            else:
                if time==10:
                    return 250*k*0.8*0.95
                elif time==13:
                    return 350*k*0.8*0.95
                elif time==16:
                    return 350*k*0.8*0.95
                else:
                    print("Такого времени нет")
        else:
            print("На другие дни купить нельзя")
    elif f==str("Соник в кино"):
        if date==str("Сегодня"):
            if k<20:
                if time==10:
                    return 350*k
                elif time==14:
                    return 450*k
                elif time==18:
                    return 450*k
                else:
                    print("Такого времени нет")
            else:
                if time==10:
                    return 350*k*0.8
                elif time==14:
                    return 450*k*0.8
                elif time==18:
                    return 450*k*0.8
                else:
                    print("Такого времени нет")
        elif date==str("Завтра"):
            if k<20:
                    if time==10:
                            return 350*k*0.95
                    elif time==14:
                        return 450*k*0.95
                    elif time==18:
                        return 450*k*0.95
                    else:
                        print("Такого времени нет")
            else:
                if time==10:
                    return 350*k*0.8*0.95
                elif time==14:
                    return 450*k*0.8*0.95
                elif time==18:
                    return 450*k*0.8*0.95
                else:
                    print("Такого времени нет")
        else:
            print("На другие дни купить нельзя")
    else:
        print("Такого фильма нет")
