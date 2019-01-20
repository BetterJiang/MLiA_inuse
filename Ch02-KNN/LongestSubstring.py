# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 20:37:27 2018
@author : HaiyanJiang
@email  : jianghaiyan.cn@gmail.com

LongestSubstring

"""


def lengthOfLongestSubstring_v1(s):
    """
    :type s: str
    :rtype: int
    """
    vs = ''
    sMax = ''
    for a in s:
        if a not in vs:
            vs += a
        else:
#            print(vs)
            if len(sMax) < len(vs):
                sMax = vs
            vs = a
    if len(sMax) < len(vs):
        sMax = vs
#    print(vs)
    return len(sMax)


s = "abcabcbb"
s = "pwwkewe"
s = '    '

s = "dvdf"

lengthOfLongestSubstring_v1(s)
# 这个结果是不对的。

# =============================================================================
# Algorithm1 - brute force
# Suppose we have a function boolean allUnique(String substring) which will
# return true if the characters in the substring are all unique, otherwise false.
#  We can iterate through all the possible substrings of the given string s and
#  call the function allUnique. If it turns out to be true, then we update our
#  answer of the maximum length of substring without duplicate characters.
# =============================================================================


def allUnique(s, start, end):
    vset = set()
    i = start
    while i < end:
        ch = s[i]
        if ch in vset:
            return False
        vset.add(ch)
        i += 1
    return True


def lengthOfLongestSubstring(s):
    n = len(s)
    ans = 0
    for i in range(0, n):  # renge(n), not include n.
        for j in range(i + 1, n + 1):
            if allUnique(s, i, j):
                ans = max(ans, j - i)
    return ans



for i in range(n):
    print(i)

s = "dvdfuj"
s = 'abcabcbbn'

start = 1
end = n

allUnique(s, start, end)

lengthOfLongestSubstring(s)



def lengthOfLongestSubstring_v2(s):
    # using hashset
    hashSet = set()  # only keep the longest unique successive string
    ans, i, j = 0, 0, 0
    n = len(s)
    while i < n and j < n:  # the index [0, n-1]
        # try to extend the range [i, j]
        if s[j] not in hashSet:
            hashSet.add(s[j])
            j += 1
            ans = max(ans, j - i)  # if switch ans = max(ans, j-i+1); j++
        else:
            hashSet.remove(s[i])
            i += 1
    return ans


s = "dvdfuj"
lengthOfLongestSubstring_v2(s)
lengthOfLongestSubstring_v31(s)


def lengthOfLongestSubstring_v31(s):
    # using hash map # mapping of characters to its index
    # keep the longest non-duplicate successive string from index i-{char:idx}
    hashMap = {}  # current index of character
    ans, i = 0, 0
    for j in range(len(s)):  # the index [0, n-1]
        # try to extend the range [i, j]
        if s[j] not in hashMap:
            hashMap[s[j]] = j
            ans = max(ans, j - i + 1)
        else:
            i = max(hashMap[s[j]], i)
            hashMap.pop(s[j])  # 错误原因应该是不需要pop
    return ans


s = "dvdfuj"
j = 0
j = 1
j = 2

def lengthOfLongestSubstring(s):
    # using hash map # mapping of characters to its index
    # keep the longest non-duplicate successive string from index i-{char:idx}
    # where i is not changing one by one
    hashMap = {}  # current index of character
    ans, i = 0, 0
    for j in range(len(s)):  # the index [0, n-1]
        # try to extend the range [i, j]
        if s[j] in hashMap:
            i = max(hashMap[s[j]] + 1, i)   # the max, j' + 1
        hashMap[s[j]] = j
        ans = max(ans, j - i + 1)
    return ans



s = "tmmzuxt"
lengthOfLongestSubstring(s)


s = "abba"
lengthOfLongestSubstring(s)

s = "abcabcbb"
lengthOfLongestSubstring(s)


