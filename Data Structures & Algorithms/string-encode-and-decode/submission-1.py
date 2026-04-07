class Solution:

    def encode(self, strs: List[str]) -> str:
        res_list = []
        for i in strs:
            res_list.append(str(len(i)))
            res_list.append('#')
            res_list.append(i)
        return (''.join(res_list))


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            j+=1
            res.append(s[j:j+length])
            i = j + length
        return res

