if __name__ == '__main__':
    A = {int(i) for i in input().split()}
    B = {int(i) for i in input().split()}

    for i in (A ^ B):
        print(i)
