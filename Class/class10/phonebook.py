#phonebook
phonebook_id={}
contact={}
contact=dict(zip(phonebook_id,contact))
ids=int(input("how many  entry do you want::"))
for i in range(ids):
    contact[i]={}
    #adding name
    contact[i]['Name']=input("Enter the name::")
    #adding Ntc Number

    contact[i]['NTC']=int(input("Enter the NTC NUMBER"))
    #adding ncell number 
    contact[i]['Ncell']=int(input("Enter the NCELL NUMBER::"))
    #adding landline
    contact[i]['landline']=int(input('Enter the landline number'))
print(contact)
