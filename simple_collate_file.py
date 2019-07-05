from pathlib import Path


fieldnames = ['Nome', 'Cod.Item', 'Preço','Detalhe do Produto']
data_pholder = Path('C:/Users/55199/Documents/')
file_compare_one = data_pholder/"File_compar_one.txt"
file_compare_tow = data_pholder/"File_compar_tow.txt"


with open(file_compare_one, 'r')as txt_file_one:
    with open(file_compare_tow, 'r')as txt_file_tow:

        linha1 = [ elem for elem in txt_file_one.readlines() ]
        linha2 = [elem for elem in txt_file_tow.readlines()]

        for i in range(len(linha1)):
            if linha1[i] == linha2[i]:
                print("{} igual a {}".format(linha1[i], linha2[i]))

            elif linha1[i] != linha2[i]:
                print("{} eh diferente de {}".format(linha1[i], linha2[i]))

