import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Hypothétique équation différentielle pour illustrer
def model(y, t):
    dydt = y  # Simplification: y' = y
    return dydt

# Paramètres
y0 = 1.0  # Condition initiale
t = np.linspace(0, 10, 100)  # Temps

# Résolution de l'ODE avec la méthode de Runge-Kutta
sol = odeint(model, y0, t)

# Affichage des résultats
plt.figure(figsize=(8, 6))
plt.plot(t, sol, label='Solution avec Runge-Kutta')
plt.xlabel('Temps')
plt.ylabel('y(t)')
plt.title('Prédiction avec la méthode de Runge-Kutta')
plt.legend()
plt.grid(True)
plt.show()
