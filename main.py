names = []
surnames = []
phones = []
cities = []
emails = []


def add_to_directory():
    new_name = str(input())
    new_surname = str(input())
    new_phone = str(input())
    new_city = str(input())
    new_email = str(input())
    if (new_email in emails) is False:
        names.append(new_name)
        surnames.append(new_surname)
        phones.append(new_phone)
        cities.append(new_city)
        emails.append(new_email)
    else:
        print('дубль не был добавлен')


def search():
    print('По какой информации хотите искать?')
    request = str(input())
    if request == 'name':
        search_name = str(input())
        if search_name in names:
            i = names.index(search_name)
            print(names[i], surnames[i], phones[i], cities[i], emails[i])
    elif request == 'surname':
        search_surname = str(input())
        if search_surname in surnames:
            i = surnames.index(search_surname)
            print(names[i], surnames[i], phones[i], cities[i], emails[i])
    elif request == 'phone':
        search_phone = str(input())
        if search_phone in phones:
            i = phones.index(search_phone)
            print(names[i], surnames[i], phones[i], cities[i], emails[i])
    elif request == 'city':
        search_city = str(input())
        if search_city in cities:
            i = cities.index(search_city)
            print(names[i], surnames[i], phones[i], cities[i], emails[i])
    elif request == 'e-mail':
        search_emails = str(input())
        if search_emails in emails:
            i = emails.index(search_emails)
            print(names[i], surnames[i], phones[i], cities[i], emails[i])


def change_directory():
    print('Какую информацию хотите изменить?')
    request = str(input())
    if request == 'name':
        print('Какое имя изменить?')
        search_name = str(input())
        print('Введите новое имя')
        change_name = str(input())
        if search_name in names:
            i = names.index(search_name)
            names[i] = change_name
    elif request == 'surname':
        print('Какую фамилию изменить?')
        search_surname = str(input())
        print('Введите новую фамилию')
        change_surname = str(input())
        if search_surname in surnames:
            i = surnames.index(search_surname)
            surnames[i] = change_surname
    elif request == 'phone':
        print('Какой телефон изменить?')
        search_phone = str(input())
        print('Введите новый телефон')
        change_phone = str(input())
        if search_phone in phones:
            i = phones.index(search_phone)
            phones[i] = change_phone
    elif request == 'city':
        print('Какой город изменить?')
        search_city = str(input())
        print('Введите новый город')
        change_city = str(input())
        if search_city in cities:
            i = cities.index(search_city)
            cities[i] = change_city
    elif request == 'e-mail':
        print('Какой e-mail изменить?')
        search_email = str(input())
        print('Введите новый e-mail')
        change_email = str(input())
        if search_email in emails:
            i = emails.index(search_email)
            emails[i] = change_email


def delete():
    print('По какой информации удалять?')
    request = str(input())
    if request == 'name':
        print('Какое имя удалить?')
        search_name = str(input())
        if search_name in names:
            i = names.index(search_name)
            names.pop(i)
            surnames.pop(i)
            phones.pop(i)
            cities.pop(i)
            emails.pop(i)
    elif request == 'surname':
        print('Какую фамилию удалить?')
        search_surname = str(input())
        if search_surname in surnames:
            i = surnames.index(search_surname)
            names.pop(i)
            surnames.pop(i)
            phones.pop(i)
            cities.pop(i)
            emails.pop(i)
    elif request == 'phone':
        print('Какой телефон удалить?')
        search_phone = str(input())
        if search_phone in phones:
            i = phones.index(search_phone)
            names.pop(i)
            surnames.pop(i)
            phones.pop(i)
            cities.pop(i)
            emails.pop(i)
    elif request == 'city':
        print('Какой город удалить?')
        search_city = str(input())
        if search_city in cities:
            i = phones.index(search_city)
            names.pop(i)
            surnames.pop(i)
            phones.pop(i)
            cities.pop(i)
            emails.pop(i)
    elif request == 'e-mail':
        print('Какой e-mail удалить?')
        search_email = str(input())
        if search_email in emails:
            i = emails.index(search_email)
            names.pop(i)
            surnames.pop(i)
            phones.pop(i)
            cities.pop(i)
            emails.pop(i)


add_to_directory()
add_to_directory()
add_to_directory()
add_to_directory()
print(names, surnames, phones, cities, emails)
file = open('1.txt', 'w', encoding='utf-8')
for i in range(len(names)):
    file.write('%s %s %s %s %s\n' % (names[i], surnames[i], phones[i],cities[i],emails[i]))
