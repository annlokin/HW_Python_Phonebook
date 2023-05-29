def add_contact(f):
    input_name = input('Введите Имя:')
    input_last_name = input('Введите Фамилию:')
    input_phone = input('Введите номер телефона')
    data = f'{input_last_name}; {input_name}: {input_phone}'
    with open(f, 'a', encoding='utf-8') as fd:
        fd.write(f'{data}\n')
    print(f'Запись {data} добавлена')

def read_all(f):
      with open (f, 'r', encording='utf-8') as fd:
          print (fd.read())

def search(f):
    last_name = input('Введите фамилию для поиска: ')
    phone_book = read_all(f)
    for line in phone_book:
        if last_name in line:
            flag = 0
            print(line)
    if flag: print('Нет информации')

def menu():
    while True:
        f = ((input('Введите фамилию для поиска: '),
                  input('Введите имя для поиска: ')))
        print(search(f))
