import mysql.connector

dbconfig = {
    'host': '127.0.0.1',
    'user': 'wordsearch',
    'password': 'wordsearchpassword',
    'database': 'wordsearchlogDB'
}
conn = mysql.connector.connect(**dbconfig)

cursor = conn.cursor()

_SQL = """show tables"""
cursor.execute(_SQL)

res = cursor.fetchall()

print(res)

_SQL1 = """describe log"""
cursor.execute(_SQL1)
res1 = cursor.fetchall()
print(res1)

def spaces(number):
    for i in range(number):
        print("")
spaces(5)

for row in res1:
    print(row)


_SQL2 = """insert into log(phrase, letters, ip, browser_string, results) values(%s, %s, %s, %s, %s)"""
cursor.execute(_SQL2, ('hanuman', 'anajani nandhana', '127.0.0.1','safari','set()'))

conn.commit()

_SQL3 = """insert into log(phrase, letters, ip, browser_string, results) values('anjaneyam', 'Maharaj', '127.0.0.1', 'Firefox', "{'e', 'i'}")"""
cursor.execute(_SQL3)



conn.commit()

_SQL4 = """select * from log"""
cursor.execute(_SQL4)
for row in cursor.fetchall():
    print(row)



cursor.close()
conn.close()


