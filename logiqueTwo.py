from itertools import product

def evaluate(expr, var_values):
    expr = expr.replace('!', 'not ').replace('->', '<=')
    for var, val in var_values.items():
        expr = expr.replace(var, str(val))
    return eval(expr)

def is_valid(argument):
    premises = argument[:-1]
    conclusion = argument[-1]

    variables = set()
    for statement in argument:
        variables.update(set(filter(lambda x: x.isalpha(), statement)))
    variables = sorted(list(variables))

    truth_values = product([True, False], repeat=len(variables))

    for values in truth_values:
        var_values = dict(zip(variables, values))
        premise_evaluations = [evaluate(premise, var_values) for premise in premises]

        if all(premise_evaluations) and not evaluate(conclusion, var_values):
            return False

    return True

def verify_arguments(arguments):
    for i, argument in enumerate(arguments, start=1):
        print(f"Argument {i}:")
        print("L'argument est valide." if is_valid(argument) else "L'argument n'est pas valide.")

arguments = [
    [
        "h1: p->q",
        "h2: r->not q",
        "h3: r",
        "Conclusion: not p"
    ],
    [
        "h1: p and q",
        "h2: p",
        "Conclusion: q"
    ],
    # Ajoutez d'autres arguments ici
]

verify_arguments(arguments)
