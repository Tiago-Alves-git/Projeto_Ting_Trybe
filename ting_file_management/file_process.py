from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file, instance: Queue):
    """Aqui irá sua implementação"""
    for index in range(len(instance)):
        if path_file == instance.search(index)["nome_do_arquivo"]:
            return None

    linhas = txt_importer(path_file)

    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(linhas),
        "linhas_do_arquivo": linhas,
    }

    instance.enqueue(new_dict)

    sys.stdout.write(str(new_dict))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# {
#     "nome_do_arquivo": "arquivo_teste.txt", Caminho do arquivo
#     "qtd_linhas": 3, Quantidade de linhas existentes no arquivo
#     "linhas_do_arquivo": [...] linhas retornadas pela função do requisito 2
# }
