# multiple line read
f = open("c.txt")

# lines = f.readlines()
# print(lines)

# single single line read

# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()

# print(line1)
# print(line2)
# print(line3)

f.close()

# append data
f2 = open("c.txt", "a")

str = "\nnew line";
f2.write(str)

f2.close()

# + mode for update

# rb mode for read in binary

# rt mode for read in text and this one is default