import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=np.inf)

v1, v2, v3, v4 = np.genfromtxt(r"E:\neskill\nexskill course ai bin\RealEstate-USA.csv", delimiter=",", usecols=(1,3,4,6), skip_header=1, unpack=True, dtype=None, invalid_raise=False)

print(v1)
print(v2)
print(v3)
print(v4)

print(v1[0])
print(v2[3])
print(v3[5])
print(v4[2])

print(v1[0:200])
print(v2[0:200])
print(v3[0:200])
print(v4[0:200])

data = np.genfromtxt(r"E:\neskill\nexskill course ai bin\RealEstate-USA.csv", delimiter=",", skip_header=1, dtype=str, invalid_raise=False)

print(data.shape)
print(data[0])
print(data[:, 2])

prices_raw = data[:, 2]

prices = np.array([
    float(x) if x.strip() not in ('', 'N/A', 'nan', 'NA') else np.nan for x in prices_raw])

print(prices.shape)

reshaped = prices.reshape(-1, 1)
print(reshaped.shape)
print(reshaped[:5])