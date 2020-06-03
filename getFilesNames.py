import os

pasta = "C:/Users/luizc/OneDrive/Área de Trabalho/New folder/"
arquivos = os.listdir(pasta)
lista = []
palavrasChaves = ["karaoke", "cantar", "PLAYBACK"]
listaErrada = []
i = 1
with open(pasta+"ArquivosKARAOKE.txt", "w", encoding="utf-8") as f:
    for arquivo in arquivos:
        f.write(str(i)+" "+arquivo+"\n")
        lista.append(arquivo)
        i += 1
    f.close()

print()
