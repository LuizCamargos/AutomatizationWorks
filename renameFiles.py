import os
i = 1
# exemplo alterado de  EX_10.5.py para 10_5.py
listaNova = []
pasta = "E:\\KARAOKE\\"
for nome in os.listdir(pasta):
    # alterar conforme sua necessidade de geração de nomes e layout de arquivos
    novo = pasta+str(i)+" "+nome
    os.rename(pasta+nome, novo)
    print("arquivo " + nome + " alterado para " + novo)
    i += 1
    listaNova.append(novo)
with open("ArquivosKARAOKE.txt", "w", encoding="utf-8") as f:
    for arquivo in listaNova:
        f.write(arquivo+"\n")
    f.close()
