#Set .difference() Operation

n_en = int(input())
s_id_e = set(input().split())
n_fr = int(input())
s_id_f = set(input().split())

print(len(s_id_e.difference(s_id_f)))