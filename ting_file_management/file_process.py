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
    try:
        removed_item = instance.dequeue()
        return print(
            f"Arquivo {removed_item['nome_do_arquivo']} removido com sucesso\n"
            )
    except IndexError:
        print('Não há elementos')


def file_metadata(instance, position):
    try:
        item = instance.search(position)
        return sys.stdout.write(f'{item}\n')
    except IndexError:
        sys.stderr.write('Posição inválida\n')
