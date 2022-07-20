# access value from the dictionary
a={
    "a":"apple",
    "b":"banana",
    "c":"caow"
}

if'a'in a:
    print('yes')
else:
        print("no")
 
b=dict(a)
print(b)
c=a.copy()
print(c)
print(list(a.keys()))