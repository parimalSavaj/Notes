name = "parimal"
a = ""
b = "savaj Parimal"
c = "savaj parimal"
d = "parimal savaj Pari mal pari-pari"

# to find length of string.
print(len(name)) # return integer value.
print(len(a))

# to check ending with string.
print(name.endswith("mal")) 
print(name.endswith("pari")) # return boolean value

# same check starting string
print(name.startswith("pari")) # return boolean value
print(name.startswith("Pari")) # this function case 

# convert any string to staring character capital and other same string to small 
print(name.capitalize())
print(b.capitalize())

# same like capitalize but this method convert every word first character to capital
print(b.title())
print(c.title())

# inside string find any word
print(c.find("pari")) # return integer
print(c.find("abc")) # if not found searching values so return '-1'
print(d.find("pari")) # return only first matching value

# find and replace word
new_str = c.replace("pari","abc") # find first argument of method and replace to second argument
print(new_str)
old_str = c.replace("abc","xyz") # if not found finding values so not replace and back same string
print(old_str)
all_str = d.replace("pari","pqr") # replace all matching values
print(all_str)