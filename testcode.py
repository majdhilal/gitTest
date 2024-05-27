array1 = ["Alice", "Bob", "Charlie", "Frank", "Jack", "Jack"]
array2 = ["Majd", "Eve", "Charlie", "Alice", "Bob", "Frank", "Grace", "Liam"]
array3 = ["Henry", "Ivy", "Jack", "Kate", "Alice", "Liam", "Ivy"]
array4 = ["Majd", "Ivy", "Eve", "Bob", "Frank", "Liam", "Frank", "Charlie", "Alice"]

arr = array1 + array2 + array3 + array4
dictionary = {}

for name in arr:
    if name in dictionary:
        dictionary[name] += 1
    else:
        dictionary[name] = 1

for name, count in dictionary.items():
    print(f"{name}: {count}")
