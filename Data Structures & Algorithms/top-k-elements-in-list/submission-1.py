from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        output = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
        result=list(output)
        return result[:k]