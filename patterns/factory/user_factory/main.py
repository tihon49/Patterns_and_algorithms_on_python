from factory import UserFactory


user_data = {
    'username': 'John',
    'password': 'password',
    'role': 'user'
}

admin_data = {
    'username': 'SuperAdmin',
    'password': 'P@ssw0rd',
    'role': 'admin'
}

support_data = {
    'username': 'SupportMan',
    'password': 'test',
    'role': 'support'
}


def main():
    factory = UserFactory()
    user = factory.get_user(user_data)
    admin = factory.get_user(admin_data)
    support = factory.get_user(support_data)
    
    users_list = [user, admin, support]

    for u in users_list:
        print(u.username)
        print(u.password)
        print(u.role)
        print()


if __name__ == '__main__':
    main()
