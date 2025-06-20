    import os
import re
# fonction pour lire un fichier
def lire_fichier_html (filepath):
    with open(filepath, 'r', encoding= 'utf -8') as f:
        return f.read()
    
    
# fonction symbole html
def symbole_html(html):
    modele = re.compile(r"<[^>]+>|[^<>]+")
    return modele.findall(html)

# fonction pour analyser html
def analyser_html(balises):
    empiler = []
    tree = []
    current = []
    
    for balise in balises:
        if balise.startswith("<"):
            if balise.startswith("</"):
                if empiler:
                    empiler.pop()
                    if empiler:
                        current = empiler[-1][1]
                    else:
                        current = tree
            elif balise.endswtih("/>"):
                current.append((balise , []))
        
            else:
                new_mode =(balise, [])
                current.append(new_mode)
                empiler.append(new_mode)
                current = new_mode[1]
        else:
            if balise.strip():
                current.append(("Text", balise.strip()))
    
    return tree
# fonction pour representer l'arbre
def representer_arbre(arbre, indent=0):
    for balise, contenu in arbre:
        print(" " * indent + balise)
        if contenu:
            representer_arbre(contenu, indent + 2)
        else:
            print(" " * (indent + 2) + "(vide)")
