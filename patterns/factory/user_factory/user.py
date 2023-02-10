from abc import ABC, abstractmethod


class IUser(ABC):
    def __init__(self, *args, **kwargs):
       self.username = kwargs.pop('username', None)
       self.password = kwargs.pop('password', None)
    
    @property
    @abstractmethod
    def role(self):
        ...




class User(IUser):
    @property
    def role(self):
        return 'user'


class Admin(IUser):
    @property
    def role(self):
        return 'admin'

class Support(IUser):
    @property
    def role(self):
        return 'support'

