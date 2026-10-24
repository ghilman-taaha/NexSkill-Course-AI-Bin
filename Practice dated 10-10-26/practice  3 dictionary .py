property_dict = {
    "PropertyTitle": "Luxury Villa",
    "PropertyLang": 73.08,
    "PropertyLat": 31.42,
    "PropertyPrice": 25000000,
    "PropertyCity": "Faisalabad",
    "PropertyZipCode": 38000,
    "IsForSale": True
}

print(property_dict)

print(property_dict["PropertyTitle"])   
print(property_dict["PropertyPrice"])    
print(property_dict.get("PropertyCity")) 

for item in property_dict :
    print(property_dict)


print(type(property_dict))

property_dict["PropertyOwnerName"] = "Ali Khan"
print(property_dict)

del property_dict["PropertyLat"]
print(property_dict)

