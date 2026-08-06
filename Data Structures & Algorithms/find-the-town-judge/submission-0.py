class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # the judge has everybody trusting him
           # n - 1 people are trusting him (not himself)
        # the judge trusts nofor in,body
           # = 0 trusts (no edges pointing to anybody)

        incoming = {}
        outgoing = {}

        for x in range(n):
            incoming[x+1] = 0
            outgoing[x+1] = 0

        for o, i in trust:
            outgoing[o] += 1
            incoming[i] += 1

        # find people with n-1 incoming
        for i in range(1,n+1):
            if incoming[i] == n-1:
                if outgoing[i] == 0:
                    return i
        return -1

        
