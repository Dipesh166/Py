mydef = {
    "home":"mandal family",
    #home is key and mandal family is value in the python
    "book":"DSA",
    1:2
}
#shows the key value 
print(mydef.keys())

#convert into list ::
print(list(mydef.keys()))

#we can also print values of the dictionary
print(list(mydef.values()))

# Items gives the tuples from the dictionary :- it gives both keys and values ::
print(list(mydef.items()))

# update is used to update the dictionary
print(mydef)
updatedef ={
    "apple":"fruit"
}
mydef.update(updatedef)
print(mydef)

#get
# Interview Questions
print(mydef.get("home2"))  # it give the none but doesn't throw the error
#print(mydef["home2"]) throws the error it give the error cause the home2 is n't present in the dictionary