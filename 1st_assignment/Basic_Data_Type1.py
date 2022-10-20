#Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    my_list = list(set(arr))
    max_value = max(my_list)
    my_list.remove(max_value)
    
    newmaxvalue = max(my_list)
    print(newmaxvalue)