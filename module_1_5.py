immutable_var=9,12,'French', True
print(immutable_var)
immutable_var=([9,12,'French',True])
immutable_var[0]=4
print(immutable_var)
immutable_var[2]='German'
print(immutable_var)
immutable_var[3]=False
print(immutable_var)

mutable_list=['Kitten','Puppy','Culf']
print(mutable_list)
mutable_list[2]= 'Chicken'
print(mutable_list)
mutable_list.append(2025)
print(mutable_list)
mutable_list.extend('899')
print(mutable_list)
print(mutable_list[3:len(mutable_list)])



