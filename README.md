# WEB_VALIDATOR_CLI.PY
Développer un validateur de pages web en ligne de commande pour identifier et potentiellement corriger les erreurs communes dans l'écriture des balises HTML (omission de balises fermantes, mauvaise orthographe, omission de chevrons, chevauchement). L'outil permettra aussi la suppression ou modification de contenu...  
Voici une explication ligne par ligne du script Python contenu dans ton fichier :



import re

➡️ Importe le module re qui sert à faire des recherches avec des expressions régulières (par exemple, pour détecter les balises HTML dans le texte).



class content_editor:

➡️ Déclare une classe appelée content_editor qui va gérer du texte enrichi avec des balises HTML de base (<p>, <b>, <i>, etc.).



def __init__(self):

➡️ Méthode constructeur appelée automatiquement lors de la création d’un objet content_editor.



self.content = ""

➡️ Initialise le contenu texte comme une chaîne vide.




self.valid_tags =["<p>","</p>","<b>","</b>","<i>","</i>"]

➡️ Définit une liste de balises HTML autorisées.



def add_content(self, text):

➡️ Méthode pour ajouter du contenu texte.



self.content += text

➡️ Ajoute le texte donné à self.content.


self.check_validity()

➡️ Appelle la méthode check_validity() pour vérifier si les balises sont bien utilisées.




def remove_content(self, text):

➡️ Méthode pour supprimer un texte donné du contenu.




   self.content = self.content.replace(text,"")

➡️ Supprime toutes les occurrences du texte donné.




self.check_validity()

➡️ Vérifie les balises après modification.




def modify_content(self, old_text, new_text):

➡️ Méthode pour remplacer un ancien texte par un nouveau 


 self.content = self.content.replace(old_text,new_text)
 self.check_validity()

➡️ Remplace le texte et vérifie les balises.


def check_validity(self):

➡️ Méthode pour vérifier la validité des balises HTML dans le contenu.


 open_tags =[]

➡️ Initialise une pile open_tags pour suivre les balises ouvertes.



for tag in re.findall(r'</?\w+>',self.content):

➡️ Utilise une expression régulière pour trouver toutes les balises HTML (ouverture/fermeture) dans le texte.


if tag in self.valid_tags:

➡️ Ignore les balises non valides.



if not tag.startswith('<') and tag("/"):

➡️  Vérifier si la balise est fermante.



open_tags.append(tag)

➡️ Cette ligne est incorrecte même si elle était atteinte. Une balise fermante ne devrait pas être ajoutée à open_tags.




else:
                    if open_tags and f"<{tag[2:]}" == open_tags[-1]:
                        open_tags.pop()
                    else:
                        print(f"Erreur: Balise fermante {tag} non fermée", open_tags)

➡️ Cette partie essaie de vérifier si les balises sont correctement fermées, mais le code ne gère pas bien la pile.


def simple_spell_check(self,word):

➡️ Méthode pour vérifier l'orthographe d’un mot de manière simplifiée.


dictionary = ['exemple', "Modifier"]
return word in dictionary

➡️ Compare le mot à une petite liste (dictionary) de mots supposés corrects.



def correct_spelling(self):

➡️ Méthode pour signaler les mots mal orthographiés.


  words = self.content.split()

➡️ Sépare le contenu en mots.



for word in words:
            if not self.simple_spell_check(word):
                print("Erreur d'orthographe trouvée: {word}")

➡️ Affiche un message pour chaque mot non reconnu


Utilisation de la classe

editor = content_editor()

➡️Crée une instance de la classe content_editor.



editor.add_content("<p>Ceci est un exemple de text.</p>")

➡️ Ajoute un paragraphe avec une faute : "text" au lieu de "texte".



editor.add_content("<b>Text en gras </b>")

➡️ Ajoute un texte en gras, avec toujours "Text" incorrect.



editor.remove_content("Exemple")

➡️ Supprime le mot "Exemple", mais ce mot n'existe pas tel quel (avec majuscule) → rien ne se passe.


editor.modify_content("Text en gras","<i>Text en italic </i>")

➡️ Remplace le texte en gras par un texte en italique.


editor.correct_spelling()

➡️ Parcourt chaque mot et signale ceux qui ne sont pas dans le dictionnaire simplifié.






