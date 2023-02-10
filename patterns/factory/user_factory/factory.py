from user import Admin, Support, User


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
        if user_role not in self._user_factorys.keys():
            raise Exception("Wrang user role specified")
        
        factory = self._user_factorys[user_role]
        user = factory(**data)

        return user
