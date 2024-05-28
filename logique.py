def modus_ponens(p_imp_q, q):
    p = p_imp_q.split('->')[0]
    if p == p_imp_q.split('->')[0]:
        return q
    else:
        return None

def modus_tollens(p_imp_q, not_q):
    p = p_imp_q.split('->')[0]
    q = p_imp_q.split('->')[1]
    if f"!{q}" == not_q:
        return f"!{p}"
    else:
        return None

def contraposition(p_imp_q):
    p, q = p_imp_q.split('->')
    contrapositive = f"!{q}->{p}"
    return contrapositive

def conjonction(p, q):
    if p.startswith("!"):
        p = f"!{p[1:]}"
    if q.startswith("!"):
        q = f"!{q[1:]}"
        
    conjunction = f"{p}^{q}"
    return conjunction


def simplification(prop):
    simplification_p = prop.split('^')
    return simplification_p

def equivalence_ou(prop):
    if "->" in prop and "!" in prop:
        _, q = prop.split("->")
        return f"p|{q.strip()}"
    else:
        return None  

def equivalence_impliq(prop):
    if "|" in prop:
        p, q = prop.split("|")
        return f"!{p.strip()}->{q.strip()}"
    else:
        return None
    
def syllogisme(premisse_majeure, premisse_mineure):
    majeure_parts = premisse_majeure.split('->')
    mineure_parts = premisse_mineure.split('->')
    
    if majeure_parts[1] == mineure_parts[0]:
        conclusion = f"{majeure_parts[0]}->{mineure_parts[1]}"
        return conclusion
    else:
        return None

def de_morgan_conjonction(prop):
    if prop.startswith("!"):
        inner_prop = prop[2:-1] if prop[2] == "(" else prop[1:]
        p, q = inner_prop.split("^")
        return [f"!{p}|!{q}"]
    else:
        return None

def de_morgan_disjonction(prop):
    if prop.startswith("!"):
        inner_prop = prop[2:-1] if prop[2] == "(" else prop[1:]
        p, q = inner_prop.split("|")
        return [f"!{p}^!{q}"]
    else:
        return None

rules = {
    'simplification': lambda p: simplification(p),
    'modus_ponens': lambda p, q: modus_ponens(p, q),
    'modus_tollens': lambda p, q: modus_tollens(p, q),
    'contraposition': lambda p, q: contraposition(p, q),
    'conjonction': lambda p, q: conjonction(p, q),
    'syllogisme': lambda p, q: syllogisme(p, q),
    'equivalence_ou': lambda p: equivalence_ou(p),
    'equivalence_impliq': lambda p: equivalence_impliq(p),
    'morgan_conjonction': lambda p: de_morgan_conjonction(p),
    'morgan_disjonction': lambda p: de_morgan_disjonction(p)
}
def determiner_etapes(input_data):
    etapes = []

    for item in input_data:
        if '->' not in item and '|' not in item:
            etapes.append(item)
        else:
            tokens = item.split('->')
            if len(tokens) == 1:
                p = tokens[0]
                etapes.append(f"simplification: {p}")
            else:
                p, q = tokens
                if '->' in item:
                    if '!' in q:
                        etapes.append(f"modus_tollens: {item}")
                    else:
                        etapes.append(f"modus_ponens: {item}")
                elif '|' in q:
                    if '!' in q:
                        etapes.append(f"morgan_disjonction: {item}")
                    else:
                        etapes.append(f"equivalence_ou: {item}")
                elif '^' in q:
                    etapes.append(f"conjonction: {item}")
                else:
                    etapes.append(f"contraposition: {item}")

    return etapes

def appliquer_regle_logique(regle, propositions, etapes_precedentes=None):
    etapes = []
    
    if regle == 'modus_ponens':
        if len(propositions) >= 2:
            p_imp_q = propositions[0]
            p = propositions[1]
            resultat = modus_ponens(p_imp_q, p)
            if resultat:
                etapes.append(f"Application de la règle du modus ponens: {resultat}")
            else:
                etapes.append("Le modus ponens ne s'applique pas.")
        else:
            etapes.append("Il n'y a pas assez de propositions pour appliquer la règle du modus ponens.")
    elif regle == 'modus_tollens':
        if len(propositions) >= 2:
            p_imp_q = propositions[0]
            not_q = propositions[1]
            resultat = modus_tollens(p_imp_q, not_q)
            if resultat:
                etapes.append(f"Application de la règle du modus tollens: {resultat}")
            else:
                etapes.append("Le modus tollens ne s'applique pas.")
        else:
            etapes.append("Il n'y a pas assez de propositions pour appliquer la règle du modus tollens.")
    elif regle == 'contraposition':
        if len(propositions) >= 1:
            if '->' in propositions[0]:
                p_imp_q = propositions[0]
                resultat = contraposition(p_imp_q)
                etapes.append(f"Contraposée de {p_imp_q}: {resultat}")
            else:
                etapes.append("La contraposition ne peut pas être appliquée.")
        else:
            etapes.append("Il n'y a pas assez de propositions pour appliquer la contraposition.")
    elif regle == 'conjonction':
        if len(propositions) >= 2:
            p = propositions[0]
            q = propositions[1]
            resultat = conjonction(p, q)
            etapes.append(f"Conjonction de {p} et {q}: {resultat}")
        else:
            etapes.append("Il n'y a pas assez de propositions pour appliquer la conjonction.")
    elif regle == 'simplification':
        if len(propositions) >= 1:
            prop = propositions[0]
            resultat = simplification(prop)
            etapes.append(f"Simplification de {prop}: {resultat}")
        else:
            etapes.append("Il n'y a pas assez de propositions pour appliquer la simplification.")
    elif regle == 'equivalence_ou':
        if len(propositions) >= 1:
            prop = propositions[0]
            resultat = equivalence_ou(prop)
            if resultat:
                etapes.append(f"Équivalence OU pour la proposition {prop}: {resultat}")
            else:
                etapes.append("La règle d'équivalence OU ne peut pas être appliquée à la proposition donnée.")
        else:
            etapes.append("Il n'y a pas assez de propositions pour appliquer l'équivalence OU.")
    elif regle == 'equivalence_impliq':
        if len(propositions) >= 1:
            prop = propositions[0]
            resultat = equivalence_impliq(prop)
            if resultat:
                etapes.append(f"Équivalence IMPLIQUE pour la proposition {prop}: {resultat}")
            else:
                etapes.append("La règle d'équivalence IMPLIQUE ne peut pas être appliquée à la proposition donnée.")
        else:
            etapes.append("Il n'y a pas assez de propositions pour appliquer l'équivalence IMPLIQUE.")
    elif regle == 'morgan_conjonction':
        if len(propositions) >= 1:
            prop = propositions[0]
            resultat = de_morgan_conjonction(prop)
            if resultat:
                etapes.append(f"Application de la règle de De Morgan pour la conjonction sur la proposition {prop}: {resultat}")
            else:
                etapes.append("La règle de De Morgan pour la conjonction ne peut pas être appliquée à la proposition donnée.")
        else:
            etapes.append("Il n'y a pas assez de propositions pour appliquer la règle de De Morgan pour la conjonction.")
    elif regle == 'morgan_disjonction':
        if len(propositions) >= 1:
            prop = propositions[0]
            resultat = de_morgan_disjonction(prop)
            if resultat:
                etapes.append(f"Application de la règle de De Morgan pour la disjonction sur la proposition {prop}: {resultat}")
            else:
                etapes.append("La règle de De Morgan pour la disjonction ne peut pas être appliquée à la proposition donnée.")
        else:
            etapes.append("Il n'y a pas assez de propositions pour appliquer la règle de De Morgan pour la disjonction.")
    elif regle == 'syllogisme':
        if len(propositions) >= 2:
            p = propositions[0]
            q = propositions[1]
            resultat = syllogisme(p, q)
            etapes.append(f"Syllogisme entre {p} et {q}: {resultat}")
        else:
            etapes.append("Il n'y a pas assez de propositions pour appliquer le syllogisme.")
    else:
        etapes.append("La règle logique spécifiée n'est pas valide.")

    # Ajouter les relations entre les étapes
    if etapes_precedentes:
        etapes[0] = f"{etapes_precedentes[-1]} => {etapes[0]}"
    
    return etapes

input_data = input_data = ['p->q', 'r->!q','r','!p']
etapes = determiner_etapes(input_data)
print("Output:")
etapes_precedentes = []
for etape in etapes:
    print(etape)
    if ': ' in etape:
        regle, parties = etape.split(': ')
        parties = parties.split(', ')
        result = appliquer_regle_logique(regle, parties, etapes_precedentes)
        if result:
            etapes_precedentes.extend(result)
            for e in result:
                print(f"  {e}")
    else:
        etapes_precedentes.append(etape)
