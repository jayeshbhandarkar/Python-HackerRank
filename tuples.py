import builtins
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    #x=hash(t)
    #print(x)
    print(hash(t))
