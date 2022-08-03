 if len(s)!=len(t):
            return False
        
        mt={}
        ms={}
        
        for i in range(len(s)):
            if s[i] in ms :
                if ms[s[i]]!=t[i]:
                    return False
            else:
                ms[s[i]]=t[i]
            
            if t[i] in mt :
                if mt[t[i]]!=s[i]:
                    return False
            else:
                mt[t[i]]=s[i]
        return True

#scratch works
'''
        if len(s)!=len(t):
            return False
        ds={}
        dt={}
        for i in s:
            if i in ds:
                ds[i]+=1
            else:
                ds[i]=1
        for i in t:
            if i in dt:
                dt[i]+=1
            else:
                dt[i]=1
        for i in range(len(s)):
            if ds[s[i]]!=dt[t[i]]:
                return False
        
            
        return True
        '''
        '''
        #character mapping:
        if len(s)!=len(t):
            return False
        d={}
        n=len(s)
        for i in range(n):
            if s[i] in d :
                if d[s[i]]!= t[i] :
                    return False
            elif t[i] in d:
                if d[t[i]]!= s[i]:
                    return False
            else:
                d[s[i]]=t[i]
                d[t[i]]=s[i]
        return True
        
        '''
