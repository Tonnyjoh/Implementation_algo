def rob_implie(lst):
    """Convertit les implications en disjonctions, y compris les conclusions complexes."""
    if len(lst) >= 3 and lst[1] == "->":
        premise = lst[0]
        if premise.startswith('!'):
            new_premise = premise[1:]  # Retirer la négation
        else:
            new_premise = f"!{premise}"  # Ajouter une négation
        conclusion = lst[2].replace("(", "").replace(")", "").split("&&")
        new_clause = [new_premise] + [item.strip() for item in conclusion]
        return new_clause
    return lst

def transform(lst_list):
    """Transforme toutes les implications en disjonctions dans la liste d'argumentation."""
    transformed_list = []
    for lst in lst_list:
        transformed_list.append(rob_implie(lst))
    return transformed_list

def flatten_clause(clause):
    """Aplatit une clause en gérant les conjonctions et disjonctions."""
    new_clauses = []
    current_clause = []

    for token in clause:
        if token == '&&':
            if current_clause:
                new_clauses.append(current_clause)
                current_clause = []
        elif token == '||':
            continue
        else:
            current_clause.append(token)

    if current_clause:
        new_clauses.append(current_clause)

    return new_clauses

def create_newlist(lst_list):
    """Fusionne les listes d'argumentation en une seule liste sans les opérateurs '||'."""
    new_list = []
    for lst in lst_list:
        new_list.extend(flatten_clause(lst))
    return [item for sublist in new_list for item in sublist]

def eliminer_complementaires(liste):
    """Élimine les éléments complémentaires de la liste (p et !p)."""
    positifs = set()
    negatifs = set()
    for element in liste:
        if element.startswith('!'):
            negatifs.add(element[1:])
        else:
            positifs.add(element)

    complements = positifs.intersection(negatifs)
    
    resultat = [element for element in liste if (element.startswith('!') and element[1:] not in complements) or (not element.startswith('!') and element not in complements)]
    
    return resultat

def simplifier_negations(liste):
    """Élimine les négations doubles de la liste (!!p devient p)."""
    return [item[1:] if item.startswith("!!") else item for item in liste]

def robinson_method(argumentations, conclusion):
    """Applique la méthode de Robinson pour vérifier la validité des argumentation."""
    # Étape 1 : Transformation des implications
    argumentations = transform(argumentations)
    
    # Étape 2 : Fusionner les listes en une seule liste
    args = create_newlist(argumentations)
    
    # Étape 3 : Éliminer les complémentaires
    args = eliminer_complementaires(args)
    
    # Étape 4 : Simplifier les négations
    args = simplifier_negations(args)
    
    # Afficher les arguments transformés
    print("Arguments transformés:", args)
    
    # Étape 5 : Transformation de la conclusion
    conclusion = rob_implie(conclusion)
    conclusion = create_newlist([conclusion])
    conclusion = simplifier_negations(conclusion)
    print("Conclusion transformée:", conclusion)
    
    # Vérifier si la conclusion est dérivable des prémisses
    if all(item in args for item in conclusion):
        print("L'argumentation est correcte")
    else:
        print("L'argumentation n'est pas correcte")

# Exemples d'utilisation
c1 = ["p", "->", "q"]
c2 = ["q", "->", "(r && s)"]
c3 = ["!r", "||", "(!t || u)"]
c4 = ["p", "&&", "t"]

conclusion = ["u"]
argumentations = [c1, c2, c3, c4]

robinson_method(argumentations, conclusion)
