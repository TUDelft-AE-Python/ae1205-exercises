values = [10, 20, 30, 40, 50, 60, 70]
lengths = [2, 2, 3]

result = []
counter = 0

for i in range(len(lengths)):
    result.append(values[counter:counter+lengths[i]])  # select a list of lengths[i] values
    counter += lengths[i]  # increment the counter by the number of values we just added

print(result)