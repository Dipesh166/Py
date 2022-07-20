a={"rayan",'shyam'}
b={"dipesh","rayan"}
c=b.union(a)
print(c)

print(b.intersection(a))
print(b.difference_update(a))
b.symmetric_difference_update(a)
print(b)