#Nested Lists

if __name__ == '__main__':
    nest_list = []
    scores = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        nest_list.append([name,score])
        
        scores.append(score)
        
    mini = set(scores)
    minscore = min(mini)
    mini.remove(minscore)
    newmin = min(mini)
    
    names = []
    
    for el in nest_list:
        if el[1] == newmin:
            names.append(el[0])
        
    print('\n'.join(sorted(names))) 