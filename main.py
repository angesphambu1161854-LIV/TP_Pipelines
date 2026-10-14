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
