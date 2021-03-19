#Basic Python Part 1
#This is a comment
"""
This is just a file I created while skimming w3schools
reading the python items. I have it saved as a .py file but if you run it
it will just close out for no reason. Again, still learning all of this stuff.
-
My goal is to create a script to check up on Ubuntu based system variables. Like uptime, hostname, cpu usage, and memory usage.
No logging, just print the information. Simple, basic, good idea to learn on.
"""

#These are global variables. I have the type declared for two but you don't have too. Also they can be changed aftewrwards.
x = int(128)
y = int(256)
z = "X is a smaller value"
#Z will not overwrite z, so thats cool. Casing matters.
Z = "Y is a larger value"

print("Get the data type for global variable x")
print(type(x))

if x > y:
	print(z)
if y > x:
	print("y is larger than x")
