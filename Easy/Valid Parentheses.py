from queue import LifoQueue
class Solution:
    def isValid(self, s: str) -> bool:
        par = ['(', ')', '[', ']', '{', '}']
        last = 0
        curr =  LifoQueue(maxsize= len(s)// 2 + 1)
        if bool(len(s)%2):
            return False    
        for i in range(len(s)):
            for j in range(len(par)):
                if s[i] == par[j]:
                    if curr.full():
                        return False
                    if bool((j + 1) % 2):
                        curr.put(j // 2)
                    else:
                        if curr.empty():
                            return False
                        last = curr.get()
                        curr.put(last)
                        if last == j // 2:
                            last = curr.get()
                        else:
                            return False
        return curr.empty()
