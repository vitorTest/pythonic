#!/usr/bin/env python3
# -*- coding: utf-8 -*-

listo = [i for i in range(41) if i%2 != 0]


# Append a item on the list's end, even if
# that item is another list
listo.append([j**2 for j in range(41) if j%2 == 0])
print("Appending a list:\n{}\n".format(listo))

# Removing like a stack
listo.pop()

# Here we can add other list
listo.extend([j**2	 for j in range(41) if j%2 == 0])

# Changing the "lasts" by the "firsts"
listo.reverse()
print("Extending a list(in a reverse order):\n{}\n".format(listo))

# Do not change by an index, only insert at the
# given position and rearrange the list
for i in range(0, 43, 21):
	listo.insert(i, 42)
print("Inserting '42's in a list:\n{}\n".format(listo))

# Give a index of an item
print("Index of the element '42', after index 19 at the list:\
    {}\n".format(listo.index(42, 20)))

# Counting a nnumber of one element present in the list
print("Index of the element '42', after index 19 at the list:\
    {}\n".format(listo.count(42)))

# sort in reverse
listo.sort(reverse=True)
print("Sorting a list:\n{}\n".format(listo))

# A copy
print("A list's copy:\n{}\n".format(listo.copy()))
