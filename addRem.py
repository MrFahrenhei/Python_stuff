letters = ["a", "b", "c"]


# add
letters.append("d")
letters.insert(0, "-")

print(letters)

# remove
letters.pop(0)  # remove only one object
letters.remove("b")
del letters[0:3]  # remove all
letters.clear()
print(letters)
