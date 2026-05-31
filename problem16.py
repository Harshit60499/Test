dictionary = {"Country": "State", "India":"Delhi", "China":"Beijing", "Japan":"Tokyo", "Qatar":"Doha", "France":"Marseiles"}
print(dictionary)
dictionary.update({"France":"Paris"})
print(dictionary)
dictionary["France"]= "Paris2"  # updating to a new value using second method of updating value
print(dictionary)