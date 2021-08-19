class Solution:
    def myAtoi(self, s: str) -> int:
        inp  = s.strip()
        outp = ""
        start = 0;
        
        if(len(inp) == 0): return(0)
        if(not(inp[0].isnumeric()) and inp[0] not in ["+", "-"]): return(0)
        else:
            for i in range(len(inp)):
                if(start == 0):
                    if(inp[i].isnumeric()):
                        outp += inp[i]
                        start = 1
                    elif(i< len(inp)-1):
                        if(inp[i] in ["+", "-"]):
                            if (inp[i+1].isnumeric()):
                                outp += inp[i]
                                start = 1
                            else: return(0)
                else:
                    if(inp[i].isnumeric()): outp += inp[i]
                    else: break
                    
        if(len(outp) == 0): return(0)
        else:
            num = int(outp)
            if(num>2147483647 or num <-2147483648 ): 
                if(num<0): return(-2147483648)
                else: return(2147483647)
            else: return(num)
        
