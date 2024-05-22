#ask user to enter a list to check wether it is palindrome or not.
check_list = []
num = int(input("Enter the number of elements you want to enter in your list: "))

for i in range(num):
  check_list.append(str(input(f"enter your {i+1} element->")))

print("we have got your list to check",check_list)

rev_list = check_list[::-1]
if check_list == rev_list:
  print("your list is palindrome")
else:
  print("your list is not palindrome")