
with open('lkos_demon_names.txt', 'r') as f:
     ls = f.readlines()
     
ls = [name.strip().split(' ')[1] for name in ls[:-1]]

ls = list(set(ls))[1:]
    
with open('lkos_demon_names.txt', 'w') as f:
      f.writelines('\n'.join(ls))

print(ls)