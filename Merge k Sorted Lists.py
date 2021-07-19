# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def sortByFirstVal(listsSorted, newListNode):
            if (newListNode is None):
                return listsSorted
            if len(listsSorted) == 0:
                return [newListNode]
            l = 0
            r = len(listsSorted) - 1
            val = newListNode.val
            mid = (l + r) / 2
            while (l < mid):
                if listsSorted[mid].val > val:
                    r = mid
                else:
                    l = mid
                mid = (l + r) / 2
            if val <= listsSorted[l].val:
                return listsSorted[:l] + [newListNode] + listsSorted[l:]
            elif val >= listsSorted[r].val:
                return listsSorted[:r+1] + [newListNode] + listsSorted[r+1:]
            else:
                return listsSorted[:l+1] + [newListNode] + listsSorted[l+1:]
        if len(lists) == 0:
            return None
        ans = ListNode(None, None)
        cur = ans
        listsSorted = list()
        for listnode in lists:
            listsSorted = sortByFirstVal(listsSorted, listnode)
        while (len(listsSorted)):
            cur.next = listsSorted[0]
            listsSorted = sortByFirstVal(listsSorted[1:], listsSorted[0].next)
            cur = cur.next
        return ans.next
        
        # def argminListNode(heads):
        #     len_ = len(heads)
        #     minIdx = None
        #     for i in range(len_):
        #         if heads[i] is None:
        #             continue
        #         else:
        #             if minIdx is None:
        #                 minIdx = i
        #             else:
        #                 if heads[i].val < heads[minIdx].val:
        #                     minIdx = i
        #     return minIdx
        # dummy = ListNode(None, None)
        # cur = dummy
        # minIdx = argminListNode(lists)
        # while (minIdx is not None):
        #     cur.next = lists[minIdx]
        #     cur = cur.next
        #     lists[minIdx] = lists[minIdx].next
        #     if lists[minIdx] is None:
        #         lists = lists[:minIdx] + lists[minIdx + 1:]
        #     minIdx = argminListNode(lists)
        # return dummy.next
            
            
#         def mergeTwo(l1, l2):
#             dummy = ListNode(None, None)
#             cur = dummy
#             while ((l1 is not None) and (l2 is not None)):
#                 if l1.val < l2.val:
#                     cur.next = l1
#                     cur = cur.next
#                     l1 = l1.next
#                 else:
#                     cur.next = l2
#                     cur = cur.next
#                     l2 = l2.next
#             if l1 is None:
#                 cur.next = l2
#                 return dummy.next
#             elif l2 is None:
#                 cur.next = l1
#                 return dummy.next
            
#         sortedList = None
#         for listnode in lists:
#             sortedList = mergeTwo(sortedList, listnode)
        
#         return sortedList
