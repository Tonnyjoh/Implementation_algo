# #methode de Robinson version 1.0.0
# def rob_implie(list):
#     if len(list)>=3 and list[1]=="->":
#         list[0]=f"!{list[0]}"
#         list[1]="||"
#     return list
# def transform(list):
#     for lst in list:
#         lst=rob_implie(lst)
#     return list
# def create_newlist(list):
#     new_list=[]
#     for lst in list:
#         for ls in lst:
#             new_list.append(ls)
#     while new_list.count("||")>0:
#         new_list.remove("||")        
#     return new_list
# def eliminer_complementaires(liste):
#     positifs = set()
#     negatifs = set()
#     for element in liste:
#         if element.startswith('!'):
#             negatifs.add(element[1:])
#         else:
#             positifs.add(element)

#     complements = positifs.intersection(negatifs)

#     resultat = [element for element in liste if (element.startswith('!') and element[1:] not in complements) or (not element.startswith('!') and element not in complements)]

#     return resultat

# c1=["p","->","q"]
# c2=["q","->","r"]
# c4=["p"]
# conclusion=["r"]
# argumentation=[c1,c2,c4]
# # print(argumentation)
# argumentation=transform(argumentation)
# args=eliminer_complementaires(create_newlist(argumentation))
# print(args)

# if args and args[0] == conclusion[0]:
#     print("l'argumentation est correcte")
# else:
#     print("l'argumentation n'est pas correcte")
#version 1.0.1
def rob_implies(lst):
    """Convertit les implications en disjonctions, y compris les conclusions complexes."""
    if len(lst) >= 3 and lst[1] == "->":
        premise = lst[0]
        if premise.startswith('!'):
            new_premise = premise[1:]  # Retirer la négation
        else:
            new_premise = f"!{premise}"  # Ajouter une négation
        conclusion = lst[2].split("||")
        new_clause = [new_premise] + [item.strip() for item in conclusion]
        return new_clause
    return lst


def transform(lst_list):
    """Transforme toutes les implications en disjonctions dans la liste d'argumentation."""
    transformed_list = []
    for lst in lst_list:
        transformed_list.append(rob_implies(lst))
    return transformed_list


def create_newlist(list):
    """Fusionne les listes d'argumentation en une seule liste sans les opérateurs '||'."""
    new_list = []
    for lst in list:
        for ls in lst:
            new_list.append(ls)
    while new_list.count("||") > 0:
        new_list.remove("||")
    while new_list.count("&&") > 0:
        new_list.remove("&&")
    for elt in new_list:
        if len(elt) >= 3:
            if elt.count("||") > 0:
                new_elt = elt.split("||")
                new_list.extend(new_elt)
                new_list.remove(elt)
            if elt.count("&&") > 0:
                new_elt = elt.split("&&")
                new_list.extend(new_elt)
                new_list.remove(elt)
    #print(new_list)
    return new_list


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

    resultat = [element for element in liste if (element.startswith('!') and element[1:] not in complements) or (
                not element.startswith('!') and element not in complements)]

    return resultat


def robinson_method(argumentations, conclusion):
    """Applique la méthode de Robinson pour vérifier la validité des argumentation."""
    argumentations = transform(argumentations)

    args = create_newlist(argumentations)

    args = eliminer_complementaires(args)

    print("Arguments transformés:", args)

    if args and conclusion[0] in args:
        print("L'argumentation est correcte")
    else:
        print("L'argumentation n'est pas correcte")


"""Exercise 2"""
# c1 = ["p", "->", "r"]
# c2 = ["r", "->", "s"]
# c3 = ["t", "||", "!s"]
# c4 = ["!t","||", "u"]
# c5 = ["!u"]

# conclusion = ["!p"]
# argumentation = [c1, c2, c3,c4,c5]

"""Exercise 3"""
# c1 = ["p", "->", "r"]
# c2 = ["!p", "->", "q"]
# c3 = ["q", "->", "s"]

# conclusion = ["!r", "->", "s"]
# argumentation = [c1, c2, c3]

"""Exercise 4"""
# c1 = ["p", "->", "q"]
# c2 = ["q", "->", "r&&s"]
# c3 = ["!r", "||", "!t||u"]
# c4 = ["p","&&","t"]

# conclusion = ["u"]
# argumentation = [c1, c2, c3,c4]
c0 = ["q", "->", "r"]  # p -> (q -> r) pas pris en compte
c1 = ["!p"]
c1.extend(rob_implies(c0))
c2 = ["p", "||", "s"]
c3 = ["t", "->", "q"]
c4 = ["!s"]

conclusion = ["!r", "->", "!t"]
argumentation = [c1, c2, c3, c4]

print(f"Conclusion: {rob_implies(conclusion)}")
robinson_method(argumentation, rob_implies(conclusion))
