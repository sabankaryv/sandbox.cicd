#  Find the second largest number in list

# lst2=[10,1,2,35]
lst2 = [10, 35, 2, 20,35]

largest=lst2[0]
second_largest=lst2[1]

for num in lst2:
    if num > largest:
        second_largest=largest
        largest=num
    elif num > second_largest and num!=largest:
        second_largest=num

print(largest)
print(second_largest)