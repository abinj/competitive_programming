import random

print(random.random())

print(random.randint(1,5))

print(random.uniform(1,5))

str = "Hello"
print(len(str))

print(str[len(str) -1])
print(str[:-1])
print(str[-2:])
print(str[0:len(str):1])
print(str[0:len(str):2])
print(str[len(str):0:-2])

print(5.5/4.5)
print(int(5.8//4.5))

print(ord('C'))
print(bool(""))

triple = lambda num: num*3
print(triple(3))

concat_str = lambda a,b,c : a[0] + b[0] + c[0]
print((concat_str("Hello", "sir", "madam")))

highest = lambda num : "High" if num > 50 else "Low"
print(highest(40))

num_list = [0,1,2,3,4]
double_list = map(lambda num : num*2, num_list)
print(list(double_list))


greater_than_2 = list(filter(lambda num: num > 2, num_list))
print(greater_than_2)




def rec_count(number):
    print(number)

    if number == 0:
        return 0
    rec_count(number - 1)
    # print(number)

rec_count(5)

for i in range(1, 11, 2):
    print(i)




a=5
b=10
a=a^b
b=a^b
a=a^b
print(a,b)



lis = [1,2,3,4]
print(lis.pop(3))
print(lis.index(3))
lis.sort(reverse=True)
print(lis)

lis_double = [n *2 for n in lis]
print(lis_double)
lis_dble = [n*2 for n in lis if n%2 == 0]
print(lis_dble)


list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1+n2 > 100]
print(sum_list)