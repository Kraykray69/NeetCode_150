# Solution 1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            group[sortedS].append(s)

        return list(group.values())


grouping = Solution()
grouping.groupAnagrams(['act','cat','pots','hat','stop','x','dinosaur'])



# Solution 2
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            group[tuple(count)].append(s)

        return list(group.values())


grouping = Solution()
grouping.groupAnagrams(['act','cat','pots','hat','stop','x','dinosaur'])
