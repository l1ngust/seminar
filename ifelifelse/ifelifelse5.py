# num_str = str(input())
# num_int = int(num_str)
# last_num = num_str[int(len(num_str))-1]
# k = 0
#
# if len(num_str) > 1:
#     k = num_int
# else:
#     for i in range(len(num_str)):
#         k = k + int(num_str[i])
#
# if (int(last_num) % 2 == 0) and (k%3 == 0):
#     print(1)

def summ(a):
    return a*2

el = [1,2,3]

print(list(map(summ, el)))
