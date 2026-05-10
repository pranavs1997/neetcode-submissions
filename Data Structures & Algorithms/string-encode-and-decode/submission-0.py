class Solution:

    def encode(self, strs: List[str]) -> str:
        str1 = ""
        for s in strs:
            str1 = str1 + str(len(s)) + "#" + s
        return str1

    def decode(self, s: str) -> List[str]:
        # for i in range(len(s)):
        #     if s[i].isnumeric() and s[i+1] == "#":
        #         skip = int(s[i])
        #         sub_str = s[i+2: skip + 2]
        #         list_str.append(sub_str)
        #         i = i + skip + 1
        #     else:
        #         continue
        # return list_str
        list_str, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            skip = int(s[i:j])
            sub_str = s[j+1: j + skip + 1]
            list_str.append(sub_str)
            i = j + skip + 1
        return list_str

