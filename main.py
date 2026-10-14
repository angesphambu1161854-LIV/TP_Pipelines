file = open("document.txt")
print(file.read())
file.close()
# r : Lecture
# a : Ajout
# w : Ecriture
# x : Création
# t : Text
# b : Binaire
# with : Gérer les cas d'erreurs et savoir quand est-ce qu'il doit arrêter l'écriture
with open("file.txt", "x") as file:
    file.write("Hello world")
with open("file.txt", "w") as file :
    file.write("AP54")

with open("file.txt", "a") as file:
    file.write("1.16 LIV")