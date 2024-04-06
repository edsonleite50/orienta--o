from Animal import Animal, Cachorro

capivara = Animal(4)

print(capivara.numero_de_patas)
print(capivara.fazer_barulho)

doguinho = Cachorro(4, 'caramelo')

print(doguinho.numero_de_patas, doguinho._cor)
print(doguinho.fazer_barulho())