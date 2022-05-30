class Master:
    def __init__(self, room, type_product, data_priem, data_done, initials, status = 'Ремонтируется'):
        self.room = room
        self.type_product = type_product
        self.data_priem = data_priem
        self.data_done = data_done
        self.initials = initials
        self.status = status


# МЕТОДЫ ДЛЯ ЗАПОЛНЕНИЯ ИНФОРМАЦИИ
    def mobile(self):
        if self.type_product == 'Телефон':
            marka = input('Введите марку : ')
            list_divases.append(marka)
            sistema = input('Введите операционную систему: ')
            list_divases.append(sistema)
            polomka = input('Введите описание поломки: ')
            list_divases.append(polomka)


    def notebook(self):
        if self.type_product == 'Телефон':
            marka = input('Введите марку : ')
            list_divases.append(marka)
            sistema = input('Введите операционную систему: ')
            list_divases.append(sistema)
            year = input('Год выпуска : ')
            list_divases.append(year)
            polomka = input('Введите описание поломки: ')
            list_divases.append(polomka)


    def tv(self):
        if self.type_product == 'Телефон':
            marka = input('Введите марку : ')
            list_divases.append(marka)
            diagonal = input('Введите диагональ : ')
            list_divases.append(diagonal)
            polomka = input('Введите описание поломки : ')
            list_divases.append(polomka)


# список информации
list_divases = []
master_list = ["Телефон", "Ноутбук", "Телевизор"]

#m = Mobile()
#n = Notebook()
#t = Tv()
#n.info('Ноутбук')
#m.info('Телефон')
#t.info('Телевизор')