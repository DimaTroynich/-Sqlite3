import sqlite3
from Level_2 import Repair_Intro



class Admin(Repair_Intro):
    def __init__(self, room = None, type_product = None, data_priem = None, data_done = None,
                 initials = None, status = "Ремонтируется"):
        super().__init__(room, type_product, data_priem, data_done, initials, status)

# Выбор действий
    def choise_admin(self):
        a = input(f'Выберите действия: {vibor_deystviy2}')
        if a == 'Сдать в ремонт':
            print('--------------------')
            self.get_choice_repair()
            print('--------------------')
        if a == "Посмотреть информацию":
            print('--------------------')
            self.get_info_room()
            print('--------------------')
        if a == "Зайти в админ-панель":
            print('--------------------')
            self.admin_add()
            self.adminka_choice()


# Админ кабинет
    def adminka_choice(self):
        while True:
            print('Выберите действия')
            a = input('\n'.join(vibor_deystviy3))
            if a == 'Отобразить список всех админов':
                print('----------------------------')
                self.get_all_admin()
                print('----------------------------')
                print('Выберите действия')
                a = input('\n'.join(vibor_deystviy3))
            if a == "Удалить админа из списка":
                print('----------------------------')
                self.get_dell_admin()
                print('----------------------------')
                print('Выберите действия')
                a = input('\n'.join(vibor_deystviy3))
            if a == "Добавить админа":
                print('----------------------------')
                self.get_upgred_admin()
                print('----------------------------')
                print('Выберите действия')
                a = input('\n'.join(vibor_deystviy3))
            if a == "Информация о квитанции":
                print('--------------------')
                a = input('Введите квитанцию: ')
                self.get_users_info(a)
                print('--------------------')
                break


# Создание метода для дальшейго использования его функций
    def admin_add(self):
        name = input('Введите ФИО: ')
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        list_admin.append(name)
        list_admin.append(login)
        list_admin.append(password)


# Админ БД
    def sql_admin(self, tuple_admin):
        try:
            conn = sqlite3.connect('admin1.db')
            cur = conn.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS admin (name TEXT PRIMARY KEY NOT NULL,
              login TEXT NOT NULL, password TEXT NOT NULL)""")

            cur.execute("INSERT INTO admin (name, login, password) VALUES (?, ?, ?)", tuple_admin)

            conn.commit()
            conn.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)


# Кортеж всех админов
    def get_all_admin(self):
         try:
             conn = sqlite3.connect('admin1.db')
             cur = conn.cursor()

             admin_select = """SELECT name FROM admin"""
             cur.execute(admin_select)
             all_admin = cur.fetchall()
             all_admin1 = list(all_admin)
             print(all_admin1)

             conn.commit()
             conn.close()
         except sqlite3.Error as error:
             print("Ошибка при работе с SQLite", error)

# Удаление одного админа
    def get_dell_admin(self):
         try:
             a = input(f'Выберите админа, которого требуется удалить: {self.get_all_admin()}')

             conn = sqlite3.connect('admin1.db')
             cur = conn.cursor()

             admin_del = """DELETE FROM admin WHERE name = ?"""
             cur.execute(admin_del, (a,))

             conn.commit()
             conn.close()
         except sqlite3.Error as error:
             print("Ошибка при работе с SQLite", error)

# Добавление админа
    def get_upgred_admin(self):
        list_admin1 = []

        try:
            name = input('Введите ФИО: ')
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            list_admin1.append(name)
            list_admin1.append(login)
            list_admin1.append(password)

            tuple_admin1 = tuple(list_admin1)
            conn = sqlite3.connect('admin1.db')
            cur = conn.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS admin (name TEXT PRIMARY KEY NOT NULL,
                      login TEXT NOT NULL, password TEXT NOT NULL)""")

            cur.execute("INSERT or IGNORE INTO admin (name, login, password) VALUES (?, ?, ?)", (tuple_admin1, ))

            conn.commit()
            conn.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
            print(list_admin1, 1)






    # def update_status(self):
    #     conn = sqlite3.connect('kvitancii7.db')
    #     cur = conn.cursor()
    #     self.get_info_room()
    #     a1 = input('Введите квитанцию: ')
    #     a = input('Введите статус: ')
    #     sql_update = """UPDATE users SET status = ? WHERE data_done = ?"""
    #     status_done = (a, self.set_data_done())
    #     cur.execute(sql_update, status_done)
    #     conn.commit()
    #     self.get_info_room()






vibor_deystviy2 = ['Сдать в ремонт', "Посмотреть информацию", "Зайти в админ-панель"]
vibor_deystviy3 = ['Отобразить список всех админов.', "Удалить админа из списка.", "Добавить админа.",
                   "Информация о квитанции."]

list_admin = []

a = Admin()
a.choise_admin()
print(list_admin)
tuple_admin = tuple(list_admin)


print(tuple_admin)
#a.sql_admin(tuple_admin)
#a.get_all_admin()
#a.get_dell_admin()
#a.adminka_choice()
#a.admin_add()
#a.get_upgred_admin()
#a.update_status()