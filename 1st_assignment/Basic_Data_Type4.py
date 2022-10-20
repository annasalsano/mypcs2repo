#Lists

if __name__ == '__main__':
    N = int(input())
    numbers = []
    for n in range(N):
        comm, *s = input().split()
        if comm == 'insert':
            numbers.insert(int(s[0]), int(s[1]))
        elif comm == 'remove':
            numbers.remove(int(s[0]))
        elif comm == 'append':
            numbers.append(int(s[0]))
        elif comm == 'sort':
            numbers.sort()
        elif comm == 'pop':
            numbers.pop()
        elif comm == 'reverse':
            numbers.reverse()
        elif comm == 'print':
            print(numbers)