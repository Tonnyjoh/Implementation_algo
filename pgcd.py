def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = 83182045654848
b = 57756487411
pgcd_result = pgcd(a, b)
print(f"Le PGCD de {a} et {b} est {pgcd_result}.")
