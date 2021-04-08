from collections import deque

FLIPPED = {"{": "}", "[": "]", "(": ")"}

def is_paired(input_string):
    stack = deque()
    for c in filter(lambda c: c in "{[()]}", input_string):
        if c in "{[(":
            stack.append(c)
        elif c in ")]}":
            try:
                match = stack.pop()
                if FLIPPED[match] != c:
                    return False
            except IndexError:
                return False
    return len(stack) == 0

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        string = input()
        if is_paired(string):
            print('Balanceada')
        else:
            print('Não balanceada')
