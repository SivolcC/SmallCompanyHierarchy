import anytree

# dataset
employees = [
    {"id": 100, "name": "Allan", "manager_id": 150},
    {"id": 220, "name": "Martin", "manager_id": 100},
    {"id": 150, "name": "Jamie", "manager_id": None},
    {"id": 275, "name": "Alex", "manager_id": 100},
    {"id": 400, "name": "Steve", "manager_id": 150},
    {"id": 190, "name": "David", "manager_id": 400},
    {"id": 222, "name": "Henri", "manager_id": 190}
]


def build_tree(p_num, p_node, data, nodes):
    for c_num in nodes[p_num]: # add children
        name = list(filter(lambda item: item['id'] == c_num, data))[0]['name']
        c_node = anytree.Node(name, parent=p_node)
        if c_num in nodes: # goes to children
            build_tree(c_num, c_node, data, nodes)

            
def find_root(data):
    try:
        roots = list(filter(lambda item: not item['manager_id'], data)) # get list of objects with no parent id
        if len(roots) < 1:
            raise Exception('Error in data: No root found.')
        elif len(roots) > 1:
            raise Exception('Error in data : One or more object is missing a parent.')
    except:
        raise
    return roots[0]['id'], roots[0]['name']


def main():
    try:
        parent_children = {}
        for e in employees: # map parents to list of children
            if e['manager_id'] in parent_children:
                parent_children[e['manager_id']].append(e['id'])
            else:
                parent_children[e['manager_id']] = [e['id']]

        root_id, root_name = find_root(employees) # get root id and name
        tree = anytree.Node(root_name)
        build_tree(root_id, tree, employees, parent_children)
                
        for pre, fill, node in anytree.RenderTree(tree): # render the tree
            print("{}{}".format(pre, node.name))
    except:
        raise


if __name__ == "__main__":
    main()
