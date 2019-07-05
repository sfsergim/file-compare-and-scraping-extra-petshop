from pathlib import Path
from Model_files import  Item_Result_Equal,Item_Result_Not_Equal

class Compare_equals(object):

    def __init__(self, next_compare):

        self.__next_compare = next_compare

    def compare(self, model_files):
        result = []
        for j in range(len(model_files._Model_files__itens[0]._Item__nome)):
            if model_files._Model_files__itens[0]._Item__nome[j] == model_files._Model_files__itens[1]._Item__nome[j]:
                result.append("{} Is equal to {}".format(model_files._Model_files__itens[0]._Item__nome[j], model_files._Model_files__itens[1]._Item__nome[j]))
               
        model_files.add_item(Item_Result_Equal(result))
        return self.__next_compare.compare(model_files)


class Compare_not_equals(object):

    def __init__(self, next_compare):

        self.__next_compare = next_compare

    def compare(self, model_files):
        result = []
        for j in range(len(model_files._Model_files__itens[0]._Item__nome)):
            if model_files._Model_files__itens[0]._Item__nome[j] != model_files._Model_files__itens[1]._Item__nome[j]:
                result.append("{} Not equal to {}".format(model_files._Model_files__itens[0]._Item__nome[j], model_files._Model_files__itens[1]._Item__nome[j]))
               
        model_files.add_item(Item_Result_Not_Equal(result))
        return self.__next_compare.compare(model_files)

class Nothing_compare(object):

    def compare(self, model_files):
        return 0