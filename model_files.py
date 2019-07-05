class Model_files(object):

    def __init__(self):

        self.__itens = []

    def obter_itens(self):
        return tuple(self.__itens)

    def add_item(self, item):
        self.__itens.append(item)


class Item(object):

    def __init__(self, nome ):
        self.__nome = nome


class Item_Result_Equal(object):

    def __init__(self, nome ):
        self.__nome = nome          

class Item_Result_Not_Equal(object):

    def __init__(self, nome ):
        self.__nome = nome
