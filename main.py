# This is a sample Python script.
from os.path import splitext
import csv

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        """
        :type photo: str
        """
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    @property
    def photo_file_name(self):
        return self.__photo_file_name

    @photo_file_name.setter
    def photo_file_name(self, path):
        ext = splitext(path)
        if not self._check_ext(ext[1]):
            raise ValueError('Wrong file type')
        self.__photo_file_name = path

    @staticmethod
    def _check_ext(ext):
        ext_lst = ['.jpg', '.jpeg', '.png', '.gif']
        if ext in ext_lst:
            return True
        return False

    def get_photo_file_ext(self):
        path = self.photo_file_name
        ext = splitext(path)
        return ext[1]


class Truck(CarBase):
    car_type = 'truck'
    def __init__(self,  brand, photo_file_name, carrying, body_whl: str = None):
        super(Truck, self).__init__( brand, photo_file_name, carrying)
        body_lst = body_whl.split('x') or [0, 0, 0]
        self.body_length, self.body_width, self.body_height = map(float, body_lst)
        self.__get_body_volume=None

    @property
    def get_body_volume(self):
        if self.__get_body_volume==None:
             self.__get_body_volume = self.body_length*self.body_width*self.body_height
        return self.__get_body_volume
class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, photo_file_name, carrying,passenger_seats_count):
        super(Car,self).__init__(brand,photo_file_name,carrying)
        self.passenger_seats_count=passenger_seats_count

class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __init__(self, brand, photo_file_name, carrying,extra):
        super(SpecMachine,self).__init__(brand,photo_file_name,carrying)
        self.extra=extra

def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            print(row)
    return car_list
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   man=Truck('Man','man.jpg','20',body_whl='4x5x2.5')
   print(man.get_body_volume,man.car_type)
   get_car_list('_af3947bf3a1ba3333b0c891e7a8536fc_coursera_week3_cars.csv')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
