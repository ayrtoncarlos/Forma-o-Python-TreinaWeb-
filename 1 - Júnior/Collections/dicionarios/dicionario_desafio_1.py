if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]
    
    dic = {}
    
    for i in range(n):
        letter = input()
        if letter in dic.keys():
            temp = dic[letter]
            temp.append(str(i+1))
            dic[letter] = temp
        else:
            dic[letter] = [str(i+1)]
    
    for _ in range(m):
        letter = input()
        
        if letter in dic.keys():
            print(' '.join(dic[letter]))
        else:
            print(-1)
