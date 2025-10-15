family_tree = {
    "Mumtaz": ["rehan", "Shahnawaz", "Sarfaraz", "Khobaib"],
    "rehan": ["soraim", "abdullah"],
    "Shahnawaz": ["Ahmad"],
    "Sarfaraz": [],
    "soraim": []
}

def find_descendants(tree, person, descendants=None):
    if descendants is None:
        descendants = []
    for child in tree.get(person, []):
        descendants.append(child)
        find_descendants(tree, child, descendants)
    return descendants

person = "Mumtaz"
descendants = find_descendants(family_tree, person)
print(f"All descendants of {person}: {descendants}")