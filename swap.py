def strs(a, b):
    n_a=b[:2] + a[2:]
    n_b=a[:2] + b[2:]
    return n_a+' '+n_b
x=input("Enter the first string:")
y=input("Enter the second string:")
print("The Original String:",x+y)
print("The Swapped String:",strs(x,y))