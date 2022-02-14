def countwords(sentence):
    # the first word doesn't have a space in front, the rest does
    count = 1
    lastspace = 1
    # Iterate over the characters in the sentence
    for i in range(len(sentence)):
        # If character is a space, increase word count
        if sentence[i] == " ":
            count = count + 1
            # Keep track of the last space:
            # After the loop, lastspace will be equal
            # to the last value for i where the
            # character was a space
            lastspace = i
    # Print the last word
    print(sentence[lastspace + 1:])
    # Return the word count
    return count


# Alternative using str.split()
def countwords(sentence):
    # First split the string (which, by default splits on whitespace)
    words = sentence.split()
    # Next, print the last word, which has index -1
    print('The last word is', words[-1])
    # Finally return the number of words
    return len(words)