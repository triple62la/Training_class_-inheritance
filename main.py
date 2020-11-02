# This is a sample Python script.
from os.path import splitext


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        """
        :type photo: str
        """
        self.car_type = car_type
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
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl: str = None):
        super(Truck, self).__init__(car_type, brand, photo_file_name, carrying)
        body_lst = body_whl.split('x') or [0, 0, 0]
        self.body_length, self.body_width, self.body_height = map(float, body_lst)
        self.__get_body_volume=None

    @property
    def get_body_volume(self):
        if self.__get_body_volume==None:
             self.__get_body_volume = self.body_length*self.body_width*self.body_height
        return self.__get_body_volume
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
