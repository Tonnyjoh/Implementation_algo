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
# argumentations=[c1,c2,c4]
# # print(argumentations)
# argumentations=transform(argumentations)
# args=eliminer_complementaires(create_newlist(argumentations))
# print(args)

# if args and args[0] == conclusion[0]:
#     print("l'argumentation est correcte")
# else:
#     print("l'argumentation n'est pas correcte")
def rob_implie(lst):
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
    """Transforme toutes les implications en disjonctions dans la liste d'argumentations."""
    transformed_list = []
    for lst in lst_list:
        transformed_list.append(rob_implie(lst))
    return transformed_list

def create_newlist(list):
    """Fusionne les listes d'argumentations en une seule liste sans les opérateurs '||'."""
    new_list=[]
    for lst in list:
        for ls in lst:
            new_list.append(ls)
    while new_list.count("||")>0:
        new_list.remove("||")        
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
    
    resultat = [element for element in liste if (element.startswith('!') and element[1:] not in complements) or (not element.startswith('!') and element not in complements)]
    
    return resultat

def robinson_method(argumentations, conclusion):
    """Applique la méthode de Robinson pour vérifier la validité des argumentations."""
    argumentations = transform(argumentations)
    
    args = create_newlist(argumentations)
    
    args = eliminer_complementaires(args)
    
    print("Arguments transformés:", args)
    
    if args and conclusion[0] in args:
        print("L'argumentation est correcte")
    else:
        print("L'argumentation n'est pas correcte")

c1 = ["p", "->", "r"]
c2 = ["!p", "->", "q"]
c3 = ["q", "->", "s"]

conclusion = ["!r", "->", "s"]
argumentations = [c1, c2, c3]
print(rob_implie(conclusion))
robinson_method(argumentations, rob_implie(conclusion))
    