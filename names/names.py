# import time

# start_time = time.time()

# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()

# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

#the initial solution is probably how I would do it just as a reflex... but it takes 12 seconds on my machine...

import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

speedWidget = BinarySearchTree('Martha Mewart')

f = open('names_1.txt', 'r')

for line in f.read().split('\n'):
    print(line)
    speedWidget.insert(line)

f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

duplicates = []
for i in names_2:
    # tom = names_2[i]
    # if speedWidget.contains(names_2[nameoh]):
    #     duplicates.append(names_2[nameoh])
    # print(tom)
    # print(i)
    if speedWidget.contains(i):
        duplicates.append(i)


# print(names_2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")