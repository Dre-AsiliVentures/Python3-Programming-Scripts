# Creating Tuples

#Method 1: Tuple Method
digits=(0,1,'Two')

print ("Method 1: Direct:\n\n      {}\n".format(digits))


#Method 2 : Tuples from lists
digits=tuple([0,1,'Two'])
print ("Method 2: Indirect using Lists:\n      {}".format(digits))
digits[0]='API'
