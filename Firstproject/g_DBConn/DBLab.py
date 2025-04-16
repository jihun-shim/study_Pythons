# 데이터베이스로 저장(변경)
# 사원 테이블에 입력 및 삭제하는 프로그램
import cx_Oracle as oci
import csv

# Oracle DB 연결 정보
conn_str = 'scott/tiger@localhost:1521/finDB'

# 입력기능
def insert_employee():
    # 데이터 입력
    bun = int(input("사번입력-> "))
    name = input("이름입력-> ")
    job = input("직책입력-> ")
    deptno = input("부서번호-> ")
    try:
        conn = oci.connect(conn_str)
        cur = conn.cursor()
        sql = "insert into dbtest(bun, name, job, deptno) values(:0, :1, :2, :3)"
        cur.execute(sql,(bun,name,job,deptno))
        conn.commit()
        print('사원 정보가 입력되었습니다.')
    except oci.DatabaseError as e:
        print('입력시 오류발생 : '+ e)
    finally:
        if cur: cur.close()
        if conn: conn.close()

# 출력기능
def select_all_employees():
    try:
        conn = oci.connect(conn_str)
        cur = conn.cursor()
        sql="select * from dbtest"

        # 결과 출력
        print("-----------------------")
        print("사번\t이름\t업무\t부서번호")
        print("-----------------------")
        cur.execute(sql)
        datas = cur.fetchall()
        for row in datas:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
        print("--------------------------")
    except oci.DatabaseError as e:
        print('사원정보 출력시 오류발생 : '+ e)
    finally:
        if cur: cur.close()
        if conn: conn.close()

# 삭제기능
def delete_employee():

    bun = int(input("삭제할 사원번호 입력 ->"))
    try:
        conn = oci.connect(conn_str)
        cur = conn.cursor()
        sql = "DELETE FROM dbtest WHERE bun = :1"
        cur.execute(sql,(bun,))
        conn.commit()
        print("사원정보가 삭제되었습니다.")
    except oci.DatabaseError as e:
        print('사원삭제시 오류발생 : '+ e)
    finally:
        if cur: cur.close()
        if conn: conn.close()

# 메뉴출력기능(함수)
def show_menu():
    while True:
        print("\n1. 사원정보 입력")
        print("2. 사원정보 출력")
        print("3. 사원정보 삭제")
        print("4. 종료")
        choice = input("메뉴선택: ")

        if choice == '1':
            insert_employee()
        elif choice == '2':
            select_all_employees()
        elif choice == '3':
            delete_employee()
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

# 프로그램 시작 함수
def main():
    show_menu() #메뉴 출력 및 기능 실행

if __name__ == '__main__': # 메인 함수 호출(시작점)
    main()




