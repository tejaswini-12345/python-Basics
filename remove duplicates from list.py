num=list(map(int,input("enter a numbers:").split()))
unique_list=[]
element=0
while element<len(num):
    if num[element] not in unique_list:
        unique_list.append(num[element])
    element+=1
print("unique list",unique_list)




numbers=[20,30,40,10,10,20,77,67,88]
unique_list=set(numbers)
print(unique_list)      #sets are unordered