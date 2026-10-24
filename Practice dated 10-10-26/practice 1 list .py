property_list = ["Luxury Villa", 73.08, 31.42, 25000000, "Faisalabad", 38000, True]

print(property_list)

print(property_list[0])    
print(property_list[3])    
print(property_list[-1])   

for item in property_list:
    print(item)

print(type(property_list))

property_list .append ("Ghilmaan")
print(property_list)

property_list.remove (31.42)
print(property_list)

property_list.append("Faisalabad")
print(property_list)
print(property_list.count("Faisalabad"))   