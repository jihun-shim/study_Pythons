class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name=name
        self.phone_name=phone_number
        self.email=email
        self.addr=addr

    def print_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_name)
        print("이메일:", self.email)
        print("주소;", self.addr)
        print('----------------------------')
#------------------------------------------------------
#입력받는 함수

def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu=input('메뉴선택:') # 1~4 입력받기
    return int(menu)

# 입력받는 함수
def set_contact():
    # 여기에 코드 작성
    name = input('이름 : ')
    phone_number = input('전화번호 : ')
    email = input('이메일 : ')
    addr = input('주소 : ')
    # print(name, phone_number, email, addr)

    contact = Contact(name, phone_number, email, addr)
    return contact
# 주소록 전체를 출력하는 함수
def print_contact(contact_list):
    # 여기에 코드 작성
    for contact in contact_list:
        contact.print_info() # 각 객체 (인스턴스)의 print_info()함수가 호출

#주소록에서 삭제하는 함수
def delete_contact(contact_list, name):
    # 여기에 코드 작성
    for i, contact in enumerate(contact_list):
        if contact.name == name :
            del contact_list[i]

#실행
def run():
    # Contact 인스턴스를 저장할 리스트 자료구조 생성
    contact_list = []
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            contact = set_contact()
            contact_list.append(contact)
        elif menu==2: # 출력을 선택하면
            print_contact(contact_list)
        elif menu==3: # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(contact_list,name)


if __name__ == "__main__":
    run()