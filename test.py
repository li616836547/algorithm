import random
import collections

class Solution:
    def InversePairs(self, data):
        # write code here
        length = len(data)
        count = 0
        for i in range(length):
            for j in range(i+1, length):
                if data[i] > data[j]:
                    count += 1
        if count > 1000000007:
            count = count % 1000000007
        return count

    def GetNumberOfK(self, data, k):
        # write code here
        def find(data, k, left, right):
            if left > right-1:
                return None
            mid = (left + right) // 2
            if data[mid] == k:
                return mid
            if data[mid] < k:
                return find(data, k, mid + 1, right)
            if data[mid] > k:

                return find(data, k, left, mid)

        index = find(data, k, 0, len(data)-1)
        count = 1 if index else 0
        if index:
            label1, label2 = index, index
            while label1 >= 1:
                label1 = label1 - 1
                if data[label1] == k:
                    count = count + 1
            while label2 < len(data)-1:
                label2 = label2 + 1
                if data[label2] == k:
                    count = count + 1
        return count

    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        l = []
        while pHead1:
            l.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            if pHead2 in l:
                return pHead2
            else:
                pHead2 = pHead2.next
        return None

    def FindNumsAppearOnce(self, array):
        # write code here
        import collections
        a = collections.Counter(array)
        l = []
        for item in a:
            if item[1] == 1:
                l.append(item[0])
        return l

    def Rematch(self, s, pattern):
        def judge(i, j):
            if pattern[j] == s[i] or pattern[j] == '.':
                return True
            else:
                return False

        def match_core(i, j):
            if i != len(s) and j == len(pattern):
                return False
            if j == len(pattern) and i == len(s):
                return True
            if j < len(pattern)-1 and pattern[j + 1] == '*':
                if i == len(s) or not judge(i, j):
                    return match_core(i, j + 2)
                else:
                    return match_core(i, j+2) | match_core(i+1, j) | match_core(i+1, j+2)
            elif i != len(s) and judge(i, j):
                return match_core(i+1, j+1)
            return False

        # main
        i, j = 0, 0
        return match_core(i, j)

    def isNumeric(self, s):
        if not s:
            return False
        i = 0
        int_list = list(map(str, range(10)))
        special_chars = ['e', 'E', '.']
        while i < len(s):
            if i == 0 and len(s) > 1 and s[i] in ['+', '-']:
                i += 1
                # if s[i] not in int_list:
                #     return False
            elif s[i] in int_list:
                i += 1
            elif s[i] == '.' and i < len(s)-1 and s[:i].count('E') == 0 and s[:i].count('e') == 0:
                i += 1
                if s[i] not in int_list:
                    return False
            elif s[i] in ['E', 'e'] and i < len(s)-1:
                i += 1
                if s[i] not in int_list:
                    if s[i] in ['+', '-'] and i < len(s)-1:
                        i += 1
                        # if s[i] not in int_list:
                        #     return False
                    else:
                        return False
            else:
                return False
        for j in special_chars:
            if s.count(j) > 1:
                return False
        return True




if __name__ == '__main__':
    a = Solution()
    a.GetNumberOfK([1,3,3,3,3,4,5], 2)
