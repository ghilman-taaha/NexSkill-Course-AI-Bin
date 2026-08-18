import numpy as np

ids, price , long , lat = np.loadtxt(r'E:\neskill\NexSkill course AI bin\OR_hos_prices1.csv', delimiter=',', usecols=(1, 2, 3, 9), unpack=True, dtype=str, quotechar='"')

print(long)
longfloat = long[1:].astype(float)
print(longfloat)

print(price)
pricefloat = price[1:].astype(float)
print(pricefloat)

print(ids)
idsclean = ids[1:]
print(idsclean)

print(lat)

latfloat = np.array([float(x) if x != '' else np.nan for x in lat[1:]])
print(latfloat)

print(np.nanmin(latfloat))

# statistics operations
print("lat mean: " , np.nanmean(latfloat))
print("lat average: " , np.nanmean(latfloat))
print("lat std: " , np.nanstd(latfloat))
print("lat mod: " , np.nanmedian(latfloat))
print("lat percentile - 25: " , np.nanpercentile(latfloat,25))
print("lat percentile  - 75: " , np.nanpercentile(latfloat,75))
print("lat percentile  - 3: " , np.nanpercentile(latfloat,3))
print("lat min : " , np.nanmin(latfloat))
print("lat max : " , np.nanmax(latfloat))

# maths operations
print("lat square: " , np.square(latfloat))
print("lat sqrt: " , np.sqrt(latfloat))
print("lat pow: " , np.power(latfloat,latfloat))
print("lat abs: " , np.abs(latfloat))

# arithmetic operations
addition = longfloat + pricefloat
subtraction = longfloat - pricefloat
multiplication = longfloat * pricefloat
division = longfloat / pricefloat

print("OR Hospitals Long - price - Addition:", addition)
print("OR Hospitals Long - price - Subtraction:", subtraction)
print("OR Hospitals Long - price - Multiplication:", multiplication)
print("OR Hospitals Long - price - Division:", division)

# trigonometric functions
latPie = (latfloat/np.pi) + 1
sine_values = np.sin(latPie)
cosine_values = np.cos(latPie)
tangent_values = np.tan(latPie)

print("lat - div - pie - Sine values:", sine_values)
print("lat - div - pie Cosine values:", cosine_values)
print("lat - div - pie Tangent values:", tangent_values)
print("lat - div - pie - Exponential values:", np.exp(latPie))