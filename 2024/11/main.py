import sys
from tqdm import tqdm
from collections import defaultdict

dic = defaultdict(int)

with open(sys.argv[1]) as file:
    numbers = file.read().split(' ')
    for n in numbers:
        dic[int(n)] += 1
    
for _ in range(int(sys.argv[2])):
    new_dic = defaultdict(int)
    for n in dic:
        if n == 0:
            new_dic[1] += dic[n]
        else:
            n_str = str(n)
            if len(n_str) % 2 == 0:
                mid_point = len(n_str) // 2 
                new_dic[int(n_str[:mid_point])] += dic[n]
                new_dic[int(n_str[mid_point:])] += dic[n]
            else:
                new_dic[n*2024] += dic[n]
    dic = new_dic
     
print(f'Total {sum(dic.values())}')
