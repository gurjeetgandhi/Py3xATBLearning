print()

# self - concept in oops which points to itself - ignore
# *args - unlimited number of arguments * - string, float, int, boolean....
# sep=' ' - How we want to seperate the arguments ,, default seperator is one whitespace.
# end= '\n' - in the end what you want to do, if end is not used by default a new line is added.
# file=None - File IO

print("hello","world","kaur","True","1234","3.14", sep='_')
print("hello","world","kaur","True","1234","3.14", sep='_', end="--")

# if end is not used by default a new line is added.
print("\nhello","gurjeet","kaur", end="")
print("hello","gurjeet","kaur")

# Use end
print("hello","test", sep=" ", end="\t")
