print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

# escape 문자인 \ (백슬래시) 앞에 \ 백슬래시를 한번더 사용(\\) 해야 
# \ 가 출력되기 때문에 \ 출력을 원하는 곳에 \\로 써주었음

# 그 외의 이스케이프 문자
# \n 줄바꿈  \t 탭   \b 백스페이스   \000 널문자
# \\ \  \" 큰따옴표     \r 줄바꿈, 커서를 앞으로 이동
# \f 줄 바꿈, 커서를 다음 줄로 이동
# \a 벨소리     \v 수직탭

# raw string을 이용하여 이스케이프 문자를 무시하고 사용할 수도 있다.
# print(r'\\hello\nworld\\') 를 출력하면
# \\hello\nworld\\ 
# 이렇게 출력됨