N = int(input())

nested_list = []

for _ in range(N):
    array = input().split()
    nested_list.append(array)

M = int(input())

for _ in range(M):
    x, y = (int(i) for i in input().split())
    
    if x < len(nested_list):
        if y < len(nested_list[x-1]):
            print(nested_list[x-1][y])
        else:
            print('ERRO!')
    else:
        print('ERRO!')
