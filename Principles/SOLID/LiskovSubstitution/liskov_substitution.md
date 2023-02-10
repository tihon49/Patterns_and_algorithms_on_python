# Принцип подстановки Лисков

    Принцип подстановки Лисков направлен на то, чтобы дочерний класс мог
    занять место своего родительского класса, не вызывая ошибок.

Рассмотрим следующий пример:

```python
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message, email):
        pass


class Email(Notification):
    def notify(self, message, email):
        print(f'Send {message} to {email}')


class SMS(Notification):
    def notify(self, message, phone):
        print(f'Send {message} to {phone}')


if __name__ == '__main__':
    notification = SMS()
    notification.notify('Hello', 'john@test.com')
```

В этом примере у нас есть три класса: Notification, Email и SMS. Классы Email и SMS наследуют от класса Notification.

Абстрактный класс Notification имеет метод notify() который отправляет сообщение на адрес электронной почты.

Метод notify() класса Email отправляет сообщение на электронную почту, что нормально.

Однако для отправки сообщения класс SMS использует номер телефона, а не адрес электронной почты. Поэтому нам нужно изменить подпись метода notify() класса SMS, чтобы принять номер телефона вместо электронной почты.

<br>

Следующий класс NotificationManager использует объект Notification для отправки сообщения Contact:

```python
class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    def __init__(self, notification, contact):
        self.contact = contact
        self.notification = notification

    def send(self, message):
        if isinstance(self.notification, Email):
            self.notification.notify(message, contact.email)
        elif isinstance(self.notification, SMS):
            self.notification.notify(message, contact.phone)
        else:
            raise Exception('The notification is not supported')


if __name__ == '__main__':
    contact = Contact('John Doe', 'john@test.com', '(408)-888-9999')
    notification_manager = NotificationManager(SMS(), contact)
    notification_manager.send('Hello John')

# Метод send() класса NoticationManager принимает объект уведомления. Он
# проверяет, является ли уведомление экземпляром Email или SMS, и передает
# адрес электронной почты и контактный телефон методу notify()
# соответственно
```

---

## Приведение к соответствию принципу подстановки Лисков

<br>

Сначала переопределим метод notify() класса Notification, чтобы он не
включал параметр email:

```python
class Notification(ABC):
    @abstractmethod
    def notify(self, message):  # <--- убрали аргумент email
        pass
```

Во-вторых, добавим параметр email в __init__ класса Email:

```python
class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send "{message}" to {self.email}')
```

В-третьих, добавим параметр phone в __init__ класса SMS:

```python
class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send "{message}" to {self.phone}')
```

В-четвертых, изменим класс NotificationManager:

```python
class NotificationManager:
    def __init__(self, notification):
        self.notification = notification
    
    def set_notification(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)
```

---

## Сложим все это вместе:

```python
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send "{message}" to {self.email}')


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send "{message}" to {self.phone}')


class Contact:
    """Класс контакта"""
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    def __init__(self, notification):
        self.notification = notification
    
    def set_notification(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == '__main__':
    contact = Contact(
        name='John Doe',
        email='john@test.com',
        phone='(408)-888-9999'
    )

    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)

    notification_manager = NotificationManager(sms_notification)
    notification_manager.send('Hello John')

    notification_manager.set_notification(email_notification)
    notification_manager.send('Hi John')
```

    # Вывод
    Send "Hello John" to (408)-888-9999
    Send "Hi John" to john@test.com

