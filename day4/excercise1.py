person={"Name":"Alice","age":25,"grade":"A"}

#add new key value
person["address"]="123 main st"
print(person)
#update age

person["age"]=32


#remove grade

if "grade" in person:
    del person["grade"]
    
    print(person)
