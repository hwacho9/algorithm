import sys

# sys.stdin을 사용하여 표준 입력을 읽습니다.
input_string = sys.stdin.read()

# 입력 문자열을 공백으로 분리하여 단어 리스트를 생성합니다.
words = input_string.split()

# 각 단어가 대문자 또는 숫자로 시작하는지 확인하고, 그런 단어를 집합에 추가합니다.
# 이렇게 하면 중복된 단어는 하나로 취급됩니다.
unique_words = {word for word in words if word[0].isupper() or word[0].isdigit()}

# 집합에 있는 단어의 수를 계산합니다.
count = len(unique_words)

# 계산된 단어의 수를 sys.stdout을 사용하여 표준 출력에 출력합니다.
sys.stdout.write(str(count))