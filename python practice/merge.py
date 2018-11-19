class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, l):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        l.sort(key=lambda x: (x.start))
        ret = []
        if len(l) > 0:
            curr = l[0]
            for i in range(1,len(l)):
                # expand processing range
                if l[i].start <= curr.end:
                    if l[i].end > curr.end:
                        curr.end = l[i].end
                # else push to ret, process new
                else:
                    ret.append(curr)
                    curr = l[i]
            ret.append(curr)
        return ret
             
run = Solution()
print(run.merge([Interval(1,4),Interval(4,5)]))
print(run.merge([Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)]))
