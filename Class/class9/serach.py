a={
    "a":"apple",
    "b":"banana",
    "c":"caow"
}

value=input("Enter the value=")
for i in a.items():
    if value in i:
        print(i)
    