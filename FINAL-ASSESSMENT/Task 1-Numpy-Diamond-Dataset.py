
import numpy as np

# only numeric columns, cut/color/clarity a
ids, price , x , y = np.genfromtxt(r'E:\neskill\NexSkill course AI bin\FINAL-ASSESSMENT\10-diamonds.csv', delimiter=',', usecols=(0,7,8,9), unpack=True, dtype=None,skip_header=1)

print(ids)
print(price)
print(x)
print(y)

print(np.min(price))

# Diamonds price  - statistics operations
print("Diamonds Price mean: " , np.mean(price))
print("Diamonds Price average: " , np.average(price))
print("Diamonds Price std: " , np.std(price))
print("Diamonds Price mod: " , np.median(price))
print("Diamonds Price percentile - 25: " , np.percentile(price,25))
print("Diamonds Price percentile  - 75: " , np.percentile(price,75))
print("Diamonds Price percentile  - 3: " , np.percentile(price,3))
print("Diamonds Price min : " , np.min(price))
print("Diamonds Price max : " , np.max(price))

# Diamonds price  - maths operations
print("Diamonds Price square: " , np.square(price))
print("Diamonds Price sqrt: " , np.sqrt(price))
print("Diamonds Price pow: " , np.power(price,price))
print("Diamonds Price abs: " , np.abs(price))



# Perform basic arithmetic operations
addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y

print(" Diamonds x - y - Addition:", addition)
print(" Diamonds x - y - Subtraction:", subtraction)
print(" Diamonds x - y - Multiplication:", multiplication)
print(" Diamonds x - y - Division:", division)


#Trigonometric Functions

pricePie = (price/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)

print("Diamonds Price - div - pie  - Sine values:", sine_values)
print("Diamonds Price - div - pie Cosine values:", cosine_values)
print("Diamonds Price - div - pie Tangent values:", tangent_values)

print("Diamonds Price - div - pie  - Exponential values:", np.exp(pricePie))


# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(pricePie)
log10_array = np.log10(pricePie)

print("Diamonds Price - div - pie  - Natural logarithm values:", log_array)
print("Diamonds Price - div - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(pricePie)
print("Diamonds Price - div - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(pricePie)
print("Diamonds Price - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(pricePie)
print("Diamonds Price - div - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(pricePie)
print("Diamonds Price - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(pricePie)
print("Diamonds Price - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)


#Diamonds x Plus y - 2 dimentional arrary
D2XY = np.array([x,
                  y])

print ("Diamonds x Plus y - 2 dimentional arrary - " ,D2XY)

# check the dimension of array1
print("Diamonds x Plus y - 2 dimentional arrary - dimension" , D2XY.ndim) 
# Output: 2

# return total number of elements in array1
print("Diamonds x Plus y - 2 dimentional arrary - total number of elements" ,D2XY.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("Diamonds x Plus y - 2 dimentional arrary - gives size of array in each dimension" ,D2XY.shape)
# Output: (2,3)

# check the data type of array1
print("Diamonds x Plus y - 2 dimentional arrary - data type" ,D2XY.dtype) 
# Output: int64

# Splicing array
D2XYSlice=  D2XY[0:1:1 , 1:5:1]
print("Diamonds x Plus y - 2 dimentional arrary - Splicing array - D2XY[:1,:5] " , D2XYSlice)
D2XYSlice2=  D2XY[:1, 4:15:4]
print("Diamonds x Plus y - 2 dimentional arrary - Splicing array - D2XY[:1, 4:15:4] " , D2XYSlice2)



# Indexing array
D2XYSliceItemOnly=  D2XYSlice[0,1]
print("Diamonds x Plus y - 2 dimentional arrary - Index array - D2XYSlice[1,5] " , D2XYSliceItemOnly)
D2XYSlice2ItemOnly=  D2XYSlice2[0, 2]
print("Diamonds x Plus y - 2 dimentional arrary - index array - D2XYSlice2[0, 2] " , D2XYSlice2ItemOnly)


#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2XY):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2XY):
    print(index, elem)

"""# for loop
rows = np.shape(D2XY[0])[0]
cols = np.shape(D2XY[1])[0]
for i in range(0, (rows + 1)):
    for j in range(0, (cols + 1)):
        print (D2XY[i,j])
"""


# 2 x 53940 ========>>>>> 1  x 107880 - reshape
D2XY1TO107880 = np.reshape(D2XY, (1, 107880))
print("Diamonds x Plus y - 2 dimentional arrary - np.reshape(D2XY, (1, 107880)) : " , D2XY1TO107880)
print("Diamonds x Plus y - 2 dimentional arrary - np.reshape(D2XY, (1, 107880)) : Size " , D2XY1TO107880.size)
print("Diamonds x Plus y - 2 dimentional arrary - np.reshape(D2XY, (1, 107880)) : ndim " , D2XY1TO107880.ndim)
print("Diamonds x Plus y - 2 dimentional arrary - np.reshape(D2XY, (1, 107880)) : shape " , D2XY1TO107880.shape)
print("Diamonds x Plus y - 2 dimentional arrary - np.reshape(D2XY, (1, 107880)) : ndim " , D2XY1TO107880.ndim)




print()