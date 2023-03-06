nota = float(input("Informe sua nota 1:"))
nota2 = float(input("Informe sua nota 2:"))
nota3 = float(input("Informe sua nota 3:"))

media = (nota + nota2 + nota3) /3

if media >=7:
    print("Aprovado" + str (media))
elif media >=5 or media = 6.9:
    print("Recuperação =" + str(media))
else:
    print (Reprovou)
