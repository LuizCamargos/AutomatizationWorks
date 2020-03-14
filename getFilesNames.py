import os

pasta = "C:/VIDEOS/KARAOKE/"
arquivos = os.listdir(pasta)
lista = []
palavrasChaves = ["karaoke", "cantar", "PLAYBACK"]
listaErrada = []
i = 1
with open("ArquivosKARAOKE.txt", "w", encoding="utf-8") as f:
    for arquivo in arquivos:
        f.write(str(i)+" "+arquivo+"\n")
        lista.append(arquivo)
        i += 1
    f.close()
for nome in lista:
    i = 0
    nome = nome.lower()
    if (nome.find("karaokê") == -1):
        i += 1
    if (nome.find("karaoke") == -1):
        i += 1
    if i > 0:
        print(nome)
        listaErrada.append(nome)
with open("ArquivosKARAOKEERRADA.txt", "w", encoding="utf-8") as f:
    for arquivo in listaErrada:
        f.write(arquivo+"\n")
    f.close()
