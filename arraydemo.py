rollno=[101,102,103,104,105]
# length of array is 5 index start from 0 and last index is 4
print(rollno)
# print(rollno[0])
# print(rollno[1])
# print(rollno[2])

for i in range(0,5):
    print(rollno[i])

print("With while loop")
i=0
while(i<5):
    print(rollno[i])
    i=i+1

names=["milind","Parth","Manasi","Sudhanshu","Kaushal","Anita"]
names.sort()
print(names)
#tradition for loop ( for (i=0;i<5;i++){})
# for i in range(0,3):
#     print(names[i])

#for in // shortcut for for loop // c++,java, JS , for each 

for x in names:
    print("Hello ", x)

names.pop()
print("After popping the name")
print(names)
names.pop()
print(names)
names.pop(1)
print(names)
# names.pop("Manasi")
names.remove("Manasi")
print(names)
# names.remove(1)
print(names)
n=input("Enter name to search ")
if n in names:
    print("Found")
else:
    print("Not found")
    



