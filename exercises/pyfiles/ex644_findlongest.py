def find_longest(string, delim):
    sequence = string.split(delim)

    longest = ""
    for word in sequence:
        if len(word) > len(longest):
            longest = word

    print(longest, len(longest))