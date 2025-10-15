site = {
    'Home': {
        'About': {},
        'Products': {
            'Electronics': {},
            'Books': {}
        },
        'Contacts': {}
    }
}

def find_path(tree, target, path=None):
    if path is None:
        path = []
    for page, subtree in tree.items():
        new_path = path + [page]
        if page == target:
            return new_path
        if isinstance(subtree, dict):
            result = find_path(subtree, target, new_path)
            if result:
                return result
    return None
target_page = 'Books'
path = find_path(site, target_page)
if path:
    print(" -> ".join(path))
else:
    print(f"Target page {target_page} not found")
