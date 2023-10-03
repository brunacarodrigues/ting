from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if any(item['nome_do_arquivo'] == path_file for item in instance.values):
        print(f'O arquivo {path_file} já foi processado anteriormente.')
        return

    linhas = txt_importer(path_file)

    data_process = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(linhas),
        'linhas_do_arquivo': linhas
    }

    instance.enqueue(data_process)

    return sys.stdout.write(f'{data_process}\n')


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
