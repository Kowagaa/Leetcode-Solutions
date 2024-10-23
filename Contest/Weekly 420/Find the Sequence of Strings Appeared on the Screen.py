class Solution:
    def stringSequence(self, target: str) -> List[str]:
        sel = "abcdefghijklmnopqrstuvwxyz"
        curr_char = 0
        curr = "a"
        out = ["a"]
        count = 0
        while target != curr:
            if curr[count] == target[count]:
                count += 1
                curr += "a"
                curr_char = 0
            else:
                curr_char += 1
                curr = curr[:-1] + sel[curr_char]
            out.append(curr)
        return out
