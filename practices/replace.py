#replace the name and date
letter ='''
You are accepted !!!
 Dear NAME,
Today is the DATE
'''
name=input("Enter the name of the person\n")
date=input("Give the date of BOT\n")
letter = letter.replace("NAME", name)
letter = letter.replace("DATE", date)
print(letter)
