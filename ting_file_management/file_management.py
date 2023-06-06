import sys
""'Importa sys para gerar erros de arquivo não encontrado'""


def txt_importer(path_file):
    ""'Importa um arquivo txt e retorna seu conteúdo'""
    if not path_file.endswith('.txt'):
        sys.stderr.write("Formato inválido")
    try:

        with open(path_file, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
