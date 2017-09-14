"""
이름 : assignment3_20171640
조건 :
– find 명령 추가 -> 명령어 추가, 예외처리 추가
– inc 명령 추가 -> 명령어 추가, 예외처리 추가
– del 명령 수정 -> 같은 이름 모두 삭제하도록 수정
– Error 처리 최대로 하기 -> 오류로 인해 프로그램이 종료되지 않게 수정
"""

# 외부 모듈 불러오기
import sys
import pickle

# 테스트를 위한 고정 입력
# f_name = input("enter data file name:")
file_name = 'test3_4.dat'


def read():
    """데이터베이스 읽기"""
    try:  # 없는 파일 예외 처리
        f = open(file_name, "rb")
    except FileNotFoundError:
        print("no such file:" + file_name)
        sys.exit()  # 파일이 없으면 종료

    wordcount = []  # pickle
    try:  # 빈 공간 예외처리
        wordcount = pickle.load(f)
    except:
        print("empty db:\t", file_name)
    else:
        print("open db:\t", file_name)
    f.close()
    return wordcount  # 리스트 반환


def write(wordcount):
    """데이터베이스 쓰기"""
    f = open(file_name, "wb")  # 이진파일 쓰기 모드
    pickle.dump(wordcount, f)
    f.close()


def do(db):
    """메인 명령"""
    try:  # 메인 예외처리
        while True:
            input_str = (input("Score DB > "))
            if input_str == "":
                    continue
            parse = input_str.split(" ")
            if parse[0] == 'add':
                record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                db += [record]
                print("성공적으로 db에 추가되었습니다.")
            elif parse[0] == 'del':
                for p in db:
                    if p['Name'] == parse[1]:
                        db.remove(p)
                        print("성공적으로 db에서 삭제되었습니다.")
                    else:
                        print("잘못된 요청입니다.")  # 없는 사람 예외 처리
                        do(db)
            elif parse[0] == 'show':
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                show(db, sortKey)
            elif parse[0] == 'find':
                for p in db:
                    if p['Name'] == parse[1]:
                        print("성공적으로 해당 사용자를 찾았습니다.")
                    else:
                        print("잘못된 요청입니다.")  # 없는 사람 예외 처리
                        do(db)
            elif parse[0] == 'inc':
                for i in range(len(db)):
                    if db[i]['Name'] == parse[1]:
                        db[i]['Score'] = str(int(db[i]['Score'])+int(parse[2]))
                        print("성공적으로 amount만큼 해당 사용자에게 추가했습니다.")
            elif parse[0] == 'quit':
                print("안전하게 종료합니다.")
                exit(0)
            else:  # 틀린 명령어 예외 처리
                print("input error! by Invalid command: " + parse[0])
    except Exception as ex:
        print("main error! by", ex)  # 오류난 이유를 출력
        do(db)
    else:
        do(db)

def show(db, keyname):
    """데이터베이스 출력"""
    try:  # 예외처리
        for p in sorted(db, key=lambda person: person[keyname]):
            for attr in sorted(p):
                print(attr + "=" + p[attr], end=' ')
            print()
    except Exception as ex:
        print("output error! by", ex)  # 오류난 이유를 출력


db = read()
try: # 예외 처리 후 재시작
    do(db)
except Exception as ex:
    print("critical error! by", ex)  # 오류난 이유를 출력
    print("다시 실행을 시도합니다...")
    do(db)
else:
    do(db)
