import collections

class Inspector:
    def __init__(self, tree_root=None, errors=None):
        """
        Initialise l'inspecteur avec la racine de l'arborescence HTML et une liste d'erreurs.
        Args:
            tree_root: Le nœud racine de l'arborescence HTML (DOM simplifié).
            errors: Une liste de dictionnaires ou d'objets représentant les erreurs détectées.
                    Chaque erreur pourrait avoir des attributs comme 'type', 'message', 'line', 'column', 'content'.
        """
        self.tree_root = tree_root
        self.errors = errors if errors is not None else []

    def set_data(self, tree_root, errors):
        """
        Met à jour les données (arborescence et erreurs) de l'inspecteur.
        Args:
            tree_root: Le nœud racine de l'arborescence HTML (DOM simplifié).
            errors: Une liste d'erreurs.
        """
        self.tree_root = tree_root
        self.errors = errors

    def _traverse_and_collect_tags(self, node, tags_list):
        """
        Fonction utilitaire récursive pour parcourir l'arborescence et collecter toutes les balises.
        """
        if node is None:
            return

        if hasattr(node, 'tag_name') and node.tag_name:
            tags_list.add(node.tag_name)

        if hasattr(node, 'children') and node.children:
            for child in node.children:
                self._traverse_and_collect_tags(child, tags_list)

    def display_all_tags(self):
        """
        Affiche toutes les balises uniques utilisées dans le document HTML.
        """
        if not self.tree_root:
            print("Aucune arborescence HTML n'est chargée.")
            return

        tags_list = set()
        self._traverse_and_collect_tags(self.tree_root, tags_list)

        if tags_list:
            print("\n--- Toutes les balises utilisées dans le document ---")
            for tag in sorted(list(tags_list)):
                print(f"- <{tag}>")
        else:
            print("Aucune balise trouvée dans le document.")

    def _print_tree_recursive(self, node, level=0):
        """
        Fonction utilitaire récursive pour afficher l'arborescence.
        """
        if node is None:
            return

        indent = "  " * level
        if hasattr(node, 'tag_name') and node.tag_name:
            print(f"{indent}<{node.tag_name}>")
            if hasattr(node, 'children') and node.children:
                for child in node.children:
                    self._print_tree_recursive(child, level + 1)
            # Afficher le contenu textuel après les enfants si la balise n'est pas auto-fermante
            if hasattr(node, 'text_content') and node.text_content and not (hasattr(node, 'is_self_closing') and node.is_self_closing):
                text_lines = node.text_content.strip().split('\n')
                for line in text_lines:
                    if line.strip(): # N'afficher que les lignes non vides
                        print(f"{indent}  {line.strip()}")
        elif hasattr(node, 'text_content') and node.text_content:
            # Pour les nœuds de texte qui ne sont pas des balises parentes
            text_lines = node.text_content.strip().split('\n')
            for line in text_lines:
                if line.strip():
                    print(f"{indent}{line.strip()}")

    def display_tag_tree(self):
        """
        Affiche l'arborescence des balises (DOM simplifié).
        """
        if not self.tree_root:
            print("Aucune arborescence HTML n'est chargée.")
            return

        print("\n--- Arborescence des balises ---")
        self._print_tree_recursive(self.tree_root)
        print("--------------------------------")

    def _find_node_by_path(self, node, path_parts, current_level=0):
        """
        Fonction utilitaire récursive pour trouver un nœud par son chemin dans l'arborescence.
        Un chemin pourrait être une liste de noms de balises, par exemple ['html', 'body', 'div', 'p'].
        """
        if node is None or current_level >= len(path_parts):
            return None

        if hasattr(node, 'tag_name') and node.tag_name == path_parts[current_level]:
            if current_level == len(path_parts) - 1:
                return node
            if hasattr(node, 'children'):
                for child in node.children:
                    found_node = self._find_node_by_path(child, path_parts, current_level + 1)
                    if found_node:
                        return found_node
        return None

    def display_tag_text_content(self, tag_path_str):
        """
        Affiche le contenu textuel d'une balise spécifique de l'arborescence.
        Args:
            tag_path_str: Une chaîne représentant le chemin de la balise, ex: "html/body/div/p".
        """
        if not self.tree_root:
            print("Aucune arborescence HTML n'est chargée.")
            return

        path_parts = tag_path_str.strip('/').split('/')
        target_node = self._find_node_by_path(self.tree_root, path_parts)

        if target_node and hasattr(target_node, 'text_content') and target_node.text_content:
            print(f"\n--- Contenu textuel de la balise '{tag_path_str}' ---")
            print(target_node.text_content.strip())
            print("-----------------------------------------------------")
        else:
            print(f"Balise '{tag_path_str}' non trouvée ou ne contient pas de texte.")

    def display_error_statistics(self):
        """
        Affiche le nombre de balises correctement et incorrectement écrites, ainsi que le taux d'erreur.
        Nécessite que le parseur et le validateur marquent les nœuds comme 'is_error'
        et que les erreurs soient passées à l'inspecteur.
        """
        if not self.tree_root:
            print("Aucune arborescence HTML n'est chargée.")
            return

        total_tags = 0
        incorrect_tags = 0

        # Compter les balises et les erreurs dans l'arborescence (si marquées sur les nœuds)
        # Ceci est un exemple simple, le validateur pourrait être plus précis.
        q = collections.deque([self.tree_root])
        while q:
            node = q.popleft()
            if hasattr(node, 'tag_name') and node.tag_name:
                total_tags += 1
                if hasattr(node, 'is_error') and node.is_error:
                    incorrect_tags += 1
            if hasattr(node, 'children'):
                for child in node.children:
                    q.append(child)

        # Si le validateur fournit une liste d'erreurs distincte, l'utiliser pour les 'incorrect_tags'
        # Plutôt que de se fier uniquement au marquage des nœuds.
        # Par exemple, si self.errors contient une liste d'objets d'erreurs distincts:
        # incorrect_tags_from_errors_list = len([err for err in self.errors if err.get('type') == 'tag_error'])
        # Le calcul ci-dessus suppose que `is_error` est mis à jour par le validateur.

        correct_tags = total_tags - incorrect_tags
        error_rate = (incorrect_tags / total_tags * 100) if total_tags > 0 else 0

        print("\n--- Statistiques des balises ---")
        print(f"Total des balises trouvées : {total_tags}")
        print(f"Balises correctement écrites : {correct_tags}")
        print(f"Balises incorrectement écrites : {incorrect_tags}")
        print(f"Taux d'erreur des balises : {error_rate:.2f}%")
        print("---------------------------------")

    def display_first_error(self):
        """
        Affiche la ligne et la colonne de la première erreur trouvée.
        """
        if not self.errors:
            print("\nAucune erreur détectée.")
            return

        first_error = self.errors[0]
        line = first_error.get('line', 'N/A')
        column = first_error.get('column', 'N/A')
        message = first_error.get('message', 'Erreur non spécifiée.')
        error_type = first_error.get('type', 'Générique')

        print("\n--- Première erreur trouvée ---")
        print(f"Type d'erreur : {error_type}")
        print(f"Ligne : {line}, Colonne : {column}")
        print(f"Message : {message}")
        print("-------------------------------")

    def display_malformed_content(self):
        """
        Affiche progressivement les portions de contenu mal écrit.
        Nécessite que les erreurs dans self.errors contiennent 'content_snippet'.
        """
        if not self.errors:
            print("\nAucune portion de contenu mal écrit détectée.")
            return

        print("\n--- Portions de contenu mal écrit ---")
        for i, error in enumerate(self.errors):
            content_snippet = error.get('content_snippet')
            line = error.get('line', 'N/A')
            column = error.get('column', 'N/A')
            message = error.get('message', 'Erreur non spécifiée.')
            error_type = error.get('type', 'Générique')

            if content_snippet:
                print(f"\nErreur #{i+1} ({error_type}) - Ligne: {line}, Colonne: {column}")
                print(f"Message: {message}")
                print("--------------------------------------------------")
                print(content_snippet.strip()) # Afficher le snippet
                print("--------------------------------------------------")
            else:
                print(f"\nErreur #{i+1} ({error_type}) - Ligne: {line}, Colonne: {column}")
                print(f"Message: {message} (Aucun extrait de contenu disponible)")
        print("\n--- Fin des portions de contenu mal écrit ---")

    def count_external_links(self):
        """
        (Bonus) Compte le nombre de liens ramenant à d'autres pages.
        Ceci nécessite de parcourir l'arborescence et d'examiner les attributs 'href' des balises 'a'.
        Une simple vérification de 'http' ou 'https' est utilisée ici pour l'externalité.
        """
        if not self.tree_root:
            print("Aucune arborescence HTML n'est chargée.")
            return

        external_link_count = 0
        q = collections.deque([self.tree_root])

        while q:
            node = q.popleft()
            if hasattr(node, 'tag_name') and node.tag_name == 'a':
                if hasattr(node, 'attributes') and node.attributes:
                    for attr in node.attributes:
                        if attr.get('name') == 'href':
                            href_value = attr.get('value', '').lower()
                            # Vérification simple pour l'externalité
                            if href_value.startswith('http://') or href_value.startswith('https://'):
                                # Une vérification plus sophistiquée pourrait inclure le domaine du document actuel
                                external_link_count += 1
                                break # On compte un lien par balise <a> valide
            if hasattr(node, 'children'):
                for child in node.children:
                    q.append(child)

        print(f"\n--- Statistiques des liens ---")
        print(f"Nombre de liens externes trouvés : {external_link_count}")
        print("----------------------------")
# --- Exemple d'utilisation (pour les tests) ---
if __name__ == "__main__":
    # Simuler une structure d'arborescence HTML simple
    class MockNode:
        def __init__(self, tag_name=None, text_content="", children=None, is_error=False, line=None, column=None, attributes=None):
            self.tag_name = tag_name
            self.text_content = text_content
            self.children = children if children is not None else []
            self.is_error = is_error
            self.line = line
            self.column = column
            self.attributes = attributes if attributes is not None else []
            self.is_self_closing = False # Pour l'exemple

    # Créons une arborescence simple
    # <html>
    #   <head>
    #     <title>Ma Page</title>
    #   </head>
    #   <body>
    #     <div>
    #       <p>Ceci est un paragraphe.</p>
    #       <p>Un autre paragraphe mal écrit.</p>
    #       <a href="http://external.com/page1">Lien externe 1</a>
    #     </div>
    #     <img src="image.jpg"> (balise auto-fermante pour l'exemple)
    #     <a href="/local/page.html">Lien local</a>
    #     <a href="https://another-external.org">Lien externe 2</a>
    #   </body>
    # </html>
    # </p>Balise P mal fermée

    p_tag1 = MockNode(tag_name="p", text_content="Ceci est un paragraphe.")
    p_tag2 = MockNode(tag_name="p", text_content="Un autre paragraphe mal écrit.", is_error=True, line=15, column=5)
    a_tag1 = MockNode(tag_name="a", text_content="Lien externe 1", attributes=[{'name': 'href', 'value': 'http://external.com/page1'}])
    div_tag = MockNode(tag_name="div", children=[p_tag1, p_tag2, a_tag1])

    img_tag = MockNode(tag_name="img", attributes=[{'name': 'src', 'value': 'image.jpg'}])
    a_tag_local = MockNode(tag_name="a", text_content="Lien local", attributes=[{'name': 'href', 'value': '/local/page.html'}])
    a_tag_external2 = MockNode(tag_name="a", text_content="Lien externe 2", attributes=[{'name': 'href', 'value': 'https://another-external.org'}])


    body_tag = MockNode(tag_name="body", children=[div_tag, img_tag, a_tag_local, a_tag_external2])
    title_tag = MockNode(tag_name="title", text_content="Ma Page")
    head_tag = MockNode(tag_name="head", children=[title_tag])
    html_root = MockNode(tag_name="html", children=[head_tag, body_tag])

    # Simuler des erreurs
    mock_errors = [
        {
            'type': 'TagError',
            'message': "Balise fermante manquante pour '<p>'",
            'line': 15,
            'column': 5,
            'content_snippet': "<p>Un autre paragraphe mal écrit."
        },
        {
            'type': 'SyntaxError',
            'message': "Chevron manquant pour '<div'",
            'line': 10,
            'column': 1,
            'content_snippet': "div>"
        },
        {
            'type': 'SpellingError',
            'message': "Balise mal orthographiée: 'boddy'",
            'line': 20,
            'column': 1,
            'content_snippet': "<boddy>"
        }
    ]



    # Instancier l'inspecteur
    inspector = Inspector(html_root, mock_errors)

    # Tester les fonctionnalités
    inspector.display_all_tags()
    print("\n" + "="*50 + "\n") # Séparateur
    inspector.display_tag_tree()
    print("\n" + "="*50 + "\n") # Séparateur
    inspector.display_tag_text_content("html/head/title")
    print("\n" + "="*50 + "\n") # Séparateur
    inspector.display_tag_text_content("html/body/div/p") # Affiche le contenu du premier p
    print("\n" + "="*50 + "\n") # Séparateur
    inspector.display_error_statistics()
    print("\n" + "="*50 + "\n") # Séparateur
    inspector.display_first_error()
    print("\n" + "="*50 + "\n") # Séparateur
    inspector.display_malformed_content()
    print("\n" + "="*50 + "\n") # Séparateur
    inspector.count_external_links()
