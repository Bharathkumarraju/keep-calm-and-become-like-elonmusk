print("\n"*2)
for i in [ x*3 for x in [1, 2, 3, 4, 5]]:
    print("\t"*i, i)
print("\n"*2)

# when you replace the surrounding square brackets with parenthesis then it's called the generator

# Parentheses around code == Generator

# So What is the difference

# Here we go... When the listcomp executes, it produces all of it's data prior to any other processing occurring.

# below for loop doesn't start processing any of the data produced by the listcomp until the listcomp is done.
# This means that a listcomp that takes a long time to produce data delays any other code from running until the listcomp concludes

# With a small list of data items this is not a big issue.

# But imagine your listcomp is required to work with a list that produces the 10 million items of data. you've now got tow issues.
# 1. You have to wait for the listcomp to process those 10 million data items before doing anything else.
# 2. You have to worry that the computer running your listcomp has enough RAM to hold all the data in memory while the listcomp executes the 10 million individual pieces of data
# So if listcomp runs out of memory the interpreter terminates.

for i in (x*3 for x in [1, 2, 3, 4, 5, 6]):
    print("\t"*i, i)
print("\n"*2)

# So Generators produce data items one at a time.
# When we replace listcomp's square brackets with parentheses, the listcomp becomes the Generator.
# Unlike listcomp, which must conclude before any other code can execute, a generator releases data as soon as the data is produced by the generator's code.

# This means that if you generate 10 million data items, the interpreter only needs enough memory to hold one data item at a time.
# and any code that's waiting to consume the data items produced by the generator executes immediately. that is there is no waiting.