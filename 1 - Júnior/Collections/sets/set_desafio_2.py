if __name__ == '__main__':
    N = int(input())
    
    names = []
    
    for _ in range(N):
        name = input()
        names.append(name)
    
    names = sorted(set(names))
    
    for name in names:
        print(name)
