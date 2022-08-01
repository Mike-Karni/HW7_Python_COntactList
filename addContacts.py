def AddContactInContactList():
  with open('file.txt', 'a', encoding='utf-8') as data:
    print("Вы выбрали функцию добавления контактов в справочник")
    infor = input("Введите имя фамилию телефон комментарий через пробел ")
    data.write(f'{infor}\n')
