def ShowMeContactList():
  with open('file.txt', 'r', encoding='utf-8') as data:
    '''read_data = data.read()
    print(f'\n')
    print(f'{read_data}\n')
    print()'''
    for row in data:
      print(f'\n{row}\n')




