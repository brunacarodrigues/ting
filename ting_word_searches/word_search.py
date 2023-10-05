def exists_word(word, instance):
    result = []

    for value in range(len(instance)):

        ocorrencias = []
        pat = instance.search(value)

    for index, linha in enumerate(pat['linhas_do_arquivo'], 1):
        if word.lower() in linha.lower():
            ocorrencias.append({'linha': index})

    if ocorrencias:
        result.append({
            'palavra': word,
            'arquivo': pat['nome_do_arquivo'],
            'ocorrencias': ocorrencias
        })

    return result


def search_by_word(word, instance):
    result = []

    for value in instance.values:
        arquivo = value["nome_do_arquivo"]
        linhas = value["linhas_do_arquivo"]

        ocorrencias = []

        for index, linha in enumerate(linhas, start=1):
            if word.lower() in linha.lower():
                ocorrencias.append({
                    "linha": index,
                    "conteudo": linha.strip()
                })

        if ocorrencias:
            result.append({
                "palavra": word,
                "arquivo": arquivo,
                "ocorrencias": ocorrencias
            })

        return result
