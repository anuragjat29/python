from os.path import split

list=[1,2,3,4,5,6,7,8,9,10]

list.append(11)
print(list)
list.remove(1)
print(list)
#find the index of the number 3
print(list.index(4))
list.sort()
print(list)
list.reverse()
print(list)
#sum
sum=0
for x in list:
    sum+=x
print(sum)
print(sum/len(list))
#reverse slicing comrehensive
r=list[::-1]
print(r)
def sumaverage(list):
    sum = 0
    for x in list:
        sum += x
    print("sum =",sum)
    print("average =",sum / len(list))
sumaverage(list)

list2=[x**2 for x in range(21) if x%2==0]
print(list2)

print(max(list2))
print(min(list2))

print(list.count(2))

#remove duplicate
list3=[1,2,33,3,2,4]
z=[]
for x in list3:
    if x is not list3:
        z.append(x)
print(z)

#merge list
print(list+list2)





















