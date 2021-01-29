from rLinkedList import rLinkedList

a=rLinkedList()
a.append("a")
a.append("b")
a.append("c")
a.append("d")

print(a)
print(a.reverse())

a.append("e")
print(a.reverse())
print(a)

a.append("f")
print(a)
print(a.reverse())
print(a.reverse().reverse())

