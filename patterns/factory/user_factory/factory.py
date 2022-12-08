from user import User, Admin, Support


class UserFactory:
    _user_factorys = {
        'user': User,
        'admin': Admin,
        'support': Support
    }

    def get_user(self, data: dict):
        user_role = data.get('role', None)
        if not user_role:
            raise Exception("No user role specified")
        if not user_role in self._user_factorys.keys():
            raise Exception("Wrang user role specified")
        
        factory = self._user_factorys[user_role]
        user = factory(**data)

        return user
