import sqlite3
from main import Master
from main import master_list, list_divases
from random import randint
import datetime



class Intro(Master):
    def __init__(self, room = None, type_product = None, data_priem = None, data_done = None,
                 initials = None, status = "Ремонтируется"):

        super().__init__(room, type_product, data_priem, data_done, initials, status)
# Состояние статуса
    def get_status(self):
        intro.append(self.status)
        return self.status

# Генератор квитанций
    def set_room(self):
        # НОМЕР КВИТАНЦИИ
        self.room = randint(1000, 10000)
        intro.append(self.room)
        #print(f'Номер квитанции {self.room}')

# Выбор техники
    def set_type_product(self):
        # ТИП ТЕХНИКИ
        n1 = input(f'Выберите тип техники : {master_list}')
        if n1 == 'Телефон':
            self.mobile()
            intro.append(n1)

        elif n1 == 'Ноутбук':
            self.notebook()
            intro.append(n1)

        elif n1 == 'Телевизор':
            self.tv()
            intro.append(n1)
        else:
            print('Вы выбрали не из списка.')


    def set_data_priem(self):
        # ДАТА ПРИЕМА
        d = datetime.datetime.now()
        intro.append(d.strftime("%d/%m/%y"))
        self.data_priem = d.strftime("%d/%m/%y")

    def set_data_done(self):
        # ДАТА ГОТОВОСТИ
        self.data_done = datetime.datetime.now() + datetime.timedelta(days=randint(1, 5))
        d = self.data_done.strftime("%d/%m/%y")
        intro.append(d)

# ФИО
    def set_initials(self):
        n2 = input('Введите ФИО : ')
        intro.append(n2)

# Переопределение Списка в Кортеж для записи в БД
    def get_tuple2(self):
        tuple1 = tuple(intro)
        list_divases1 = tuple(list_divases)
        tuple2 = tuple1[:3] + list_divases1 + tuple1[3:]
        return tuple2

# Создание БД
    def sql_kvitancii(self, tuple2):
         try:
             conn = sqlite3.connect('kvitancii7.db')
             cur = conn.cursor()

             cur.execute("CREATE TABLE IF NOT EXISTS users"
                         "(room INTEGER PRIMARY KEY,"
                             "name TEXT, type_product TEXT, info_product TEXT, info_product2 TEXT, info_product3 TEXT,"
                             "info_product4 TEXT,"
                              " data_priem TEXT, data_done TEXT,"
                             "status TEXT)")
             if len(tuple2) == 10:
                 cur.execute("""INSERT INTO users (room, name, type_product, info_product,
                      info_product2, info_product3, info_product4, data_priem, data_done, status)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", tuple2)

             else:
                 cur.execute("""INSERT INTO users (room, name, type_product, info_product,
                                  info_product2, info_product3, info_product4, data_priem, data_done, status)
                                  VALUES (?, ?, ?, ?, ?, ?, NULL, ?, ?, ?)""",
                             tuple2)

             conn.commit()
             conn.close()
         except sqlite3.Error as error:
             print("Ошибка при работе с SQLite", error)

# Печать пользователя по квитанции
    def get_users_info(self, room):
         try:
             conn = sqlite3.connect('kvitancii7.db')
             cur = conn.cursor()

             sql_select = """SELECT * FROM users WHERE room = ?"""
             cur.execute(sql_select, (room,))
             rec = cur.fetchall()
             for row in rec:
                 print('Квитанция: ', row[0])
                 print('Имя: ', row[1])
                 print('Тип продукта: ', row[2])
                 print('Информация о продукте:', row[3], row[4], row[5], row[6], sep=', ')
                 print('Дата приема: ', row[7])
                 print('Дата готовности: ', row[8])
                 print('Статус: ', row[9])

             conn.commit()
             conn.close()
         except sqlite3.Error as error:
             print("Ошибка при работе с SQLite", error)

intro = []


d = Intro()
#
# d.set_room()
# d.set_initials()
# d.set_type_product()
# d.set_data_priem()
# d.set_data_done()
# d.get_status()

tuple1 = tuple(intro)
#print(tuple1)
list_divases1 = tuple(list_divases)
#print(list_divases1)
#print(intro)
tuple2 = tuple1[:3] + list_divases1 + tuple1[3:]
#print(tuple2)
#d.sql(tuple2)
#d.get_users_info(5802)


