import re
p = re.compile("ca.e")

def print_match(m):
    if m:
        print("m.group(): ", m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string) # 입력 받은 문자열
        print("m.start():",m.start()) # 일치하는 문자열의 시작
        print("m.end():", m.end()) # 일치하는 문자열의 끝
        print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝
    else:
        print("매칭되지 않음")

#m = p.search("good care")
#print_match(m)

lst = p.findall("careless cafe")
print(lst)