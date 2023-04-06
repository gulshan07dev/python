# tuples are emmutable

# merge 2 tuples
countries = ("India", "China", "Pakistan")
countries2 = ("Afrika", "America", "Shrilanka")
southEastAsia = countries + countries2
print(southEastAsia)

# count() method
tuple1 = (0, 1, 2, 3, 2, 3, 1)
res1 = tuple1.count(3)
print("Count of 3 in tuple1:", res1)

# index() method
tuple2 = (0, 1, 2, 3, 2, 3, 1)
res2 = tuple2.index(3)
print("index of 3 is:", res2)