"""
ПАТТЕРНЫ ПРЕОКТИРОВАНИЯ
https://refactoring.guru/ru/design-patterns
Из чего состоит:
проблема которую решает паттерн
мотивации к решению проблем способом, который предлагает паттерн
структуры классов, составляющих регшение
примера наодном из языков программирования
особенностей реализации в различных контекстах
связей с други ми паттернами

"Язык шаблонов города Здания Строительство" -> Примеры ООП. Паттерны проектирования (Gof book, книга от бонды четрых)

Зачем?
Проверенные решения
Стандартизация кода
Общий программистский словарь

Декоратор - это паттерн

MVC - тоже паттерн, по нему создает веб. В джанго это MTC
modul - где лежат наши даные. БД
view - шаблон, темплейтс
Control - логика


Идиомы - низкоуровневые и простые паттерны
Архитектурные паттерны - которые омжно риадизовать практически
на любом языке и проектирвоания всей программы

Виды паттернов:
Порождающие - беспокоятся о гибком создании объектов без внесения в программу лишних зависимосетй
Струткурные - показввают рпзличные способы построения сваязей между объектами
Поведенческие - эффективная коммуникация между объектами


ФАБРИЧНЫЙ   МЕТОД
Порождающий паттерн проетирования которфй определяет общий интпфейс
 для создлания обезвтов в суперклассе, позволяя подклассам изменять тип создаваемых объектов
 Применимо когда неизвестны тиаы и зависмсмомти объектов

 преимущества
 избавляет класс от привязки к конкретным классам продуков
 Выделяет код произво
 Суть в применнии абстратного класса и абстрактного метода


from abc import ABC, abstractmethod
#ABC класс из  модуля который делает класс абсратктным.
# СОздать объект  Animal() напрямую нельзя, только через подкласс
# @abstractmetod - декоратор который говорит: каждый декоратор обязан реализовать этот метод
# есои не реализуешь  - питон выбросит ошибку при создании объекта
#Продукт
class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

class Dog(Animal):
    def speak(self) -> str:
        return "Гав!"

class Cat(Animal):
    def speak(self) -> str:
        return "Мяу!"

#Создатель
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

    def make_sound(self)->str:
        animal = self.create_animal()
        return f"Животное говорит: {animal.speak()}"

class DogFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Cat()

#использование
factory = DogFactory()
print(factory.make_sound())

factory = CatFactory()
print(factory.make_sound())


from abc import ABC, abstractmethod
#Продукт
class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        pass

class EmailNotification(Notification):
    def send(self, message: str) -> str:
        return f'[Email] отправлено: {message}'

class SMSNotification(Notification):
    def send(self, message: str) -> str:
        return f'[SMS] отправлено: {message}'

class PushNotification(Notification):
    def send(self, message: str) -> str:
        return f'[Push] отправлено: {message}'

# асбратктные создатели
class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass

    def notify(self, message: str) -> str:
        notification = self.create_notification()
        return notification.send(message)

# конкретные создатели
class EmailFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()

class SMSFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return SMSNotification()

class PushFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return PushNotification()

#Функция отправки
def send_alert(factory: NotificationFactory, message: str):
    print(factory.notify(message))

send_alert(EmailFactory(), "Ваш заказ подтвержден")
send_alert(SMSFactory(), "Код подтверждения: 5347")
send_alert(PushFactory(), "У вас новое сообщение")


from abc import ABC, abstractmethod
#Продукт
class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        pass

class MaxNotification(Notification):
    def send(self, message: str) -> str:
        return f'[Max] отправлено: {message}'

class TelegramNotification(Notification):
    def send(self, message: str) -> str:
        return f'[Telegram] отправлено: {message}'

class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass

    def notify(self, message: str) -> str:
        notification = self.create_notification()
        return notification.send(message)

class MaxFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return MaxNotification()

class TelegramFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return TelegramNotification()

def send_alert(factory: NotificationFactory, message: str):
    print(factory.notify(message))

send_alert(MaxFactory(), 'Я сканирую твой жесткий диск')
send_alert(TelegramFactory(), 'Я работаю только с VPN')

"""

"""
АДАПТЕР (ОБЕРТКА, вРАППЕР) - структурный
Позволяет объектам с несовместимым интерфейсом работать вместе

Когда вы хотите использовать сторонний класс, но его 
интерфейс(в данном контексте абстрактный класс, или расширение функционала) 
не соотвествует остальному коду приложения.
Адаптер поможет позволяет создать объект-прокладку, который будет арверащать вызовы приложения в формат, 
понятный стороннему классу

Когда вам нужно использовать несколько существующих подклассов, но в них 
не хватает какой-то общей функциональности, причем расширить суперклассов 
вы не можете (не можем создавать объекты)

Вы могли  бы создать еще один уровень подкалссов и добавить в них недостающую функционаьльность. 
Но при этом дублировать один и тот эе кодв обеих ветках подклассов

Найти премумущества и ннедостатки
"""
from abc import ABC, abstractmethod

class EuropeanSocket(ABC):
    @abstractmethod
    def charge_220v(self):
        pass

#адаптируемый класс
class AmericanDevice:
    def charge_110v(self):
        return "Заряжусь от 110v (американская вилка)"
#адаптер между двумя интерфесами
class AmericanToEuropeanAdapter(EuropeanSocket):

    def __init__(self, american_device: AmericanDevice):
        self._device = american_device

    def charge_220v(self) -> str:
        result = self._device.charge_110v()
        return f"Адаптер преобразует 220v -> 110 v | {result}"

def plugin_in(socket: EuropeanSocket):
    print(socket.charge_220v())

american_laptop = AmericanDevice()
adapter = AmericanToEuropeanAdapter(american_laptop)
plugin_in(adapter)




