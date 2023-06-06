import sys
""'Importa sys para gerar erros'""
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            sys.stdout.write(f"Arquivo {path_file} já está na fila\n")

    text = txt_importer(path_file)

    if text is None:
        sys.stdout.write(f"Arquivo {path_file} não encontrado\n")

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text),
        "linhas_do_arquivo": text
    }

    instance.enqueue(data)
    sys.stdout.write(str(data))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
