def runge_kutta_4_system(f, g, t0, x0, y0, h, t_final):
    """
    Implémente la méthode de Runge-Kutta d'ordre 4 pour un système d'équations différentielles du premier ordre.
    
    :param f: Fonction représentant la première équation différentielle, f(t, x, y).
    :param g: Fonction représentant la deuxième équation différentielle, g(t, x, y).
    :param t0: Temps initial.
    :param x0: Valeur initiale de x.
    :param y0: Valeur initiale de y.
    :param h: Étape de temps.
    :param t_final: Temps final de l'intervalle de simulation.
    :return: Liste des valeurs approximatives de x et y à chaque étape de temps.
    """
    t = t0
    x = x0
    y = y0
    t_values = [t]
    x_values = [x]
    y_values = [y]
    
    while t < t_final:
        k1_x, k1_y = f(t, x, y)
        k2_x, k2_y = f(t + h/2, x + k1_x/2, y + k1_y/2)
        k3_x, k3_y = f(t + h/2, x + k2_x/2, y + k2_y/2)
        k4_x, k4_y = f(t + h, x + k3_x, y + k3_y)
        
        x += (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6
        y += (k1_y + 2*k2_y + 2*k3_y + k4_y) / 6
        
        t += h
        t_values.append(t)
        x_values.append(x)
        y_values.append(y)
    
    return t_values, x_values, y_values
# Exemple d'utilisation
def f(t, x, y):
    # Exemple de système d'équations différentielles: dx/dt = -x, dy/dt = -y
    return -x, -y


t0 = 0
x0 = 1
y0 = 1
h = 0.1
t_final = 2

t_values, x_values, y_values = runge_kutta_4_system(f, f, t0, x0, y0, h, t_final)

# Affichage des résultats
for t, x, y in zip(t_values, x_values, y_values):
    print(f"t = {t}, x = {x}, y = {y}")

