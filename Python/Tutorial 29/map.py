meters = [100,200,400,800,1600,3200,5000]
'''miles = []
for i in meters:
    convert = i / 1609
    miles.append(convert)
print(miles)'''
meters_to_miles = lambda x: x/1609
print(list(map(meters_to_miles,meters)))