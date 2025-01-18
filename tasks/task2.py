from collections import deque

def is_palindrome(text: str):
    d = deque()
    for letter in text:
        if not letter == ' ':
            d.append(letter.lower()) 

    while True:
        try:
            right = d.pop()
            left = d.popleft()
            if right != left:
                return False
        except IndexError:
            return True


texts = [
    "",
    "A",
    "aB",
    "aB A",
    " A  b   B   a   ",
    "qwe  rt yt Rew Q",
    "asSA",
    "not tom"
]

for text in texts:
    print(f"Is palindrome? {'YES' if is_palindrome(text) else 'NO'}")
