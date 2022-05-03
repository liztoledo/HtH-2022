### LIST PRACTICE ###

#STEP I
cities = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(cities)

#STEP II
artists = ["Jhene Aiko", "Mac Miller", "Chris Lake", "ILLENIUM", "Miguel", "Olivia Rodrigo", "SZA", "Beach House", "KAYTRANADA", "Rauw Alejandro", "Megan Thee Stallion"]

#STEP III
print(cities[0])
print(cities[2])
print(cities[3])


print(artists[0])
print(artists[4])
print(artists[5])

#STEP IV
fav_cities = [cities[0], cities[2:4], cities[7]]
print(fav_cities)
fav_artists = [artists[0], artists[3:5], artists[6]]
print(fav_artists)

#STEP V
cities[0] = "San Francisco"
cities[2] = "Brooklyn"
cities[7] = "Hollywood"
cities[5] = "Tampa"

#STEP VI
cities.append("Oakland")
cities.extend(["New York City", "Los Angeles"])
cities.insert(0, "Miami")

#STEP VII
cities.pop(8)
del cities[6]
cities.remove("New Orleans")
print(cities)


