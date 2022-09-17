ids = {'user1': [213, 213, 213, 15, 213], 
       'user2': [54, 54, 119, 119, 119], 
       'user3': [213, 98, 98, 35]}

geo_set = set()

for geo in ids.values():
    geo_set = geo_set.union(set(geo))

print(geo_set)
