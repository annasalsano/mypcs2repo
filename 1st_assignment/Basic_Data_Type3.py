#Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student = {}
    for std in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student[name] = scores
    query_name = input()
    
    for nm in student:
        if nm == query_name:
            name = query_name
            mean = sum(student[name])/len(scores)
            print(f'{mean:.2f}')