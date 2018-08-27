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






