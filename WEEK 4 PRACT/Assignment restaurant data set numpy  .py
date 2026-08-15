import numpy as np

v1, v2, v3, v4 = np.genfromtxt(r"E:\neskill\nexskill course ai bin\FastFoodRestaurants.csv", delimiter=",", usecols=(1,3,4,6), skip_header=1, unpack=True, dtype=None, invalid_raise=False)

print(v1)
print(v2)
print(v3)
print(v4)

print(v1[0])
print(v2[3])
print(v3[5])
print(v4[2])

print(v1[0:10000])
print(v2[0:10000])
print(v3[0:10000])
print(v4[0:10000])

data = np.genfromtxt(r"E:\neskill\nexskill course ai bin\FastFoodRestaurants.csv", delimiter=",", skip_header=1, dtype=str, invalid_raise=False)

print(data.shape)
print(data[0])
print(data[:, 2])
print(data)

funding_raw = data[:, 5]

funding = np.array([
    float(x) if x.strip() not in ('', 'N/A', 'nan', 'NA') else np.nan for x in funding_raw])

print(funding.shape)

reshaped = funding.reshape(-1, 1)
print(reshaped.shape)
print(reshaped)