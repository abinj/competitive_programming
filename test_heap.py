import heapq

heap = []

#inserting elements
heapq.heappush(heap, 10)
heapq.heappush(heap, 70)
heapq.heappush(heap, 5)
heapq.heappush(heap, 35)
heapq.heappush(heap, 50)


#popping the smallest value
minimum = heapq.heappop(heap)
print(minimum)



num1 = 10
num2 = 20
print(num1^num2)
print(num1 << 2)



my_list = [9, 8, 7]
new_list = [[x for x in[my_list]] for x in range(3)]
print (new_list)

my_list = [a for a in range(7)]
new_list = [a for a in range(10) if a in my_list and a%2==0]
print(new_list)


my_tuple = (2e-04, True, False, 18, 1.7, True)
val = 0
for a in my_tuple:
  val += int(a)
print(val)


my_dict = dict()
for i in range (3):
  for j in range(2):
    my_dict[i] = j
print(my_dict)


def grade_stats(lis):
    # If the passed-in list is empty, your function should return an empty dictionary.

    # Insert your code here
    out = {}
    for i in lis:
        if i in out:
            out[i] = out.get(i) + 1
        else:
            out.update({i: 1})
    return out
    pass


print(grade_stats(['A', 'I', 'C', 'C', 'E', 'B', 'A', 'E', 'E', 'A', 'B', 'B', 'B']))


