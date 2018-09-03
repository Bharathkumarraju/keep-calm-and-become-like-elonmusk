'''
Lists are full-blown python collection objects.
This means that lists comes with ready-to-use functionality in the form of list methods
like len append pop extend remove insert
'''

movies = ["The lord of the rings","the hobbit","the slum dog millionaire","the titanic","the dark night rises"]
print("")
print(movies)

print("")

print(movies[2])

print(movies[0])

print(movies[4])

print("")
# use length method
print("length of the movies")
print(len(movies))

# use append method
movies.append("Bahubali the conclusion")
print(movies)

#use pop method
movies.pop()
print(movies)

#use extend method
movies.extend(["Bahubali the beginning","Bahubali the conclusion"])
print(movies)
print(len(movies))

#use remove method
movies.remove("Bahubali the beginning")
print(movies)

#use insert method
movies.insert(1,"Geetha Govindham")
print(movies)

#use reverse
movies.reverse()
print(movies)

#use index
movies.sort()
print(movies)

print("")
#use count
movies.count(movies)
print(movies)

'''
Python lists contain data of mixed type
'''

movies.insert(1,"1975")
print(movies)

movies.insert(3,"1878")
movies.insert(5,"1991")
movies.insert(7,"2001")
movies.insert(9,"2010")
movies.insert(11,"2011")
movies.insert(13,"2016")
print(movies)
print("")

print("use of for loop")
print("")
# Time to use for loop
for fav_movies in movies:
    print(fav_movies)

print("")
print("")
print("use of while loop")
print("")
# how to use while loop
count = 0
while count < len(movies):
    print(movies[count])
    count = count+1


print("")
print(movies[2])

print("")
print(movies)



