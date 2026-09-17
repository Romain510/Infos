classDict={
    "class":{
        "student":{
            "Mike":{
                "name":"Mike",
                "marks":{
                    "physics":70,
                    "history":80
                }
            },
            "Ted":{
                "name":"Mike",
                "marks":{
                    "physics":34,
                    "history":99
                }
            }
            
        }
    }
}

##Calcul de moyenne
def moyenne(etudiant):
    print("Ajout de le moyenne")
    moyenne=0
    for elem in classDict["class"]["student"][etudiant]["marks"]:
        moyenne+=classDict["class"]["student"][etudiant]["marks"][elem]
    moyenne=moyenne/(len(classDict["class"]["student"][etudiant]["marks"]))
    classDict["class"]["student"][etudiant]["marks"]["average"]=moyenne

def rajoutEtudiant():
    print("Ajout d'un étudiant")
    nbEt=int(input("nombre d'étudiant à rajouter"))
    for i in range(nbEt):
        etudiant=input("Nom de l'étudiant")
        classDict["class"]["student"][etudiant]={}
        classDict["class"]["student"][etudiant]["name"]=etudiant
        classDict["class"]["student"][etudiant]["marks"]={}

def ajoutNotes(etudiant):
    print("Ajout de notes")
    nbNotes=int(input("Nombre de notes à rajouter: \n"))
    for i in range(nbNotes):
        matiere=input("Quelle matière?\n")
        note=int(input("Note à ajouter: \n"))
        classDict["class"]["student"][etudiant]["marks"][matiere]=note
        

def moyenneClasse():
    moyenneCl=0
    for etud in classDict["class"]["student"]:
        moyenneCl+=classDict["class"]["student"][etud]["marks"]["average"]
    moyenneCl=moyenneCl/len(classDict["class"]["student"])
    classDict["class"]["student"]["class average"]=moyenneCl


moyenne("Mike")
moyenne("Ted")
moyenneClasse()
print(classDict["class"]["student"]["class average"])

##Ajout d'étudiant, de notes et calcul des moyennes

'''classDict={}
classDict["class"] = {}
classDict["class"]["student"] = {}'''

'''
run=True

while run:
    rajoutEt=input("Rajouter un étudiant? (o/n)\n")
    if rajoutEt=="o":
        rajoutEtudiant()

    rajoutNotes=input("Rajouter des notes? (o/n)\n")
    if rajoutNotes=="o":
        etudiant=input("Pour quel etudiant?:\n")
        ajoutNotes(etudiant)
        moyenne(etudiant)

    continuer=input("Continuer? (o/n)\n")
    if continuer=="n":
        run=False

    moyenneClasse()

    print(classDict)'''