a = 7

def factoriel_calc(num):
    if num == 0:
        return 1
    else:
        return num * factoriel_calc(num - 1)
        

print(factoriel_calc(a))
