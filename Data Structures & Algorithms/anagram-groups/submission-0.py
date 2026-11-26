from itertools import groupby
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anags=[]
        
        indices=[]
        
        for i in strs:
            indices.append("".join(sorted(i)))
            index_dict = defaultdict(list)
        for idx, item in enumerate(indices):
            index_dict[item].append(idx)

        for val in index_dict.values():
            group=[]
            for j in range(len(val)):
                group.append(strs[val[j]])
            anags.append(group)

        return anags