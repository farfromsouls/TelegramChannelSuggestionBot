def Announc(brend, name, overview, price):
    global textmess
    textmess = (f'Бренд: {brend} \n'
                 f'Название: {name} \n'
                 f'Описание: {overview} \n'
                 f'Цена: {price} \n')
    print(textmess)

def changes(brend, name, overview, price):
    inputMess = input("сасиска")
    if inputMess == "Бренд":
#тут короче строчка запроса по типу напишите бренд
        brend = 
    elif inputMess == "Название":
#тут короче строчка запроса по типу напишите бренд
        name = 
    elif inputMess == "Описание":
#тут короче строчка запроса по типу напишите бренд
        overview = 
    elif inputMess == "Цена":
#тут короче строчка запроса по типу напишите бренд
        price = 
    else:
        print("неправильный ввод")
        return
    Announc(brend, name, overview, price)









