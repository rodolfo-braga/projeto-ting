def exists_word(word, instance):
    search = []
    for i in range(instance.__len__()):
        file = instance.search(i)
        occurrences = []
        file_lines = file['linhas_do_arquivo']
        number_of_lines = len(file_lines)
        for line in range(number_of_lines):
            if word.lower() in file_lines[line].lower():
                occurrences.append({
                    'linha': line + 1,
                })
        if len(occurrences) > 0:
            search.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': occurrences
            })
    return search


def search_by_word(word, instance):
    search = []
    for i in range(instance.__len__()):
        file = instance.search(i)
        occurrences = []
        file_lines = file['linhas_do_arquivo']
        number_of_lines = len(file_lines)
        for line in range(number_of_lines):
            if word.lower() in file_lines[line].lower():
                occurrences.append({
                    'linha': line + 1,
                    'conteudo': file_lines[line]
                })
        if len(occurrences) > 0:
            search.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': occurrences
            })
    return search
