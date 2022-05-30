
# import sqlite3
#
# class Sql:
#     # def __init__(self, room = None, type_product = None, data_priem = None, data_done = None,
#     #               initials = None, status = "Ремонтируется"):
#     #      super().__init__(room, type_product, data_priem, data_done, initials, status)
#
#     # Создание БД
#     def sql_kvitancii(self, tuple2):
#         try:
#             conn = sqlite3.connect('kvitancii7.db')
#             cur = conn.cursor()
#
#             cur.execute("CREATE TABLE IF NOT EXISTS users"
#                         "(room INTEGER PRIMARY KEY,"
#                             "name TEXT, type_product TEXT, info_product TEXT, info_product2 TEXT, info_product3 TEXT,"
#                             "info_product4 TEXT,"
#                              " data_priem TEXT, data_done TEXT,"
#                             "status TEXT)")
#             if len(tuple2) == 10:
#                 cur.execute("""INSERT INTO users (room, name, type_product, info_product,
#                      info_product2, info_product3, info_product4, data_priem, data_done, status)
#                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", tuple2)
#
#             else:
#                 cur.execute("""INSERT INTO users (room, name, type_product, info_product,
#                                  info_product2, info_product3, info_product4, data_priem, data_done, status)
#                                  VALUES (?, ?, ?, ?, ?, ?, NULL, ?, ?, ?)""",
#                             tuple2)
#
#             conn.commit()
#             conn.close()
#         except sqlite3.Error as error:
#             print("Ошибка при работе с SQLite", error)
#
#     # Печать пользователя по квитанции
#     def get_users_info(self, room):
#         try:
#             conn = sqlite3.connect('kvitancii7.db')
#             cur = conn.cursor()
#
#             sql_select = """SELECT * FROM users WHERE room = ?"""
#             cur.execute(sql_select, (room,))
#             rec = cur.fetchall()
#             for row in rec:
#                 print('Квитанция: ', row[0])
#                 print('Имя: ', row[1])
#                 print('Тип продукта: ', row[2])
#                 print('Информация о продукте:', row[3], row[4], row[5], row[6], sep=', ')
#                 print('Дата приема: ', row[7])
#                 print('Дата готовности: ', row[8])
#                 print('Статус: ', row[9])
#
#             conn.commit()
#             conn.close()
#         except sqlite3.Error as error:
#             print("Ошибка при работе с SQLite", error)
#
#     # Админ БД
#     def sql_admin(self, tuple_admin):
#         try:
#             conn = sqlite3.connect('admin1.db')
#             cur = conn.cursor()
#
#             cur.execute("""CREATE TABLE IF NOT EXISTS admin (name TEXT PRIMARY KEY NOT NULL,
#              login TEXT NOT NULL, password TEXT NOT NULL)""")
#
#             cur.execute("INSERT INTO admin (name, login, password) VALUES (?, ?, ?)", tuple_admin)
#
#             conn.commit()
#             conn.close()
#         except sqlite3.Error as error:
#             print("Ошибка при работе с SQLite", error)
#
#     # Кортеж всех админов
#     def get_all_admin(self):
#         try:
#             conn = sqlite3.connect('admin1.db')
#             cur = conn.cursor()
#
#             admin_select = """SELECT name FROM admin"""
#             cur.execute(admin_select)
#             all_admin = cur.fetchall()
#             all_admin1 = list(all_admin)
#             print(all_admin1)
#
#             conn.commit()
#             conn.close()
#         except sqlite3.Error as error:
#             print("Ошибка при работе с SQLite", error)
#
#     # Удаление одного админа
#     def get_dell_admin(self):
#         try:
#             a = input(f'Выберите админа, которого требуется удалить: {self.get_all_admin()}')
#
#             conn = sqlite3.connect('admin1.db')
#             cur = conn.cursor()
#
#             admin_del = """DELETE FROM admin WHERE name = ?"""
#             cur.execute(admin_del, (a,))
#
#             conn.commit()
#             conn.close()
#         except sqlite3.Error as error:
#             print("Ошибка при работе с SQLite", error)
#
#
#     # Добавление админа
#     def get_upgred_admin(self, tuple_admin):
#         try:
#             #self.admin_add()
#             conn = sqlite3.connect('admin1.db')
#             cur = conn.cursor()
#
#             cur.execute("""CREATE TABLE IF NOT EXISTS admin (name TEXT PRIMARY KEY NOT NULL,
#                      login TEXT NOT NULL, password TEXT NOT NULL)""")
#
#             cur.execute("INSERT or IGNORE INTO admin (name, login, password) VALUES (?, ?, ?)", (tuple_admin, ))
#
#             conn.commit()
#             conn.close()
#         except sqlite3.Error as error:
#             print("Ошибка при работе с SQLite", error)

#s = Sql()
# s.sql_kvitancii()
# s.get_users_info()
# s.sql_admin()
# s.get_all_admin()
# s.get_dell_admin()
#s.get_upgred_admin()


