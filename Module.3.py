import re

class content_editor:
    def __init__(self):
        self.content = ""
        self.valid_tags =["<p>","</p>","<b>","</b>","<i>","</i>"]
    def add_content(self, text):
        '''Ajout du contenu textuel.'''
        self.content += text
        self.check_validity()
    def remove_content(self, text):
        '''supprimer du contenu textuel.'''
        self.content = self.content.replace(text,"")
        self.check_validity()
    def modify_content(self, old_text, new_text):
        '''Modifier du contenu textuel.'''
        self.content = self.content.replace(old_text,new_text)
        self.check_validity()
    def check_validity(self):
        '''Verifier la validite des balises.'''
        open_tags =[]
        for tag in re.findall(r'</?\w+>',self.content):
            if tag in self.valid_tags:
                if not tag.startswith('<') and tag("/"):
                    open_tags.append(tag)
                else:
                    if open_tags and f"<{tag[2:]}" == open_tags[-1]:
                        open_tags.pop()
                    else:
                        print(f"Erreur: Balise fermante {tag} non fermée", open_tags)
    def simple_spell_check(self,word):
        '''Verifie si un mot est mal écrit (exemple simpliste).'''
        dictionary = ['exemple', "Modifier"]
        return word in dictionary
    def correct_spelling(self):
        '''Corrige les mots mal arthographiés dans le contenu.'''
        words = self.content.split()
        for word in words:
            if not self.simple_spell_check(word):
                print("Erreur d'orthographe trouvée: {word}")
#Utilisation du module
editor = content_editor()
editor.add_content("<p>Ceci est un exemple de text.</p>")
editor.add_content("<b>Text en gras </b>")
editor.remove_content("Exemple")
editor.modify_content("Text en gras","<i>Text en italic </i>")
editor.correct_spelling()



# Validateur balise <form> </form>
def validateur_form():
    form = ['<form>','</form>']
    for i in form: 
        if form [0] == '<form>' and form [-1] == '</form>':
            break
        else:
            print ("La balise '<form>','</form>' est invalide")
            break

# Validateur balise <fielset></fielset>
def validateur_fielset():
    fielset = ['<fielset>','</fielset>']
    for i in fielset:
        if fielset [0] ==  '<fielset>' and fielset [-1] == '</fielset>':
            break
        else:
            print ("La balise '<fielset>','</fielset>' est invalide ")
            break

# Validateur balise <label></label>
def validateur_label():
    label = ['<label>','</label>']
    for i in label:
        if label [0] == '<label>' and  label [-1] == '</label>':
            break
        else:
            print ("La balise '<label>','</label>' est invalide ")
            break

# Validateur balise <legend>,</legend>
def validateur_legend():
    legend = ['<legend>','</legend>']
    for i in legend:
        if legend [0] == '<legend>' and legend [-1] == '</legend>':
            break
        else:
            print ("La balise  <legend>,</legend> est invalide")
            break
# Validateur balise <aside>,</aside>
def validateur_aside():
    aside = ['<aside>','</aside>']
    for i in aside:
        if aside[0] == '<aside>' and aside [-1] == '</aside>':
            break
        else:
            print ("La balise '<aside>','</aside> est invalide")
            break

# Validateur balise <footer>,</footer>
def validateur_footer():
    footer = ['<footer>','</footer>']
    for i in footer:
        if footer [0] == '<footer>' and footer [-1] == '</footer>':
            break
        else:
            print ("La balise '<footer>','</footer> est invalide")
            break



