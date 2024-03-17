import sqlite3


class BaseType:
    field_type: str  # название типа данных поля

    def __init__(self, unique: bool = False, null: bool = True, default: int = None):
        self.unique = unique
        self.null = null
        self.default = default


class IntegerField(BaseType):
    field_type = 'INTEGER'


class TextField(BaseType):
    field_type = 'TEXT'


class BlobField(BaseType): # Двоичные данны
    field_type = 'BLOB'


class RealField(BaseType): #данные с плавующей точкой
    field_type = 'REAL'


class NumericField(BaseType):
    field_type = 'NUMERIC' # = int


class Model:
    def __init__(self, *args, **kwargs):
        fields = [el for el in vars(self.__class__) if not el.startswith("_")] #поля, которые мы создали в модели
        for i, value in enumerate(args):
            setattr(self, fields[i], value)  # задаем переменные переданные с помощью args

        for field, value in kwargs.items():  # задаем переменные переданные с помощью kwargs
            setattr(self, field, value)

    def json(self):
        attributes = {}
        for key, value in vars(self).items():
            if not key.startswith("__") and not callable(value):  # проверка на системные методы и поля
                attributes[key] = value

        return attributes


class Box(Model):
  name = TextField()
  width = IntegerField()
  height = IntegerField()


print(Box('Box 1', 1, 1).json())#выведет {'name': 'Box 1', 'width': 1, 'height': 1}
