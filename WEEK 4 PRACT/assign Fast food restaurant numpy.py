#FastFoodRestaurants.csv
import numpy as np

import csv

postalCodeList, longitudeList, latitudeList = [], [], []
with open(r'E:\neskill\NexSkill course AI bin\FastFoodRestaurants.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        postalCodeList.append(float(row['postalCode'].split('-')[0]))
        longitudeList.append(float(row['longitude']))
        latitudeList.append(float(row['latitude']))

postalCode = np.array(postalCodeList)
longitude = np.array(longitudeList)
latitude = np.array(latitudeList)

print(postalCode)
print(longitude)
print(latitude)

print(np.min(postalCode))

# FastFoodRestaurants postalCode - statistics operations
print("FastFoodRestaurants postalCode mean: " , np.mean(postalCode))
print("FastFoodRestaurants postalCode average: " , np.average(postalCode))
print("FastFoodRestaurants postalCode std: " , np.std(postalCode))
print("FastFoodRestaurants postalCode mod: " , np.median(postalCode))
print("FastFoodRestaurants postalCode percentile - 25: " , np.percentile(postalCode,25))
print("FastFoodRestaurants postalCode percentile  - 75: " , np.percentile(postalCode,75))
print("FastFoodRestaurants postalCode percentile  - 3: " , np.percentile(postalCode,3))
print("FastFoodRestaurants postalCode min : " , np.min(postalCode))
print("FastFoodRestaurants postalCode max : " , np.max(postalCode))

# FastFoodRestaurants postalCode - maths operations
print("FastFoodRestaurants postalCode square: " , np.square(postalCode))
print("FastFoodRestaurants postalCode sqrt: " , np.sqrt(postalCode))
print("FastFoodRestaurants postalCode pow: " , np.power(postalCode,postalCode))
print("FastFoodRestaurants postalCode abs: " , np.abs(postalCode))



# Perform basic arithmetic operations
addition = longitude + latitude
subtraction = longitude - latitude
multiplication = longitude * latitude
division = longitude / latitude

print(" FastFoodRestaurants longitude - latitude - Addition:", addition)
print(" FastFoodRestaurants longitude - latitude - Subtraction:", subtraction)
print(" FastFoodRestaurants longitude - latitude - Multiplication:", multiplication)
print(" FastFoodRestaurants longitude - latitude - Division:", division)


#Trigonometric Functions

postalCodePie = (postalCode/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(postalCodePie)
cosine_values = np.cos(postalCodePie)
tangent_values = np.tan(postalCodePie)

print("FastFoodRestaurants postalCode - div - pie  - Sine values:", sine_values)
print("FastFoodRestaurants postalCode - div - pie Cosine values:", cosine_values)
print("FastFoodRestaurants postalCode - div - pie Tangent values:", tangent_values)

print("FastFoodRestaurants postalCode - div - pie  - Exponential values:", np.exp(postalCodePie))


# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(postalCodePie)
log10_array = np.log10(postalCodePie)

print("FastFoodRestaurants postalCode - div - pie  - Natural logarithm values:", log_array)
print("FastFoodRestaurants postalCode - div - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(postalCodePie)
print("FastFoodRestaurants postalCode - div - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(postalCodePie)
print("FastFoodRestaurants postalCode - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(postalCodePie)
print("FastFoodRestaurants postalCode - div - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(postalCodePie)
print("FastFoodRestaurants postalCode - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(postalCodePie)
print("FastFoodRestaurants postalCode - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)


#FastFoodRestaurants longitude Plus latitude - 2 dimentional arrary
D2LongitudeLatitude = np.array([longitude,
                  latitude])

print ("FastFoodRestaurants longitude Plus latitude - 2 dimentional arrary - " ,D2LongitudeLatitude)

# check the dimension of array1
print("FastFoodRestaurants longitude Plus latitude - 2 dimentional arrary - dimension" , D2LongitudeLatitude.ndim) 
# Output: 2

# return total number of elements in array1
print("FastFoodRestaurants longitude Plus latitude - 2 dimentional arrary - total number of elements" ,D2LongitudeLatitude.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("FastFoodRestaurants longitude Plus latitude - 2 dimentional arrary - gives size of array in each dimension" ,D2LongitudeLatitude.shape)
# Output: (2,3)

# check the data type of array1
print("FastFoodRestaurants longitude Plus latitude - 2 dimentional arrary - data type" ,D2LongitudeLatitude.dtype) 
# Output: float64

# Splicing array
D2LongitudeLatitudeSlice=  D2LongitudeLatitude[0:1:1 , 1:5:1]
print("FastFoodRestaurants longitude Plus latitude - 2 dimentional arrary - Splicing array - D2LongitudeLatitude[:1,:5] " , D2LongitudeLatitudeSlice)
D2LongitudeLatitudeSlice2=  D2LongitudeLatitude[:1, 4:15:4]
print("FastFoodRestaurants longitude Plus latitude - 2 dimentional arrary - Splicing array - D2LongitudeLatitude[:1, 4:15:4] " , D2LongitudeLatitudeSlice2)



# Indexing array
D2LongitudeLatitudeSliceItemOnly=  D2LongitudeLatitudeSlice[0,1]
print("FastFoodRestaurants longitude Plus latitude - 2 dimentional arrary - Index array - D2LongitudeLatitudeSlice[1,5] " , D2LongitudeLatitudeSliceItemOnly)
D2LongitudeLatitudeSlice2ItemOnly=  D2LongitudeLatitudeSlice2[0, 2]
print("FastFoodRestaurants longitude Plus latitude - 2 dimentional arrary - index array - D2LongitudeLatitudeSlice2[0, 2] " , D2LongitudeLatitudeSlice2ItemOnly)


#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2LongitudeLatitude):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2LongitudeLatitude):
    print(index, elem)

"""# for loop
rows = np.shape(D2LongitudeLatitude[0])[0]
cols = np.shape(D2LongitudeLatitude[1])[0]
for i in range(0, (rows + 1)):
    for j in range(0, (cols + 1)):
        print (D2LongitudeLatitude[i,j])
"""


# 2 x 10000 ========>>>>> 1  x 20000 - reshape
D2LongitudeLatitude1TO20000 = np.reshape(D2LongitudeLatitude, (1, 20000))
print("FastFoodRestaurants longitude Plus latitude - 2 dimentional arrary - np.reshape(D2LongitudeLatitude, (1, 20000)) : " , D2LongitudeLatitude1TO20000)
print("FastFoodRestaurants longitude Plus latitude - 2 dimentional arrary - np.reshape(D2LongitudeLatitude, (1, 20000)) : Size " , D2LongitudeLatitude1TO20000.size)
print("FastFoodRestaurants longitude Plus latitude - 2 dimentional arrary - np.reshape(D2LongitudeLatitude, (1, 20000)) : ndim " , D2LongitudeLatitude1TO20000.ndim)
print("FastFoodRestaurants longitude Plus latitude - 2 dimentional arrary - np.reshape(D2LongitudeLatitude, (1, 20000)) : shape " , D2LongitudeLatitude1TO20000.shape)
print("FastFoodRestaurants longitude Plus latitude - 2 dimentional arrary - np.reshape(D2LongitudeLatitude, (1, 20000)) : ndim " , D2LongitudeLatitude1TO20000.ndim)




print()