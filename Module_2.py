import re

liste_balises_valide = {"html","head","body","title","div","p","span","a","ul","li","br","img"}

def validation_balises(input_chaine):
    detection_balises = re.compile(r"</?([a-zA-Z0-9]+)[^>]*>")
    ordre_elements=[]
    erreur=[]

    for resultat_recherche in detection_balises.finditer(input_chaine):
        balises = resultat_recherche.group(1)
        test_balise_complete = resultat_recherche.group(0)
        position = resultat_recherche.start()

        if balises not in liste_balises_valide:
            erreur.append((f"Tag invalide:<{balises}>",position))
            continue

        if test_balise_complete.startswith("</"): # balise fermante
                if not ordre_elements or ordre_elements[-1]!=balises:erreur.append((f"Balise fermante inattendue</{balises}>",position))
                else:
                    ordre_elements.pop()
        else: #balise ouvrannte 
             ordre_elements.append(balises)

    if ordre_elements:
        erreur.append((f"Balise non fermée:<{ordre_elements[-1]}>",input_chaine.rfind(ordre_elements[-1])))

    if not erreur:
        return"✔Toutes les balises sont valides."
    else:
        return "\n".join([f"Erreur à la position{pos} : {msg}" for msg,pos in erreur]) 
 #Exempled'utilisation
html_code="<html><head><title>Test</title></head><body><div><p>Bonjour</div></body></html>"
print(validation_balises(html_code))

        
        
            
    

    
        
        
    
