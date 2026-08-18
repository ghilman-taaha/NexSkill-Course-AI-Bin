#RealEstate-USA.csv
import numpy as np

bed, price , bath , houseSize = np.genfromtxt(r'E:\neskill\NexSkill course AI bin\RealEstate-USA.csv', delimiter=',', usecols=(3,2,4,10), unpack=True, dtype=None,skip_header=1)

print(bed)
print(price)
print(bath)
print(houseSize)

print(np.min(price))

# RealEstate-USA Price - statistics operations
print("RealEstate-USA Price mean: " , np.mean(price))
print("RealEstate-USA Price average: " , np.average(price))
print("RealEstate-USA Price std: " , np.std(price))
print("RealEstate-USA Price mod: " , np.median(price))
print("RealEstate-USA Price percentile - 25: " , np.percentile(price,25))
print("RealEstate-USA Price percentile  - 75: " , np.percentile(price,75))
print("RealEstate-USA Price percentile  - 3: " , np.percentile(price,3))
print("RealEstate-USA Price min : " , np.min(price))
print("RealEstate-USA Price max : " , np.max(price))

# RealEstate-USA Price - maths operations
print("RealEstate-USA Price square: " , np.square(price))
print("RealEstate-USA Price sqrt: " , np.sqrt(price))
print("RealEstate-USA Price pow: " , np.power(price,price))
print("RealEstate-USA Price abs: " , np.abs(price))



# Perform basic arithmetic operations
addition = bath + houseSize
subtraction = bath - houseSize
multiplication = bath * houseSize
division = bath / houseSize

print(" RealEstate-USA bath - houseSize - Addition:", addition)
print(" RealEstate-USA bath - houseSize - Subtraction:", subtraction)
print(" RealEstate-USA bath - houseSize - Multiplication:", multiplication)
print(" RealEstate-USA bath - houseSize - Division:", division)


#Trigonometric Functions

pricePie = (price/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)

print("RealEstate-USA Price - div - pie  - Sine values:", sine_values)
print("RealEstate-USA Price - div - pie Cosine values:", cosine_values)
print("RealEstate-USA Price - div - pie Tangent values:", tangent_values)

print("RealEstate-USA Price - div - pie  - Exponential values:", np.exp(pricePie))


# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(pricePie)
log10_array = np.log10(pricePie)

print("RealEstate-USA Price - div - pie  - Natural logarithm values:", log_array)
print("RealEstate-USA Price - div - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(pricePie)
print("RealEstate-USA Price - div - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(pricePie)
print("RealEstate-USA Price - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(pricePie)
print("RealEstate-USA Price - div - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(pricePie)
print("RealEstate-USA Price - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(pricePie)
print("RealEstate-USA Price - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)


#RealEstate-USA bath Plus houseSize - 2 dimentional arrary
D2BathHouseSize = np.array([bath,
                  houseSize])

print ("RealEstate-USA bath Plus houseSize - 2 dimentional arrary - " ,D2BathHouseSize)

# check the dimension of array1
print("RealEstate-USA bath Plus houseSize - 2 dimentional arrary - dimension" , D2BathHouseSize.ndim) 
# Output: 2

# return total number of elements in array1
print("RealEstate-USA bath Plus houseSize - 2 dimentional arrary - total number of elements" ,D2BathHouseSize.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("RealEstate-USA bath Plus houseSize - 2 dimentional arrary - gives size of array in each dimension" ,D2BathHouseSize.shape)
# Output: (2,3)

# check the data type of array1
print("RealEstate-USA bath Plus houseSize - 2 dimentional arrary - data type" ,D2BathHouseSize.dtype) 
# Output: float64

# Splicing array
D2BathHouseSizeSlice=  D2BathHouseSize[0:1:1 , 1:5:1]
print("RealEstate-USA bath Plus houseSize - 2 dimentional arrary - Splicing array - D2BathHouseSize[:1,:5] " , D2BathHouseSizeSlice)
D2BathHouseSizeSlice2=  D2BathHouseSize[:1, 4:15:4]
print("RealEstate-USA bath Plus houseSize - 2 dimentional arrary - Splicing array - D2BathHouseSize[:1, 4:15:4] " , D2BathHouseSizeSlice2)



# Indexing array
D2BathHouseSizeSliceItemOnly=  D2BathHouseSizeSlice[0,1]
print("RealEstate-USA bath Plus houseSize - 2 dimentional arrary - Index array - D2BathHouseSizeSlice[1,5] " , D2BathHouseSizeSliceItemOnly)
D2BathHouseSizeSlice2ItemOnly=  D2BathHouseSizeSlice2[0, 2]
print("RealEstate-USA bath Plus houseSize - 2 dimentional arrary - index array - D2BathHouseSizeSlice2[0, 2] " , D2BathHouseSizeSlice2ItemOnly)


#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2BathHouseSize):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2BathHouseSize):
    print(index, elem)

"""# for loop
rows = np.shape(D2BathHouseSize[0])[0]
cols = np.shape(D2BathHouseSize[1])[0]
for i in range(0, (rows + 1)):
    for j in range(0, (cols + 1)):
        print (D2BathHouseSize[i,j])
"""


# 2 x 200 ========>>>>> 1  x 400 - reshape
D2BathHouseSize1TO400 = np.reshape(D2BathHouseSize, (1, 400))
print("RealEstate-USA bath Plus houseSize - 2 dimentional arrary - np.reshape(D2BathHouseSize, (1, 400)) : " , D2BathHouseSize1TO400)
print("RealEstate-USA bath Plus houseSize - 2 dimentional arrary - np.reshape(D2BathHouseSize, (1, 400)) : Size " , D2BathHouseSize1TO400.size)
print("RealEstate-USA bath Plus houseSize - 2 dimentional arrary - np.reshape(D2BathHouseSize, (1, 400)) : ndim " , D2BathHouseSize1TO400.ndim)
print("RealEstate-USA bath Plus houseSize - 2 dimentional arrary - np.reshape(D2BathHouseSize, (1, 400)) : shape " , D2BathHouseSize1TO400.shape)
print("RealEstate-USA bath Plus houseSize - 2 dimentional arrary - np.reshape(D2BathHouseSize, (1, 400)) : ndim " , D2BathHouseSize1TO400.ndim)




print()