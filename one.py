# memory reference 
k=["hi",1,1]
print("Before assign")
# printing the k values
print(k)
#giving the reference the k values to a
a=k
#changing the k[0] value to "bye" 
a[0]="bye"
print("After assign")
print(k)
print(a)

"""
output:
Before assign
['hi', 1, 1]
After assign
['bye', 1, 1]
['bye', 1, 1]
"""