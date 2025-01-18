
OPENED = ["(", "[", "{"]
CLOSED = [")", "]", "}"]

def check(text):
    symbols = []
    for symbol in text:
        if symbol in OPENED:
            symbols.append(symbol)
        if symbol in CLOSED:
            try:
                last = symbols.pop()
                index = CLOSED.index(symbol)
                if last != OPENED[index]:
                    return False
            except IndexError:
                return False
    
    return len(symbols) == 0
    


data = [
    "] [",
    "( 22 ( 1))",
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3)",
    "( 11 }"
]

for text in data:
    print(f"Is simetric? {'YES' if check(text) else 'NO'}")
