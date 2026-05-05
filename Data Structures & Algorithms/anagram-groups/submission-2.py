class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = []
        length = len(strs)
        for i in range(length):
            dummy = [strs[i]]
            if strs[i] == None:
                continue
            for j in range(i + 1, length):
                if Counter(strs[i]) == Counter(strs[j]) and strs[j] != None and strs[i] != None :
                    dummy.append(strs[j])
                    strs[j] = None
            sol.append(dummy)
        print(sol)
        return sol