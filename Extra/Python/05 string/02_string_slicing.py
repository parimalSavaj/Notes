# slicing string

# Example: sl = name[ start_inx : end_inx : jump] her jump is option.
# start_inx included.
# end_inx is not included.

name = "parimal"
print(name[0:3])
print(name[1:3])
print(name[-4:-1]) # negative slicing also support.

print(name[:3]) # start_ind not mention so it means 0 so here 0:3
print(name[2:]) # same here but end part included

print(name[0:4:2])