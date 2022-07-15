from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(instance.__len__()):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return
    imported_file = txt_importer(path_file)
    processed_file = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(imported_file),
        'linhas_do_arquivo': imported_file
    }
    instance.enqueue(processed_file)
    print(processed_file)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
