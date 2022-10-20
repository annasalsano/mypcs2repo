#Set .add()

n_country = int(input())
set_countries = set()

for n in range(n_country):
    country = input()
    set_countries.add(country)
    
print(len(set_countries)) 