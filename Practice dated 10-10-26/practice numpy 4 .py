import numpy as np 
import re
ids, Age, Gender, Country = np.genfromtxt(r'E:\neskill\NexSkill course AI bin\Practice dated 10-10-26\AI_Usage_and_Impact_on_Students_and_Professionals.csv',delimiter ="," , usecols = (0,1,2,3) ,dtype = str , unpack=True,encoding ='utf-8' , skip_header = 1)

print(ids)
print(Age)
print(Gender)
print(Country)

age_num = np.array([float(a) for a in Age if a.isdigit()])



print("Age mean: ", np.nanmean(age_num))
print("Age std: ", np.nanstd(age_num))
print("Age median: ", np.nanmedian(age_num))
print("Age percentile - 25: ", np.nanpercentile(age_num, 25))
print("Age percentile - 75: ", np.nanpercentile(age_num, 75))
print("Age percentile - 3: ", np.nanpercentile(age_num, 3))
print("Age min : ", np.nanmin(age_num))
print("Age max : ", np.nanmax(age_num))

print("Age square: ", np.square(age_num))
print("Age sqrt: ", np.sqrt(age_num))
print("Age pow: ", np.power(age_num, age_num))
print("Age abs: ", np.abs(age_num))
 
agePie = (age_num/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(agePie)
cosine_values = np.cos(agePie)
tangent_values = np.tan(agePie)
 
print("AI Usage Age - div - pie  - Sine values:", sine_values)
print("AI Usage Age - div - pie Cosine values:", cosine_values)
print("AI Usage Age - div - pie Tangent values:", tangent_values)
 
print("AI Usage Age - div - pie  - Exponential values:", np.exp(agePie))
 

log_array = np.log(agePie)
log10_array = np.log10(agePie)
 
print("AI Usage Age - div - pie  - Natural logarithm values:", log_array)
print("AI Usage Age - div - pie  = Base-10 logarithm values:", log10_array)

