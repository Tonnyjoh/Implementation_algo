def euler_method(f, t0, y0, h, t_final):
    """
    Implémente la méthode d'Euler pour résoudre une équation différentielle.
    
    :param f: Fonction représentant l'équation différentielle, f(t, y).
    :param t0: Temps initial.
    :param y0: Valeur initiale de y.
    :param h: Étape de temps.
    :param t_final: Temps final de l'intervalle de simulation.
    :return: Liste des valeurs approximatives de y à chaque étape de temps.
    """
    t = t0
    y = y0
    t_values = [t]
    y_values = [y]

    while t < t_final:
        y += h * f(t, y)
        t += h
        t_values.append(t)
        y_values.append(y)

    return t_values, y_values


# Exemple d'utilisationnn
def f(t, y):
    # Exemple d'équation différentielle: y' = -y
    return -t*y +(4*t)/y


t0 = 0
y0 = 1
h = 0.25
t_final = 1

t_values, y_values = euler_method(f, t0, y0, h, t_final)

# Affichage des résultats
for t, y in zip(t_values, y_values):
    print(f"t = {t}, y = {y}")
