
from make_collate import Compare_equals, Compare_not_equals, Nothing_compare
from pathlib import Path


class Compare_of_files(object):

    def compare(self, model_files):

        return Compare_equals(
            Compare_not_equals(
                Nothing_compare()
            )
        ).compare(model_files)

if __name__ == "__main__":

    from model_files import Model_files, Item

    model_files = Model_files()

    data_pholder = Path('C:/Users/55199/Documents/')
    file_compare_one = data_pholder/"File_compar_one.txt"
    file_compare_tow = data_pholder/"File_compar_tow.txt"
    linha1 = []
    linha2 = []
    with open(file_compare_one, 'r')as txt_file_one:
        with open(file_compare_tow, 'r')as txt_file_tow:
            linha1 = [ elem for elem in txt_file_one.readlines() ]
            linha2 = [elem for elem in txt_file_tow.readlines()]

    model_files.add_item(Item(linha1))
    model_files.add_item(Item(linha2))

    comparetor = Compare_of_files()

    comparetor.compare(model_files)
    model_files._Model_files__itens[2]._Item_Result_Equal__nome
    model_files._Model_files__itens[3]._Item_Result_Not_Equal__nome
