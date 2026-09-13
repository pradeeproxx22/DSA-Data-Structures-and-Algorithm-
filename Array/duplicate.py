# This program is to find duplicate in the array and print duplicate number only once .

n = int(input("Enter element :"))
arr = []
printed = []
for i in range(0, n):
    value = int(input("> "))
    arr.append(value)

for i in range (0, n): 
    
    for j in range(i+1,n):
        if arr[i] == arr[j] and arr[i] not in printed:  #  andar wala == bahar wala
            printed.append(arr[i])


print("Duplicate elements : ",printed)    
    
       

    
    
