#Set .union() Operation

eng_stud = input()
s_id_e = input().split()
french_stud = input()
s_id_f = input().split()

e = set(s_id_e)
f = set(s_id_f)

print(len(e.union(set(f))))