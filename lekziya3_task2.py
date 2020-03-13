phonenumber  = input("Введите номер телефона =  ")
nat_num = "38"
if len(phonenumber) == 10:
    print (nat_num + phonenumber)
    print("Данные номмера телефона КОРРЕКТНЫ")
else:
    print("Данные номера телефона НЕ КОРРЕКТНЫ")