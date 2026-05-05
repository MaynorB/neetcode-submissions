class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lis = []
        c = Counter(nums)
        hee = c.most_common(k)
        for he in hee:
            lis.append(he[0])
        return lis