import string

letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']


def all_words(length):
    # Base case
    if length == 0:
        yield ""
    # Recursive rule
    else:
        for word in all_words(length - 1):
            for letter in letter_list:
                yield letter + word


max_consecutive_length = 2

total_valid_names = 0

for worldlen in range(1, 8):
    current_len_names = 0
    print("Writing names of length {}".format(worldlen))
    with open("names_{}.txt".format(worldlen), "w") as f:
        names = list(all_words(worldlen))
        validnames = []

        for name in names:
            valid = True
            for letter in name:
                fragment = ''
                for i in range(max_consecutive_length + 1):
                    fragment += letter
                if name.__contains__(fragment):
                    valid = False
            if valid:
                # validnames.append(name)
                total_valid_names += 1
                current_len_names += 1
                # f.write(name + "\n")
    print("Valid names of length {}: {}".format(worldlen, current_len_names))

print("Total valid names:\n{0:} or approx. {0:.2e}".format(total_valid_names))
