recipe=("pizza","italian","medium")
print("Name =",recipe[0])
print("Cuisine =",recipe[1])
print("Size =",recipe[2])

pasta_in={"tomato","onion","garlic","tomato","garlic"}
print(pasta_in)
pasta_in.add("olive oil")
print(pasta_in)
pasta_in.discard("tomato")
print(pasta_in)

biryani_in={"onion","garlic","tomato","rice","water"}
print(pasta_in.intersection(biryani_in))
print(pasta_in.union(biryani_in))
print(pasta_in.difference(biryani_in))
print(pasta_in.symmetric_difference(biryani_in))