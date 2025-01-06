def count_substring(string, sub_string):
    count = 0
    start = 0

    while start < len(string):
        start = string.find(sub_string, start)
        
        if start == -1:
            break
            
        count += 1
        start += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
