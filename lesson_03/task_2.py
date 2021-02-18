

def show_info(name, surname, birth_year, residence_city, email, phone, sep='; '):

    info = sep.join((
        f'name: {name}',
        f'surname: {surname}',
        f'birth_year: {birth_year}',
        f'residence_city: {residence_city}',
        f'email: {email}',
        f'phone: {phone}',
    ))
    
    print(info)


show_info(name='Pavel', surname='Vaschenko', birth_year=1989, residence_city='Novosibirsk', email='qwerty@qwerty.com', phone='+7-000-000-00-00')