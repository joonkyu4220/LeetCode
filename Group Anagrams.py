class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        alphabets = 'qwertyuiopasdfghjklzxcvbnm'
        anagramDic = {}
        for s in strs:
            dic = {}
            key = ""
            for c in s:
                if c in dic:
                    dic[c] += 1
                else:
                    dic[c] = 1
            for a in alphabets:
                if a in dic:
                    key += a + str(dic[a])
            if key in anagramDic:
                anagramDic[key].append(s)
            else:
                anagramDic[key] = [s]
        
        return anagramDic.values()
      
      
      
      
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorteds = []
        groups = []
        
        for s in strs:
            sort = sorted(s)
            check = False
            for i in range(len(sorteds)):
                if sorteds[i] == sort:
                    groups[i].append(s)
                    check = True
                    break
            if not(check):
                groups.append([s])
                sorteds.append(sort)
        
        return groups
