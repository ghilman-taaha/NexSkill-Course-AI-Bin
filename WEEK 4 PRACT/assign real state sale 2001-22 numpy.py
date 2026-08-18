#Real_Estate_Sales_2001-2022_GL-Short.csv
import numpy as np

serialNumber, saleAmount , assessedValue , salesRatio = np.genfromtxt(r'E:\neskill\NexSkill course AI bin\Real_Estate_Sales_2001-2022_GL-Short.csv', delimiter=',', usecols=(0,6,5,7), unpack=True, dtype=None,skip_header=1, comments=None)

print(serialNumber)
print(saleAmount)
print(assessedValue)
print(salesRatio)

print(np.min(saleAmount))

# Real Estate Sales Sale Amount - statistics operations
print("Real Estate Sales Sale Amount mean: " , np.mean(saleAmount))
print("Real Estate Sales Sale Amount average: " , np.average(saleAmount))
print("Real Estate Sales Sale Amount std: " , np.std(saleAmount))
print("Real Estate Sales Sale Amount mod: " , np.median(saleAmount))
print("Real Estate Sales Sale Amount percentile - 25: " , np.percentile(saleAmount,25))
print("Real Estate Sales Sale Amount percentile  - 75: " , np.percentile(saleAmount,75))
print("Real Estate Sales Sale Amount percentile  - 3: " , np.percentile(saleAmount,3))
print("Real Estate Sales Sale Amount min : " , np.min(saleAmount))
print("Real Estate Sales Sale Amount max : " , np.max(saleAmount))

# Real Estate Sales Sale Amount - maths operations
print("Real Estate Sales Sale Amount square: " , np.square(saleAmount))
print("Real Estate Sales Sale Amount sqrt: " , np.sqrt(saleAmount))
print("Real Estate Sales Sale Amount pow: " , np.power(saleAmount,saleAmount))
print("Real Estate Sales Sale Amount abs: " , np.abs(saleAmount))



# Perform basic arithmetic operations
addition = assessedValue + salesRatio
subtraction = assessedValue - salesRatio
multiplication = assessedValue * salesRatio
division = assessedValue / salesRatio

print(" Real Estate Sales assessedValue - salesRatio - Addition:", addition)
print(" Real Estate Sales assessedValue - salesRatio - Subtraction:", subtraction)
print(" Real Estate Sales assessedValue - salesRatio - Multiplication:", multiplication)
print(" Real Estate Sales assessedValue - salesRatio - Division:", division)


#Trigonometric Functions

saleAmountPie = (saleAmount/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(saleAmountPie)
cosine_values = np.cos(saleAmountPie)
tangent_values = np.tan(saleAmountPie)

print("Real Estate Sales Sale Amount - div - pie  - Sine values:", sine_values)
print("Real Estate Sales Sale Amount - div - pie Cosine values:", cosine_values)
print("Real Estate Sales Sale Amount - div - pie Tangent values:", tangent_values)

print("Real Estate Sales Sale Amount - div - pie  - Exponential values:", np.exp(saleAmountPie))


# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(saleAmountPie)
log10_array = np.log10(saleAmountPie)

print("Real Estate Sales Sale Amount - div - pie  - Natural logarithm values:", log_array)
print("Real Estate Sales Sale Amount - div - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(saleAmountPie)
print("Real Estate Sales Sale Amount - div - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(saleAmountPie)
print("Real Estate Sales Sale Amount - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(saleAmountPie)
print("Real Estate Sales Sale Amount - div - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(saleAmountPie)
print("Real Estate Sales Sale Amount - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(saleAmountPie)
print("Real Estate Sales Sale Amount - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)


#Real Estate Sales assessedValue Plus salesRatio - 2 dimentional arrary
D2AssessedValueSalesRatio = np.array([assessedValue,
                  salesRatio])

print ("Real Estate Sales assessedValue Plus salesRatio - 2 dimentional arrary - " ,D2AssessedValueSalesRatio)

# check the dimension of array1
print("Real Estate Sales assessedValue Plus salesRatio - 2 dimentional arrary - dimension" , D2AssessedValueSalesRatio.ndim) 
# Output: 2

# return total number of elements in array1
print("Real Estate Sales assessedValue Plus salesRatio - 2 dimentional arrary - total number of elements" ,D2AssessedValueSalesRatio.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("Real Estate Sales assessedValue Plus salesRatio - 2 dimentional arrary - gives size of array in each dimension" ,D2AssessedValueSalesRatio.shape)
# Output: (2,3)

# check the data type of array1
print("Real Estate Sales assessedValue Plus salesRatio - 2 dimentional arrary - data type" ,D2AssessedValueSalesRatio.dtype) 
# Output: float64

# Splicing array
D2AssessedValueSalesRatioSlice=  D2AssessedValueSalesRatio[0:1:1 , 1:5:1]
print("Real Estate Sales assessedValue Plus salesRatio - 2 dimentional arrary - Splicing array - D2AssessedValueSalesRatio[:1,:5] " , D2AssessedValueSalesRatioSlice)
D2AssessedValueSalesRatioSlice2=  D2AssessedValueSalesRatio[:1, 4:15:4]
print("Real Estate Sales assessedValue Plus salesRatio - 2 dimentional arrary - Splicing array - D2AssessedValueSalesRatio[:1, 4:15:4] " , D2AssessedValueSalesRatioSlice2)



# Indexing array
D2AssessedValueSalesRatioSliceItemOnly=  D2AssessedValueSalesRatioSlice[0,1]
print("Real Estate Sales assessedValue Plus salesRatio - 2 dimentional arrary - Index array - D2AssessedValueSalesRatioSlice[1,5] " , D2AssessedValueSalesRatioSliceItemOnly)
D2AssessedValueSalesRatioSlice2ItemOnly=  D2AssessedValueSalesRatioSlice2[0, 2]
print("Real Estate Sales assessedValue Plus salesRatio - 2 dimentional arrary - index array - D2AssessedValueSalesRatioSlice2[0, 2] " , D2AssessedValueSalesRatioSlice2ItemOnly)


#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2AssessedValueSalesRatio):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2AssessedValueSalesRatio):
    print(index, elem)

"""# for loop
rows = np.shape(D2AssessedValueSalesRatio[0])[0]
cols = np.shape(D2AssessedValueSalesRatio[1])[0]
for i in range(0, (rows + 1)):
    for j in range(0, (cols + 1)):
        print (D2AssessedValueSalesRatio[i,j])
"""


# 2 x 142 ========>>>>> 1  x 284 - reshape
D2AssessedValueSalesRatio1TO284 = np.reshape(D2AssessedValueSalesRatio, (1, 284))
print("Real Estate Sales assessedValue Plus salesRatio - 2 dimentional arrary - np.reshape(D2AssessedValueSalesRatio, (1, 284)) : " , D2AssessedValueSalesRatio1TO284)
print("Real Estate Sales assessedValue Plus salesRatio - 2 dimentional arrary - np.reshape(D2AssessedValueSalesRatio, (1, 284)) : Size " , D2AssessedValueSalesRatio1TO284.size)
print("Real Estate Sales assessedValue Plus salesRatio - 2 dimentional arrary - np.reshape(D2AssessedValueSalesRatio, (1, 284)) : ndim " , D2AssessedValueSalesRatio1TO284.ndim)
print("Real Estate Sales assessedValue Plus salesRatio - 2 dimentional arrary - np.reshape(D2AssessedValueSalesRatio, (1, 284)) : shape " , D2AssessedValueSalesRatio1TO284.shape)
print("Real Estate Sales assessedValue Plus salesRatio - 2 dimentional arrary - np.reshape(D2AssessedValueSalesRatio, (1, 284)) : ndim " , D2AssessedValueSalesRatio1TO284.ndim)




print()