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
    """"Implemente a sua função aqui"""
