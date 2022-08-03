def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        if s==t:
            return True
        if len(s)>len(t):
            return False
        slen=len(s)
        tlen=len(t)
        i,j=0,0
        while i<slen and j<tlen:
            if s[i]==t[j]:
                j+=1
                i+=1
            else:
                j+=1
        if i<slen :
            return False
        elif j==tlen and s[i-1]!=t[j-1]:
            return False
        else:
            return True
