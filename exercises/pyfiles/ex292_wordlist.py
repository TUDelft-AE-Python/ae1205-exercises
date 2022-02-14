nwords = int(input("How many words do you want in your list? "))

# Store the words in a list. Start with an empty one
words = []
# Use a for-loop to call input() nwords times
for i in range(nwords):
    word = input("Enter the next word in the list: ")
    # Use list.append() to add the word to the list
    words.append(word)

for i in range(nwords):
    print(words[i], 'has length', len(words[i]))