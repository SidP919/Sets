s = {'blueberry', 'rasberry'}

s.add('redberry')
print(s)

s.add("blueberry")
print(s)
#Sets always have unique elements only

l = [1, 2, 3, 3, 4, 4, 4, 5, 'abc', 'abc']
#casting of list to Set:
no_duplicate_set = set(l)
print(no_duplicate_set)

#Operations on Sets:-------------->
library1 = {'Harry Potter', "Hunger Games", "Lord of Rings"}
library2 = {'Harry Potter', 'Romeo & Juliet'}
#union:
all_the_books = library1.union(library2)
print(all_the_books)
#intersection:
at_both_libraries = library1.intersection(library2)
print(at_both_libraries)
#difference:
not_at_lib2_but_at_lib1 = library1.difference(library2)
print(not_at_lib2_but_at_lib1)
#clear:
library1.clear()
print(library1)