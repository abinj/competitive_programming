from collections import Counter

arr = ['f', 'l', 'e', 'a']
str = "donutsandwafflemakemehungry"


#shortest substring that contains all the characters in arr
def t_in_substring(t, substring):
    for i in t:
        if i not in substring:
            return False
    return True


def shortest_unique_substring(t, s):
    if not s or not t or len(s) < len(t):
        return ''

    left= 0
    right = 1
    ans = ""

    while(right < len(s)):

        if t_in_substring(t, s[left:right]):
            if not ans :
                ans = s[left:right]
            elif len(s[left:right]) < len(ans):
                ans = s[left:right]
            if (left + 1) != right:
                left += 1
            else:
                right += 1
        else:
            right += 1
    return ans




print(shortest_unique_substring(arr, str))








