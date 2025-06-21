# WEB_VALIDATOR_CLI.PY
Développer un validateur de pages web en ligne de commande pour identifier et potentiellement corriger les erreurs communes dans l'écriture des balises HTML (omission de balises fermantes, mauvaise orthographe, omission de chevrons, chevauchement). L'outil permettra aussi la suppression ou modification de contenu...  
Voici une explication ligne par ligne du script Python contenu dans ton fichier :

# MEMBRES
LUTONDE BYEMBA CYNTHIA
LWAMBA SALUMU GOD WISHES
MABANZA MASEKA SABRINA
MAFUTA KASONGO ISMAEL
MAGANGA FAILA SARAH

# FONCTIONNALITES
Permettre à l'utilisateur de spécifier l'URL (fichier local) d'une page web.
o Opérations d'inspection :
   Afficher toutes les balises utilisées dans le document HTML.
   Afficher l'arborescence des balises (progressivement, parents d'abord).
   Afficher le contenu textuel d'une balise spécifique de l'arborescence.
   Afficher le nombre de balises correctement et incorrectement écrites.
   Afficher la ligne et la colonne de la première erreur trouvée.
   Afficher progressivement les portions de contenu mal écrit.
o Opérations de manipulation :
   Calculer et afficher le taux d'erreur des balises mal écrites.
   Proposer une correction automatique pour une portion de contenu mal écrit.
   Permettre des corrections manuelles (ajout, suppression, modification de contenu).
o (Bonus) Compter le nombre de liens ramenant à d'autres pages.
o Analyse & Conception (Structure des données):
   Page web : URL, contenu.
   Contenu : ensemble d'éléments.
   Élément : type complexe (balise ouvrante, contenu, balise fermante) ou vide (auto-fermante); catégorie (bloc/ligne).
   Balise : peut avoir des attributs.
   Attribut : nom, valeur(s) (booléen si valeur omise et égale au nom), valeur encadrée par guillemets.

# STRUCTURE DU PROGRAMME

   html_parser.py # récuperation du chemin et lit les balises
   tag_validator.py # validateur des balises
   content_editor.py # correction automatique des erreurs
   inspector.py # affiche l'arborescence DOM
   main_cli.py # Interface utilisateur en ligne de commande

# INSTALLATION
1. Cloner le dêpot :
   git clone https://github.com:sabrina066/WED_VALIDATOR_CLI.PY
   cd WEB_VALIDATOR_CLIPY


   





