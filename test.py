from os.path import splitext


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class CarBase:
    def __init__(self, car_type:str, brand:str, photo_file_name:str, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file = photo_file_name
        self.carrying = carrying

    @staticmethod
    def _check_ext(ext):
        ext_lst = ['.jpg', '.jpeg', '.png', '.gif']
        if ext in ext_lst:
            return True
        return False

    @property
    def file(self):
        return self.__photo_file

    @file.setter
    def file(self, photo_file_name):
        print('setter')
        ext = self.get_photo_file_ext()
        if not self._check_ext(ext):
            raise ValueError('Wrong file format')
        self.__photo_file = photo_file_name

    def get_photo_file_ext(self):
        ext = splitext(self.photo_file)
        return ext[1]

car=CarBase('car','bmw',r'./test/test.txt',15)
print(car.get_photo_file_ext())
print(car._check_ext(car.get_photo_file_ext()))
print(car.photo_file)