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


def remove(instance: Queue):
    """Aqui irá sua implementação"""

    item_removed = instance.dequeue()

    if item_removed is None:
        print("Não há elementos")
    else:
        print(
          f"Arquivo {item_removed['nome_do_arquivo']} removido com sucesso"
        )


def file_metadata(instance: Queue, position):
    """Aqui irá sua implementação"""
    try:
        searched = instance.search(position)
        print(searched)
    except IndexError:
        sys.stderr.write("Posição inválida\n")
