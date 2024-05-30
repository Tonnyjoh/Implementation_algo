def rob_implie(list):
    if len(list)>=3 and list[1]=="->":
        list[0]=f"!{list[0]}"
        list[1]="||"
    return list
def transform(list):
    for lst in list:
        lst=rob_implie(lst)
    return list
def create_newlist(list):
    new_list=[]
    for lst in list:
        for ls in lst:
            new_list.append(ls)
    while new_list.count("||")>0:
        new_list.remove("||")        
    return new_list
def eliminer_complementaires(liste):
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
      
c1=["p","->","q"]
c2=["q","->","r"]
c4=["p"]
conclusion=["r"]
argumentations=[c1,c2,c4]
# print(argumentations)
argumentations=transform(argumentations)
args=eliminer_complementaires(create_newlist(argumentations))
print(args)

if args[0]==conclusion[0]:
    print("l'argumentation est correcte")