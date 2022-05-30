from Level_1 import Intro


class Repair_Intro(Intro):
    def __init__(self, room = None, type_product = None, data_priem = None, data_done = None,
                 initials = None, status = "Ремонтируется"):
        super().__init__(room, type_product, data_priem, data_done, initials, status)


    def get_choice_repair(self):
            self.set_room()
            self.set_initials()
            self.set_type_product()
            self.set_data_priem()
            self.set_data_done()
            self.get_status()
            self.sql_kvitancii(self.get_tuple2())


    def get_info_room(self):
        a = input('Введите квитанцию: ')
        self.get_users_info(a)



    def choice_deystviy(self):
        print('--------------------')
        a = input(f'Выберите действие: {vibor_deystviy}')
        if a == 'Сдать в ремонт':
            self.get_choice_repair()
            print('--------------------')
        else:
            self.get_info_room()




vibor_deystviy = ['Сдать в ремонт', "Посмотреть информацию"]
r = Repair_Intro()
#r.choice_deystviy()
