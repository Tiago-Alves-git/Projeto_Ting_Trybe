from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    """Aqui irá sua implementação"""

    queue_list = list(instance.queue)
    result = []

    # Itera sobre cada objeto na fila
    for obj in queue_list:
        file_name = obj['nome_do_arquivo']
        lines = obj['linhas_do_arquivo']
        occurrences = []

        # Itera sobre as linhas do arquivo
        for line_number, line in enumerate(lines, start=1):
            # Verifica se a palavra (ignorando maiúsculas/minúsculas)
            if word.lower() in line.lower():
                occurrences.append({"linha": line_number})

        # Se ocorrencias não estiver vazio, adiciona à lista de resultados
        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })

    return result


def search_by_word(word, instance: Queue):
    """Aqui irá sua implementação"""
    queue_list = list(instance.queue)
    result = []

    # Itera sobre cada objeto na fila
    for obj in queue_list:
        file_name = obj['nome_do_arquivo']
        lines = obj['linhas_do_arquivo']
        occurrences = []

        # Itera sobre as linhas do arquivo
        for line_number, line in enumerate(lines, start=1):
            # Verifica se a palavra (ignorando maiúsculas/minúsculas)
            if word.lower() in line.lower():
                occurrences.append({
                    "linha": line_number,
                    "conteudo": line
                })

        # Se ocorrencias não estiver vazio, adiciona à lista de resultados
        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })

    return result
