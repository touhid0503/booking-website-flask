list = []
n = int(input())
for i in range(n):
    x = input()
    list.append(x)
    # print(x);

# for x in list:
#     print(x)
lis = list.copy()
lis.reverse()
if lis == list:
    print(1)
else:
    print(0)
