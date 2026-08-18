#startup_growth_investment_data.csv
import numpy as np

fundingRounds, investmentAmount , valuation , growthRate = np.genfromtxt(r'E:\neskill\NexSkill course AI bin\startup_growth_investment_data.csv', delimiter=',', usecols=(2,3,4,8), unpack=True, dtype=None,skip_header=1)

print(fundingRounds)
print(investmentAmount)
print(valuation)
print(growthRate)

print(np.min(investmentAmount))

# Startup Investment Amount - statistics operations
print("Startup Investment Amount mean: " , np.mean(investmentAmount))
print("Startup Investment Amount average: " , np.average(investmentAmount))
print("Startup Investment Amount std: " , np.std(investmentAmount))
print("Startup Investment Amount mod: " , np.median(investmentAmount))
print("Startup Investment Amount percentile - 25: " , np.percentile(investmentAmount,25))
print("Startup Investment Amount percentile  - 75: " , np.percentile(investmentAmount,75))
print("Startup Investment Amount percentile  - 3: " , np.percentile(investmentAmount,3))
print("Startup Investment Amount min : " , np.min(investmentAmount))
print("Startup Investment Amount max : " , np.max(investmentAmount))

# Startup Investment Amount - maths operations
print("Startup Investment Amount square: " , np.square(investmentAmount))
print("Startup Investment Amount sqrt: " , np.sqrt(investmentAmount))
print("Startup Investment Amount pow: " , np.power(investmentAmount,investmentAmount))
print("Startup Investment Amount abs: " , np.abs(investmentAmount))



# Perform basic arithmetic operations
addition = valuation + growthRate
subtraction = valuation - growthRate
multiplication = valuation * growthRate
division = valuation / growthRate

print(" Startup Valuation - growthRate - Addition:", addition)
print(" Startup Valuation - growthRate - Subtraction:", subtraction)
print(" Startup Valuation - growthRate - Multiplication:", multiplication)
print(" Startup Valuation - growthRate - Division:", division)


#Trigonometric Functions

investmentAmountPie = (investmentAmount/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(investmentAmountPie)
cosine_values = np.cos(investmentAmountPie)
tangent_values = np.tan(investmentAmountPie)

print("Startup Investment Amount - div - pie  - Sine values:", sine_values)
print("Startup Investment Amount - div - pie Cosine values:", cosine_values)
print("Startup Investment Amount - div - pie Tangent values:", tangent_values)

print("Startup Investment Amount - div - pie  - Exponential values:", np.exp(investmentAmountPie))


# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(investmentAmountPie)
log10_array = np.log10(investmentAmountPie)

print("Startup Investment Amount - div - pie  - Natural logarithm values:", log_array)
print("Startup Investment Amount - div - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(investmentAmountPie)
print("Startup Investment Amount - div - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(investmentAmountPie)
print("Startup Investment Amount - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(investmentAmountPie)
print("Startup Investment Amount - div - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(investmentAmountPie)
print("Startup Investment Amount - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(investmentAmountPie)
print("Startup Investment Amount - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)


#Startup Valuation Plus growthRate - 2 dimentional arrary
D2ValuationGrowthRate = np.array([valuation,
                  growthRate])

print ("Startup Valuation Plus growthRate - 2 dimentional arrary - " ,D2ValuationGrowthRate)

# check the dimension of array1
print("Startup Valuation Plus growthRate - 2 dimentional arrary - dimension" , D2ValuationGrowthRate.ndim) 
# Output: 2

# return total number of elements in array1
print("Startup Valuation Plus growthRate - 2 dimentional arrary - total number of elements" ,D2ValuationGrowthRate.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("Startup Valuation Plus growthRate - 2 dimentional arrary - gives size of array in each dimension" ,D2ValuationGrowthRate.shape)
# Output: (2,3)

# check the data type of array1
print("Startup Valuation Plus growthRate - 2 dimentional arrary - data type" ,D2ValuationGrowthRate.dtype) 
# Output: float64

# Splicing array
D2ValuationGrowthRateSlice=  D2ValuationGrowthRate[0:1:1 , 1:5:1]
print("Startup Valuation Plus growthRate - 2 dimentional arrary - Splicing array - D2ValuationGrowthRate[:1,:5] " , D2ValuationGrowthRateSlice)
D2ValuationGrowthRateSlice2=  D2ValuationGrowthRate[:1, 4:15:4]
print("Startup Valuation Plus growthRate - 2 dimentional arrary - Splicing array - D2ValuationGrowthRate[:1, 4:15:4] " , D2ValuationGrowthRateSlice2)



# Indexing array
D2ValuationGrowthRateSliceItemOnly=  D2ValuationGrowthRateSlice[0,1]
print("Startup Valuation Plus growthRate - 2 dimentional arrary - Index array - D2ValuationGrowthRateSlice[1,5] " , D2ValuationGrowthRateSliceItemOnly)
D2ValuationGrowthRateSlice2ItemOnly=  D2ValuationGrowthRateSlice2[0, 2]
print("Startup Valuation Plus growthRate - 2 dimentional arrary - index array - D2ValuationGrowthRateSlice2[0, 2] " , D2ValuationGrowthRateSlice2ItemOnly)



for elem in np.nditer(D2ValuationGrowthRate):
    print(elem)


for index, elem in np.ndenumerate(D2ValuationGrowthRate):
    print(index, elem)

"""# for loop
rows = np.shape(D2ValuationGrowthRate[0])[0]
cols = np.shape(D2ValuationGrowthRate[1])[0]
for i in range(0, (rows + 1)):
    for j in range(0, (cols + 1)):
        print (D2ValuationGrowthRate[i,j])
"""


# 2 x 5000 ========>>>>> 1  x 10000 - reshape
D2ValuationGrowthRate1TOFlat = np.reshape(D2ValuationGrowthRate, (1, 10000))
print("Startup Valuation Plus growthRate - 2 dimentional arrary - np.reshape(D2ValuationGrowthRate, (1, 10000)) : " , D2ValuationGrowthRate1TOFlat)
print("Startup Valuation Plus growthRate - 2 dimentional arrary - np.reshape : Size " , D2ValuationGrowthRate1TOFlat.size)
print("Startup Valuation Plus growthRate - 2 dimentional arrary - np.reshape : ndim " , D2ValuationGrowthRate1TOFlat.ndim)
print("Startup Valuation Plus growthRate - 2 dimentional arrary - np.reshape : shape " , D2ValuationGrowthRate1TOFlat.shape)
print("Startup Valuation Plus growthRate - 2 dimentional arrary - np.reshape : ndim " , D2ValuationGrowthRate1TOFlat.ndim)




print()