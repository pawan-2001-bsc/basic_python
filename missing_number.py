n=int(input("Enter the size of an array:"))

arr=[]
print("Enter the numbers:")
for i in range(0,n-1):
    arr.append(int(input()))

expected_sum = n * (n + 1) // 2

actual_sum=sum(arr)

missing_number = expected_sum - actual_sum

print("The  missing number is:",missing_number)
