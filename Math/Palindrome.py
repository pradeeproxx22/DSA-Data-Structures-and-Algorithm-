num= int(input('Enter a number '))
original_num=num
rev = 0

# Seprate digit from number * and + into reverse
while num > 0:
  nxtdigit=num%10
  num=num//10
  rev=rev*10+nxtdigit

if original_num == rev:
  print('Palindrome')
else:
  print('Not a palindrome')
