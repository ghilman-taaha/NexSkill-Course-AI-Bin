EmployeeInfoDic =  { 'Name': "Richard" , 'Age' : 34, 'Height' :5.9 }
print(EmployeeInfoDic)
print(type (EmployeeInfoDic))


print(len(EmployeeInfoDic))

for x in EmployeeInfoDic:
    print(x)

for x in EmployeeInfoDic:
    print(EmployeeInfoDic[x])

EmployeeInfoDic['Age'] = 56

EmployeeInfoDic['City'] = "LHR"
