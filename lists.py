if __name__ == '__main__':
    list=[]
    n = int(input())
    
    for _ in range(n):
        command=input().split()
        
        if command[0]=="insert":
            i,e=map(int,command[1:])
            list.insert(i,e)
            
        elif command[0]=="print":
            print(list)
            
        elif command[0]=="remove":
            e=int(command[1])
            list.remove(e)
            
        elif command[0]=="append":
            e=int(command[1])
            list.append(e)
            
        elif command[0]=="sort":
            list.sort()
            
        elif command[0]=="pop":
            list.pop()
            
        elif command[0]=="reverse":
            list.reverse()
