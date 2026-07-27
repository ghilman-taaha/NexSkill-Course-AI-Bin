import numpy as np
v1, v2, v3, v4 = np.genfromtxt(r"E:\neskill\nexskill course ai bin\RealEstate-USA.csv", delimiter=",", usecols=(1,3,4,6), skip_header=1, unpack=True, dtype=None)
print(v1)
print(v2)
print(v3)
print(v4)

print(v1[0])    #values(status)
print(v2[3])    #bed
print(v3[5])    #Bath
print(v4[2])    #street

print(v1[0:5])    # v1 ke pehle 5 values
print(v2[2:7])    # v2 index from 2 to 6
print(v4[:3])     # v4 starting 3 values

data = np.genfromtxt(r"E:\neskill\nexskill course ai bin\RealEstate-USA.csv", delimiter=",", skip_header=1, dtype=str)

print(data.shape)
print(data[0])
print(data[:, 2])

prices = data[:, 2].astype(float)     # price column, number mein convert
print(prices.shape)                    # (200,)

reshaped = prices.reshape(-1, 1)       # column shape banayenge
print(reshaped.shape)                   # (200, 1)
print(reshaped[:5])                     # pehli 5 dekhne ke liye