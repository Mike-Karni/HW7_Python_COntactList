import PrintContactList
import addContacts
def MainFunction():
    command = input(("Введите 1 , если вы хотите просмотреть список контактов\n"
           "Введите 2 , если вы хотите добавить в список контактов\n"))
    if command =="1":
        PrintContactList.ShowMeContactList()
    elif command =="2":
        addContacts.AddContactInContactList()
    else:
        print("Вы осуществили неправильный ввод. Перезапустите и введите нормально!")