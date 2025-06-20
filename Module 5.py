#Module 5
import os
def menu_principal():
    print("== Menu Principal ==")
    print("1. Charger")
    print("2. Afficher le contenu du fichier")
    print("3. Sauvegader les modifications dans un nouveau fichier")
    print("4. Quitter")
def telecharger_fichier():
    url_fichier = input("Entrez l'url du fichier à charger:")
    if os.path.isfile(url_fichier):
        with open(url_fichier, 'r') as fichier:
            contenu = fichier.read()
            print("Fichier chargé avec succès.")
            return contenu
    else:
        print("Le fichier n'existe pas, veillez réessayez.")
        return None

def display_content(content):
    if content is not None:
        print("\n=== Contentu du fichier ===")
        print(content)
    else:
        print("Aucun contenu à afficher.")
    
def sauvegarder_fichier(contenu):
    if contenu is not None:
        nouvelle_url_fichier = input("Entrez le nom du nouveau fichier pour sauvegader les modifications:")
        with open(nouvelle_url_fichier, "w") as fichier:
            fichier.write(contenu)
            print("Modification sauvegardée dans",nouvelle_url_fichier)
    else:
        print("Aucun contenu à saugarder.")

def principal():
    contenu = None
    while True:
        menu_principal()
        choix = input("Choisissez une option:")
        if choix == "1":
            contenu =  telecharger_fichier()
        elif choix == "2":
            display_content(contenu)
        elif choix == "3":
            sauvegarder_fichier(contenu) 
        elif choix == "4": 
            print("Aurevoir!")
            break
        else:
            print("Option invalide, veillez réesayez>.")
if __name__ == "__main__":
    principal() 














