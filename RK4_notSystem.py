def runge_kutta_4(f, t0, y0, h, t_final):
    """
    Implémente la méthode de Runge-Kutta d'ordre 4 pour résoudre une équation différentielle.
    
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
        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
        t_values.append(t)
        y_values.append(y)

    return t_values, y_values


# Exemple d'utilisation
def f(t, y):
    # Exemple d'équation différentielle: y' = -y
    return -t*y +(4*t)/y


t0 = 0
y0 = 1
h = 0.25
t_final = 1

t_values, y_values = runge_kutta_4(f, t0, y0, h, t_final)

# Affichage des résultats
for t, y in zip(t_values, y_values):
    print(f"t = {t}, y = {y}")
