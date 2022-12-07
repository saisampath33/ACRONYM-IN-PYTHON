#function
def fxn(stng):
    # add first letter
    oupt = stng[0]

    # iterate over string
    for i in range(1, len(stng)):
        if stng[i - 1] == ' ':
            # add letter next to space
            oupt += stng[i]

    # uppercase oupt
    oupt = oupt.upper()
    return oupt


# input string
inpt1 = str(input('Enter the name:'))

# output acronym
print(fxn(inpt1))

# input string
inpt2 = str(input('enter the name:'))

# output acronym
print(fxn(inpt2))

# input string
inpt3 = str(input('enter the name:'))

# output acronym
print(fxn(inpt3))