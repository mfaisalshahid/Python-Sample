def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    ans = collections.defaultdict(list)
    print ans
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()
  
  
# Time Complexity: O(NK \log K)O(NKlogK), where NN is the length of strs, and KK is the maximum length of a string in strs. The outer loop has complexity O(N)O(N) as we iterate through each string. Then, we sort each string in O(K \log K)O(KlogK) time.

# Space Complexity: O(NK)O(NK), the total information content stored in ans.
