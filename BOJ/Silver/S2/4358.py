import sys

tree = {}
tree_count = 0

for line in sys.stdin:  
    if line == '\n':
        break  
    type = line.strip()
    tree[type] = tree.get(type, 0) + 1
    tree_count += 1

sorted_tree = sorted(tree.items(), key=lambda x : x[0])

for key, value in sorted_tree:
    percentage = round(value/tree_count * 100, 4)
    print(key, '%.4f' %percentage)