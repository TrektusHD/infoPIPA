def istPrimzahl(input):
    input = int(input)
    prim = True
    k = 2
    while k*k <= input and prim == True:
        if input % k == 0: 
            prim = False
        k = k+1
    return prim

print(istPrimzahl(60))


def primfaktoren(n):
  faktoren = []
  z = n
  while z > 1:
    k = 2
    while k*k <= z:
      if z % k == 0:
        p = k
        faktoren.append(p)
        z = z // p
        k = 2
      else: 
        k = k + 1
    faktoren.append(z)
    break

    #bestimme den kleinsten Primfaktor p von z mit Probedivisionen
  return faktoren

print(primfaktoren(24))