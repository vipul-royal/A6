def char_dlt(str, n):
    x= str[:n]
    y=str[n+1:]
    return x+y
ch=input("Enter the string:")
n=int(input("Enter the index where the character is to be deleted:"))
print(char_dlt(ch,n))