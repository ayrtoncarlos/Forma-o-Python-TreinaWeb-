from array import array

if __name__ == "__main__":
    n = int(input())
    a = array('b')
    for i in range(n):
        num = int(input())
        a.insert(i, num)
    for num in a:
        print(num)
