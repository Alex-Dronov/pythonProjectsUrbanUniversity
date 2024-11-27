import types
import inspect
from pprint import pprint


class Car:
    """Класс описывающий программную модель автомобиля"""

    def __init__(self, brand, color='white', number_of_doors=4, size_of_tyres='R16'):
        self.speed = 0
        self.isStopped = None
        self.isStarted = None
        self.brand = brand
        self.color = color
        self.number_of_doors = number_of_doors
        self.size_of_tyres = size_of_tyres

    def start(self):
        """Включить зажигание и запустить двигатель"""
        if self.isStopped:
            self.isStarted = True
        else:
            print('Двигатель работает')
        return self.isStarted

    def stop(self):
        """Отключить зажигание и остановить двигатель"""
        if self.isStarted:
            self.isStopped = True
        else:
            print('Автомобиль не заведен')

    def go(self, speed):
        """ Двигаться со скоростью 'speed'"""
        if self.isStarted:
            self.speed = speed
        else:
            print('Автомобиль не заведен')


def introspection_info(_obj):
    _obj_info = {}
    _methods_inspect = []
    _methods_types = []
    _all_attributes = []

    for attr_name in dir(_obj):
        attr = getattr(_obj, attr_name)

        if inspect.ismethod(attr):
            _methods_inspect.append(attr_name)
        else:
            _all_attributes.append(attr_name)

        if type(attr) is types.MethodType:
                _methods_types.append(attr_name)

    _obj_info.__setitem__('1.Тип объекта/Type of an object', type(_obj))
    _obj_info.__setitem__('2.Описание/Description', inspect.getdoc(_obj))
    _obj_info.__setitem__('3.Модуль/Module', str(inspect.getmodule(_obj)).split(sep=' from')[0] + '>')
    _obj_info.__setitem__('4.Переменные/Writable attributes/Vars - вариант _obj.__dict__', _obj.__dict__)
    _obj_info.__setitem__('5.Переменные/Writable attributes/Vars - вариант vars(_obj)', vars(_obj))
    _obj_info.__setitem__('6.Методы/Methods вариант types.MethodType', _methods_types)
    _obj_info.__setitem__('7.Методы/Methods вариант inspect.ismethod(obj)', _methods_inspect)
    _obj_info.__setitem__('8.Все атрибуты/All attributes', _all_attributes)


    return _obj_info


firstCar = Car('VW', 'Red')

_info = introspection_info(firstCar)
pprint(_info)