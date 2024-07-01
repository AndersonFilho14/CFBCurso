''' Uma lista que não é modificada, sendo expressa por '()', na lista é '[]'
podendo ser mudada transfomando em uma lista e depois voltando para uma tupla

'''
casa = ('amarela','verde','azul')
l_casa = list(casa)
l_casa[0] = "lilas"
t_casa = tuple(l_casa)
print(t_casa)

