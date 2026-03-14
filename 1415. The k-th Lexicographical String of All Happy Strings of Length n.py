class Solution:
    def getHappyString(self, n, k):
        next_letters = {
            'a': 'bc',
            'b': 'ac',
            'c': 'ab'
        }
        queue = ['a', 'b', 'c']
        while len(queue[0]) < n:
            u = queue.pop(0)
            for nxt in next_letters[u[-1]]:
                queue.append(u + nxt)
        if len(queue) < k:
            return ""
        return queue[k - 1]