
# Armstrong 
num = int(input("Enter a number"))

# Variable initialize and value allocation 
orig_num = num
check_num = num
count = 0
armstrong_sum = 0

# num seprate and counting 
while num > 0 :
  nxt_digit= num % 10
  num = num // 10
  count+= 1


# loop -> separate -> loop -> power -> sum -> divide 
while orig_num > 0:
  nxt_digit2= orig_num %10
  total = 1
  for i in range(count):
    total*=nxt_digit2

# inside the while loop add-> divide 
  armstrong_sum+=total
  orig_num=orig_num//10


#Check with if else armstrong or not
if check_num == armstrong_sum :
  print("Armstrong")
else:
  print("Not a Armstrong number")
