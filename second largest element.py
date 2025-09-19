num = list(map(int, input("Enter the numbers: ").split()))
element = 0
first_largest = 0
second_largest = 0
while element < len(num):
    if num[element] > first_largest:
        second_largest = first_largest
        first_largest = num[element]
    elif num[element] < first_largest and num[element] > second_largest:
        second_largest = num[element]
    element += 1
print("Second largest element is:", second_largest)


#first largest element without using varibles a,b,c
num=list(map(int,input("Enter the numbers:").split()))
element=0
first_largest=0
while element<len(num):
    if num[element]>first_largest:
        first_largest=num[element]
    element+=1
print("secon largest element is:",first_largest)