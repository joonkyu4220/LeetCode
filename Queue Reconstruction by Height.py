class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_people = sorted(people)
        people = [0 for _ in range(len(people))]
        vis = [1 for _ in range(len(people))]
        cur = -1
        count = -1
        for person in sorted_people:
            start = start + 1 if person[0] == cur else -1
            cur = person[0]
            count = start
            for i in range(len(vis)):
                if vis[i]:
                    count += 1
                    if count == person[1]:
                        vis[i] = 0
                        people[i] = person
                        break
        return people
