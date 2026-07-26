EmployeeInfoList =  [ "Richard" , 34 , 5.9 ]

print(EmployeeInfoList)
print(type(EmployeeInfoList))

print(len(EmployeeInfoList))

for x in EmployeeInfoList:
    print (x)

EmployeeInfoList.append("Lahore")

EmployeeInfoList.insert(2,"ABC")

EmployeeInfoList.remove(34)

EmployeeInfoList.pop(1)

print(EmployeeInfoList)
print(EmployeeInfoList[0])

print(EmployeeInfoList[1])

print(type(EmployeeInfoList))

EmployeeInfoList[0]= "changed....."
print(EmployeeInfoList)