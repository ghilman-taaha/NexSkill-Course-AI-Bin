BookList =  [ "Think and grow rich" , 1997 , 54.5  , "Richard" , True]
print(BookList)
print(type(BookList))
print(len(BookList))
for x in BookList:
    print(x)

BookList.append("ABC INC")
print(BookList)

BookList.insert(3,"LA")
print (BookList)

BookList.remove(54.5)
print(BookList)

BookList.pop(1)
print(BookList)

BookList[1] = "Changed..."
print(BookList)

print(BookList[0])
print(type(BookList[0]))