# Task 2, Option 22

import datetime
import re 
import random

class Account():    # The base class for different account types
    type = 'Account'

    def __init__(self, user):
        self.__number = self.type[0] + user.name[0] + user.surname[0] + \
                        str(user.birthdate.date()).replace('-','')    # Creating an account number using user data
        self.__user = user
        self.__balance = 0

    # Encapsulation implementation below using build-in decorators 
    # for getting, setting and validating attributes

    @property
    def number(self):
        return self.__number

    @property
    def user(self):
        return self.__user

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def add_money(self, sum):   # The method for adding money to an account
        self.__balance += sum
        print('\nAdded', sum, 'to', self.__number, \
              'account\nCurrent balance:', self.__balance)
    
    def take_money(self, sum):   # The method for taking money from an account
        self.__balance -= sum
        print('\nTook', sum, 'from', self.__number, \
              'account\nCurrent balance:', self.__balance)

    def __str__(self):
        return "\n" + self.type + ' - {}{}\nBalance: {}'.format(self.__number,\
               str(self.__user), str(self.__balance)) 

class SavingsAccount(Account):
    type = 'Savings Account'
    
    def __init__(self, user, percent):
        self.__percent = percent
        super().__init__(user)    # Using a superclass constructor for initializing fields inherited from the superclass

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, value):
        self.__percent = value

    def add_percents(self):   # The method for adding money to an account according to the percents
        self.balance += self.balance * self.percent / 100
        print('\nAdd', self.percent, 'percents to', self.number, \
              'account\nCurrent balance:', self.balance)

    def __str__(self):   # Override the base method by calling it and add current class info
        return super().__str__() + '\nPercent: {}%'.format(self.percent)

class PaymentAccount(Account):
    type = 'Payment Account'
    
    def __init__(self, user, payment):
        self.__payment = payment
        super().__init__(user)    # Using a superclass constructor for initializing fields inherited from the superclass

    @property
    def payment(self):
        return self.__payment

    @payment.setter
    def payment(self, value):
        self.__payment = value

    def make_payment(self):   # The method for making payment on an account according to the payment value
        self.balance -= self.payment
        print('\nMade payment:', self.payment, 'for', self.number, \
              'account\nCurrent balance:', self.balance)

    def __str__(self):   # Override the base method by calling it and add current class info
        return super().__str__() + '\nPayment: {}'.format(self.__payment)

class CurrencyAccount(Account):
    type = 'Currency Account'
    course = 2.20
    def __init__(self, user, currency):
        self.__currency = currency
        super().__init__(user)   # Using a superclass constructor for initializing fields inherited from the superclass

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        self.__currency = value

    def to_local_currency(self):    # The method for givinig information about the balance using local currency
        local_balance = self.balance * self.course
        print('\n', self.balance, self.currency, 'to local currency:', local_balance)

    def __str__(self):   # Override the base method by calling it and add current class info
        return super().__str__() + '\nCurrency: {}'.format(self.__currency)
        
class Address():
    def __init__(self, zip='Undefined', country='Undefined', city='Undefined', \
                 region='Undefined', street='Undefined', number='Undefined', \
                 room='Undefined'):
        self.__zip = zip
        self.__country = country
        self.__city = city
        self.__region = region
        self.__street = street
        self.__number = number
        self.__room = room

    # Encapsulation implementation below using build-in decorators for getting, 
    # setting and validating attributes using regural expressions

    @property
    def zip(self):
        return self.__zip

    @zip.setter
    def zip(self, value):
        if len(value) < 20 and re.match("^[0-9]+$", value):
            self.__zip = value
        else:
            print('Incorrect zip code: {}'.format(value))

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value) < 50 and re.match("^[a-zA-Z- ]+$", value):
            self.__country = value
        else:
            print('Incorrect country name: {}'.format(value))

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if len(value) < 50 and re.match("^[a-zA-Z- ]+$", value):
            self.__city = value
        else:
            print('Incorrect city name: {}'.format(value))

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, value):
        if len(value) < 50 and re.match("^[a-zA-Z-.' ]+$", value):
            self.__region = value
        else:
            print('Incorrect region name: {}'.format(value))

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        if len(value) < 50 and re.match("^[a-zA-Z- ]+$", value):
            self.__street = value
        else:
            print('Incorrect street name: {}'.format(value))

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if len(value) < 10 and re.match("^[a-zA-Z0-9 ]+$", value):
            self.__number = value
        else:
            print('Incorrect number: {}'.format(value))

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, value):
        if len(value) < 10 and re.match("^[a-zA-Z0-9- ]+$", value):
            self.__room = value
        else:
            print('Incorrect room: {}'.format(value))

    def __str__(self):
        cnt = 0
        for value in self.__dict__.values():
            if value == "Undefined":
                cnt += 1
        return '\nAddress: ' + self.__zip + " " + self.__country + ', ' + \
               self.__region + ', ' +  self.__city + ', ' + self.__street + \
               ', ' + self.__number + ', ' +  self.__room \
               if cnt != len(self.__dict__) else "\nAddress: Undefined"

class Person():
    def __init__(self, name='Undefined', surname='Undefined', birthdate= \
                 datetime.datetime.now(), phone='Undefined', address=Address()):
        self.__name = name
        self.__surname = surname
        self.__birthdate = birthdate
        self.__phone = phone
        self.__address = address

    @property
    def name(self):
        return self.__name
 
    @name.setter
    def name(self, name):
        if len(name) < 50 and re.match("^[a-zA-Z-']+$", name):
            self.__name = name
        else:
            print('Incorrect name: {}'.format(name))

    @property
    def surname(self):
        return self.__surname
 
    @surname.setter
    def surname(self, surname):
        if len(surname) < 50 and re.match("^[a-zA-Z-']+$", surname):
            self.__surname = surname
        else:
            print('Incorrect surname: {}'.format(surname))

    @property
    def birthdate(self):
        return self.__birthdate
 
    @birthdate.setter
    def birthdate(self, date):
        if date < datetime.datetime.now():
            self.__birthdate = date
        else:
            print('Incorrect date: {}'.format(str(date)))
    
    @property
    def phone(self):
        return self.__phone
 
    @phone.setter
    def phone(self, phone):
        if len(phone) < 20 and re.match("^[0-9+]+$", phone):
            self.__phone = phone
        else:
            print('Incorrect phone number: {}'.format(str(phone)))

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address 

    def __str__(self):
        return '\nName: ' + self.__name + '\nSurname: ' + self.__surname + \
               '\nBirthdate: ' + str(self.__birthdate.date()) + \
               '\nPhone: ' + self.__phone + str(self.__address)

def random_sum():
    return random.randrange(0, 1000)

if __name__ == '__main__':

    # Aggregation implementation by creating an object of an Address class 
    # and giving it to a Person object constructor as a parameter 

    pers1 = Person()
    pers1.name = 'Anna'
    pers1.surname = 'Slyadneva'
    pers1.phone = '+375295167195'
    pers1.birthdate = datetime.datetime(1973, 2, 23)
    addr1 = Address()
    addr1.zip = '211443'
    addr1.country = 'Belarus'
    addr1.region = 'Vitebsk reg.'
    addr1.city = 'Novopolotsk'
    addr1.street = 'Molodezhnaya'
    addr1.number = '14'
    addr1.room = '91'
    pers1.address = addr1

    pers2 = Person('Elena', 'Zavadskaya', datetime.datetime(1999, 4, 29), \
                   '+375447213359', Address('220103', 'Belarus', 'Minsk', \
                   'Minsk reg.', 'Kalinovskogo', '79', '25'))
    
    pers3 = Person(input('Enter name: '), input('Enter surname: '), \
                   datetime.datetime.strptime(\
                   input('Enter birthdate (dd.mm.yyyy): '), "%d.%m.%Y"), \
                   input('Enter phone: '), Address(input('Enter zip code: '), \
                   input('Enter country: '), input('Enter region: '), \
                   input('Enter city: '), input('Enter street: '), \
                   input('Enter number: '), input('Enter room: ')))
    
    print(pers1, pers2, pers3)
    
    acc1 = SavingsAccount(pers1, 3)
    acc1.add_money(random_sum())
    acc1.add_money(random_sum())
    acc1.take_money(random_sum())
    acc1.add_percents()
    print(acc1)

    acc2 = PaymentAccount(pers2, 100)
    acc2.add_money(random_sum())
    acc2.take_money(random_sum())
    acc2.make_payment()
    print(acc2)

    acc3 = CurrencyAccount(pers3, 'USD')
    acc3.add_money(random_sum())
    acc3.take_money(random_sum())
    acc3.to_local_currency()
    print(acc3)


    

    

