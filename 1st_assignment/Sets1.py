#Introduction to Sets

def average(array):
    # your code goes here
    mean = sum(set(array))/len(set(array))
    return float(mean)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)