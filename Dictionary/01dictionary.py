# dicitionary is same like the dictionary we use in the real world
#dictionary is mutable which means it can able to change

from unicodedata import numeric


myDic ={
    "home":"THE PLACE WHERE WE ALL WE LIVE",
    "village":"Ruler human habitat area",
    "numbers":[1,2,3,],

    #nested disctionary
    "Animal": {'Dog': 'Mammal and friendly animal'}

} 



print(myDic['village'])
myDic['numbers']=[1,2,100]
print(myDic['numbers'])
print(myDic['Animal']['Dog'])