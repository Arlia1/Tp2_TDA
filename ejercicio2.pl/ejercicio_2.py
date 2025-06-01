import pulp

def resolver_concesiones():
    paradas=200
    problema = pulp.LpProblem("Concesiones_Argentina_2000_SRL", pulp.LpMaximize)
    a = pulp.LpVariable("a", cat="Binary")
    b_1 = pulp.LpVariable("b_1", cat="Binary")
    b_2 = pulp.LpVariable("b_2", cat="Binary")
    c = pulp.LpVariable("c", cat="Binary")
    d = pulp.LpVariable("d", cat="Binary")
    e = pulp.LpVariable("e", cat="Binary")
    f = pulp.LpVariable("f", cat="Binary")
    g = pulp.LpVariable("g", cat="Binary")

    problema += (50000*a + 100000*b_1 + 120000*b_2 + 100000*c + 80000*d + 5000*e + 40000*f + 90000*g)
    problema += (30*a + 80*b_1 + 120*b_2 + 75*c + 50*d + 2*e + 20*f + 100*g) <= paradas
    problema += (a + d <= 1)
    problema += (b_1 + b_2 <= 1)

    problema.solve()

    return problema

if __name__ == "__main__":
    problema = resolver_concesiones()
    print("Estado:", pulp.LpStatus[problema.status])
    for var in problema.variables():
        print(f"{var.name}: {int(var.varValue)}")
    print("Ganancia total:", pulp.value(problema.objective))
