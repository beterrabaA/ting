def exists_word(word, instance):
    arquivo = instance.search(0)
    retorno = [{
        "palavra": word,
        "arquivo": arquivo["nome_do_arquivo"],
        "ocorrencias": []
    }]
    word_lower = word.lower()
    for index, linha in enumerate(arquivo["linhas_do_arquivo"]):
        lowerd = linha.lower()
        if word_lower in lowerd:
            retorno[0]["ocorrencias"].append({"linha": index + 1})
    if len(retorno[0]["ocorrencias"]) == 0:
        retorno = []
    return retorno


def search_by_word(word, instance):
    words_filed = exists_word(word, instance)
    if len(words_filed) == 0:
        return []
    arquivo = instance.search(0)
    for index, ocorrencia in enumerate(words_filed[0]["ocorrencias"]):
        ocorrenced_content = words_filed[0]["ocorrencias"]
        ocorrenced_line = arquivo["linhas_do_arquivo"][ocorrencia["linha"] - 1]
        ocorrenced_content[index]["conteudo"] = ocorrenced_line
    return words_filed
