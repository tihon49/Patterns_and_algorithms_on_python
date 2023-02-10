class File:
    def __init__(self, name):
        self.name = name
    
    def decor_1(method):
        def wrapper(self):
            print('before method')
            self.name = self.name + '_wrapped'
            print('after method')
        return wrapper
    
    def decor_2(method):
        def wrapper(*args, **kwargs):
            print('before method')
            method(*args, **kwargs)
            print('after method')
        return wrapper
    
    def decor_3(flag=False):
        def inner(method):
            def wrapper(*args, **kwargs):
                print('before method')
                if flag:
                    print('FLAG IS ON')
                    method(*args, **kwargs)
                else:
                    print('FLAG IS OFF')
                    method(*args, **kwargs)
            return wrapper
        return inner
            
    @decor_1
    def get_name(self):
        print('get_name')

    @decor_2
    def get_name2(self):
        print('get_name')

    @decor_3(False)
    def get_name3(self):
        print('get_name with flag')
    

f = File('my_name')
f.get_name()
print()
f.get_name2()
print()
f.get_name3()
