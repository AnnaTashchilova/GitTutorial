from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком варианте записать данные?\n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'\nВаш выбор: '
                    ))
    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf-8") as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open("data_second_variant.csv", "a", encoding="utf-8") as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')



def print_data():
    print("1 файл: ")
    with open("data_first_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            print(i, end="")

    print("2 файл: ")
    with open("data_second_variant.csv", "r", encoding="utf-8") as file:
        data = file.readlines()
        for i in data:
            if i != '\n':
                print(i, end="")

def delete_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком варианте удалить данные?\n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'\nВаш выбор: '
                    ))
    if var == 1:
        with open("data_first_variant.csv", "r+", encoding="utf-8") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if (name.lower() not in line.lower()) or (surname.lower() not in line.lower()) or (phone.lower() not in line.lower()) or (adress.lower() not in line.lower()):
                    file.write(line)
                file.truncate()
            
    else:
        with open("data_second_variant.csv", "r+", encoding="utf-8") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if (name.lower() not in line.lower()) or (surname.lower() not in line.lower()) or (phone.lower() not in line.lower()) or (adress.lower() not in line.lower()):
                    file.write(line)
                file.truncate()
    
def change_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком варианте изменить данные?\n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'\nВаш выбор: '
                    ))
    if var == 1:
        new_name, new_surname, new_phone, new_adress = input_user_data()
        with open("data_first_variant.csv", "r+", encoding="utf-8") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if (name.lower() in line.lower()) and (surname.lower() in line.lower()) and (phone.lower() in line.lower()) and (adress.lower() in line.lower()):
                    file.write( f'{new_name}\n'
                                f'{new_surname}\n'
                                f'{new_phone}\n'
                                f'{new_adress}\n\n')
                else:
                    file.write(line)
            file.truncate()
            
    else:
        new_name, new_surname, new_phone, new_adress = input_user_data()
        with open("data_second_variant.csv", "r+", encoding="utf-8") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if (name.lower() in line.lower()) and (surname.lower() in line.lower()) and (phone.lower() in line.lower()) and (adress.lower() in line.lower()):
                    file.write(f'{new_name};{new_surname};{new_phone};{new_adress}\n\n')
                else:
                    file.write(line)
            file.truncate()