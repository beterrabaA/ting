import sys
""'Importa sys para gerar erros'""
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    text = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text),
        "linhas_do_arquivo": text
    }

    instance.enqueue(data)
    sys.stdout.write(str(data))


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")

    filed = instance.dequeue()
    sys.stdout.write(
        f"Arquivo {filed['nome_do_arquivo']} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        sys.stdout.write(str(instance.search(position)))
    except IndexError:
        sys.stderr.write("Posição inválida")
