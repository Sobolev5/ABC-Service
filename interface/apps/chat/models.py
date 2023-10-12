import re
from simple_print import sprint
from .db import RamDB

# lesson5 lesson6 
class BaseField: 

    def __init__(self, max_length=140, null=True):         
        self.max_length = max_length
        self.null = null
        self.value = None

    validate_exp = r'^.+$'

    def __set_name__(self, owner, name):
        # https://pythonz.net/references/named/object.__set_name__/
        # self._name -> author, message в данном контексте
        self._name = name
    
    def __get__(self, instance, owner):
        return self.value
        
    def __set__(self, instance, value):
        if not value and not self.null:
            raise TypeError(self._name)
        elif self.null and not self.value:
            pass
        else:
            if not self.validate(value):
                raise ValueError(f"{self._name} does not match {self.validate_exp}")
            
            if len(value) > self.max_length:
                raise ValueError(f"{self._name} is greater than {self.max_length}")    
            self.value = value

    def validate(self, value):
        return bool(re.match(self.validate_exp, str(value)))


class CharField(BaseField):
    validate_exp = r'^[A-Za-z ]+$'

class IntegerField(BaseField):
    validate_exp = r'\d+'

# Пример наследования (делаем EmailField)
class EmailField(BaseField):
    validate_exp = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'


class RamDirectOrmModel: 
    ALLOCATED_DATA_IN_RAM = []
    
    def __init__(self, **kwargs):
        classfields = [field for field in self.__class__.__dict__ if field[0] != '_'] 
        # if field[0] != '_' отсекаем магические методы
        for field in classfields:
            if kwargs.get(field):
                self.__setattr__(field, kwargs.get(field))

    def save(self):
        classfields = [field for field in self.__class__.__dict__ if field[0] != '_'] 
        # if field[0] != '_' отсекаем магические методы
        data = {}
        for field in classfields:
            data[field] = self.__getattribute__(field)
        RamDirectOrmModel.ALLOCATED_DATA_IN_RAM.append(data)

    @classmethod
    def all(cls):
        return cls.ALLOCATED_DATA_IN_RAM  


# НЕ КОПИРОВАТЬ (ЭТО РЕШЕНИЕ ЗАДАЧИ)
class RamDBOrmModel: 

    db = RamDB()

    def __init__(self, **kwargs):
        classfields = [field for field in self.__class__.__dict__ if field[0] != '_'] 
        RamDBOrmModel.db.create_table(table_name=self.__class__.__name__.lower(), fields=tuple(classfields))  
        for field in classfields:
            self.__setattr__(field, kwargs.get(field))

    def save(self):
        classfields = [field for field in self.__class__.__dict__ if field[0] != '_'] 
        data = {}
        for field in classfields:
            data[field] = self.__getattribute__(field)
        RamDBOrmModel.db.create_record(table_name=self.__class__.__name__.lower(), record=[v for k,v in data.items()])

    @classmethod
    def all(cls):     
        return cls.db.read_record(table_name=cls.__name__.lower())


class ChatMessage(RamDirectOrmModel):
    room_id = IntegerField(null=False)
    author = CharField(max_length=150, null=False) 
    message = CharField(max_length=150, null=False)


