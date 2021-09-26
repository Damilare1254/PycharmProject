class Converter:
    def __init__(self, weight):
        self.__weight = weight

    def set_kilogram(self):
        return  self.__weight

    def convert_kilogram_to_pounds(self):
        weight4 = float(self.__weight) / 0.454
        return weight4

    def convert_pounds_to_kilogram(self):
        weight3 = float(self.__weight) * 0.454
        return weight3

