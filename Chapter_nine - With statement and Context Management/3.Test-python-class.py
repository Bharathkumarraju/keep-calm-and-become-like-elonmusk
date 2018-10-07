from dbcm import UseDataBase


dbconfig = {
    'host': '127.0.0.1',
    'user': 'wordsearch',
    'password': 'wordsearchpassword',
    'database': 'wordsearchlogDB'
}
print("")
with UseDataBase(dbconfig) as cursor:
    _SQL = """show tables"""
    cursor.execute(_SQL)
    data = cursor.fetchall()

print(data)

