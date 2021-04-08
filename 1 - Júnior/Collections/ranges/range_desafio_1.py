def decrescentes():
    return range(10, 0, -1)

def pares():
    return range(2, 51, 2)

if __name__ == '__main__':
    decrescentes = decrescentes()
    pares = pares()
    
    for item in decrescentes:
        print(item, end=' ')
        
    print()
    
    for item in pares:
        print(item, end=' ')
    
    print()