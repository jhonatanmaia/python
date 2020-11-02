def notas(* n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :paran n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    total=len(n)
    maior=max(n)
    media=sum(n)/len(n)
    if sit==False:
        return {'total':total,'maior':maior,'media':media}
    elif sit==True:
        if media>7:
            return {'total':total,'maior':maior,
                    'media':media,'situacao':'BOA'}
        elif 7<media<5:
            return {'total':total,'maior':maior,
                    'media':media,'situacao':'RAZOÁVEL'}
        else:
            return {'total':total,'maior':maior,
                    'media':media,'situacao':'RUIM'}


resp = notas(10,4,5.6,3,6.9,sit=True)
print(resp)