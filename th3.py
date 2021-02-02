def root_finder(part_list):
    root = [part_list[0][0]]
    for i in part_list[1:]:
        if not is_leaf(i):
            root.append(i[0])
    for i in part_list:
        if not is_leaf(i):
            for j in i[1:]:
                if j[1] in root:
                    root.remove(j[1])
    for i in part_list:
        if i[0] == root[0]:
            return i

def copier(lst):
    new_list = []
    for i in lst:
        if is_leaf(i):
            new_list.append(i)
        else:
            mini_list = []
            for j in i:
                mini_list.append(j)
            new_list.append(mini_list)

    return new_list
def fixer(part_list):
    x =  copier(part_list)
    temp = copier(part_list)
    root_tree = root_finder(temp)
    if is_leaf(root_tree):
        return [1]+[root_tree]
    temp.remove(root_tree)
    for i in range(1,len(root_tree)):
        if not is_leaf(root_tree):
            root_tree[i] = list(root_tree[i])
            root_tree[i][1] = merger(root_tree[i][1],temp)
    part_list = x
    return [1]+[root_tree]

def merger(name,part_list):
    temp = part_list
    for i in temp:
        if i[0] == name:
            node = i
            break
    if is_leaf(node):
        return node
    lst = [node[0]]
    temp.remove(node)
    for i in range(1,len(node)):
        lst.append([node[i][0]]+[merger(node[i][1],temp)])
    return lst

def is_leaf(t):
    if type(t[1]) == float:
        return True
    return False

def calculator(tree):
    if is_leaf(tree):
        return tree[1]
    if is_leaf(tree[1]):
        return tree[0]*tree[1][1]
    x = 0
    for i in range(1,len(tree[1])):
        x+= tree[0]*calculator(tree[1][i])
    return x

def name_keeper(tree):
    names = []
    if is_leaf(tree):
        return tree[0]
    if is_leaf(tree[1]):
        return tree[1][0]
    for i in range(1,len(tree[1])):
        t=name_keeper(tree[1][i])
        if type(t) == list:
            for i in t:
                names.append(i)
        else:    
            names.append(t)
    return names

def counter(tree):
    if is_leaf(tree):
        return 1
    if is_leaf(tree[1]):
        return tree[0]
    x = []
    for i in range(1,len(tree[1])):
        t = counter(tree[1][i])
        if type(t) == list:
            for k in t:
                x+= [tree[0]*k]
        else:
            x+= [tree[0]*counter(tree[1][i])]
    return x



def calculate_price(part_list):
    temp = part_list.copy()
    temp = fixer(temp)
    return calculator(temp)

def required_parts(part_list):
    tree = fixer(part_list)
    if is_leaf(tree[1]):
        return [(1,tree[1][0])]
    else:
        names = name_keeper(tree)
        count = counter(tree)
        return [(count[i],names[i]) for i in range(len(names))]

def stock_check(part_list, stock_list):
    temp = part_list.copy()
    req_list = required_parts(temp)
    res  = [(i[1],i[0]) for i in req_list]
    deletion = []
    for i in range(len(res)):
        for j in stock_list:
            if res[i][0] == j[1]:
                if res[i][1]-j[0] > 0:
                  res[i]= (res[i][0],res[i][1]-j[0])
                else:
                    deletion.append(res[i])
    for i in deletion:
        res.remove(i)
    return res
