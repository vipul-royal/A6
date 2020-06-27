str=input("Enter the string:")
ch=input("Enter the character to be checked:")
count=0
for letter in str:
    if letter==ch:
        count=count+1
print("The",ch,"Letter","in",str,"has repeated for",count,"times")