import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=np.inf)

v1, v2, v3, v4 = np.genfromtxt(r"E:\neskill\nexskill course ai bin\startup_growth_investment_data.csv", delimiter=",", usecols=(0,1,3,4), skip_header=1, unpack=True, dtype=None, invalid_raise=False)

print(v1)
print(v2)
print(v3)
print(v4)

print(v1[0])
print(v2[3])
print(v3[5])
print(v4[2])

print(v1[0:5000])
print(v2[0:5000])
print(v3[0:5000])
print(v4[0:5000])

data = np.genfromtxt(r"E:\neskill\nexskill course ai bin\startup_growth_investment_data.csv", delimiter=",", skip_header=1, dtype=str, invalid_raise=False)

print(data.shape)
print(data[0])
print(data[:, 3])

investment_raw = data[:, 3]

investment = np.array([
    float(x) if x.strip() not in ('', 'N/A', 'nan', 'NA') else np.nan for x in investment_raw])

print(investment.shape)

reshaped = investment.reshape(-1, 1)
print(reshaped.shape)
print(reshaped[:5])