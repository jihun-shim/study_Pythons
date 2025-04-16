import cx_Oracle as oci

# 1) Connect 얻어오기
conn = oci.connect('scott/tiger@localhost:1521/finDB')
print(conn.version)

# 2) cursor 객체 얻어오기
cursor = conn.cursor()

# Oracle DB의 emp 테이블 검색(select)
# 3) SQL 명령
sql = 'select * from emp '

# 4) SQL 명령 실행
cursor.execute(sql)
datas = cursor.fetchall()
for row in datas:
    #print(row)
    print(row[0],row[1]) # 원하는 컬럼만.

# 5) cursor 객체 닫기
cursor.close()
    #if cursor: cursor.close()
# 6) Oracle 서버연결 끊기
conn.close()
    #if conn: conn.close()
