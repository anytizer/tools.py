from namifier import namifier

names = ["", "First", "Fast Last", "First Middle Last", "First M1 m2 Last"]

nf = namifier()
for name in names:
    n = nf.namify(name)
    print(n)
