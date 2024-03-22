def get_input(filename):
    with open(filename) as file:
        tmp = file.readlines()
    new_tmp = []
    for i in tmp:
        new_tmp.append(i.strip())
    return new_tmp


def molecules(data):
    replacements = []
    molecule = []

    for i in data:
        if "=>" in i:
            replacements.append(i)
        elif len(i) > 0:
            molecule.append(i)

    return [replacements, molecule]


def fusion(replace, molecule, fusion):
    find, add = replace.split(" => ")

    end = len(find)
    position = molecule.find(find)

    while position != -1:

        new_mol = molecule[:position] + add + molecule[position + end:]
        fusion.append(new_mol)
        position = molecule.find(find, position+end)

    return fusion


def reverse_engineer(molecule, replacements):
    count = 0

    for m in molecule:
        if m.isupper():
            count += 1

    Rn = molecule.count("Rn")
    y = molecule.count("Y")

    output = count - Rn*2 - y*2 -1

    return output