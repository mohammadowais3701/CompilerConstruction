import regex
import json
class Token():
    def __init__(self,CP,VP,LINE):
        self.CP=CP
        self.VP=VP
        self.LINE=LINE
    def getTokens(self):
        return [self.CP,self.VP,self.LINE]
def breakwords():
   global line 
   global i
   temp=""
   count=0    # use for " count
   counts=0
   comment=0 

   while(i<len(contents)):
        if(i==len(contents)-1):
            temp=temp+contents[i]
            i=i+1
            return temp
     
        if(contents[i]=="\n"):
            if(len(temp)==0):

                line=line+1
                i=i+1
            else:
                return temp    
    #    print("i={i}",i)
        
        elif(contents[i]==" "  and counts==0 and count==0):
            i=i+1
            #return temp
           # i=i+1
            if(len(temp)==0):
                while(contents[i]==" "):
                    i=i+1
            else:
             #   i=i+1
               
                return temp
        elif((len(temp)==4 and count==1 and temp[1]=="\\" and (temp[2]=="\\" or temp[2]=="'" or temp[2]=="n" or temp[2]=="\"" or temp[2]=="b")) and counts==0 and count==0):
            
            return temp
        elif(len(temp)==3 and count==1  and counts==0 and count==0):
            return temp    
        elif(contents[i]=="."  and counts==0 and count==0):
            
            
           
           
            if(len(temp)==0):
                
                if(regex.integerConstant(contents[i+1])):
                    temp=contents[i]
                    i=i+1
                else:
                    temp=contents[i]
                    i=i+1
                    return temp
            elif(not(len(temp)==0) and ( regex.integerConstant(temp) or regex.floatConst(temp)) and  not(regex.identifiers(contents[i+1]))):
                temp=temp+contents[i]
                i=i+1
            else:
                return temp


        elif(contents[i]==";"  or contents[i]==":" or contents[i]==","  and counts==0 and count==0):
            if(len(temp)>0):
                return temp
            elif(len(temp)==0):
                temp=contents[i]
                i=i+1 
                return temp   
        elif(contents[i]=="*" or contents[i]=="/" or contents[i]=="%" and counts==0 and count==0):    
             if(len(temp)>0):
                return temp
             elif(len(temp)==0):
                temp=contents[i]
                i=i+1 
                return temp
        elif(contents[i]=="+"  and  counts==0 and count==0):    
                if(len(temp)>0):
                    return temp
                elif(len(temp)==0):
                    temp=contents[i]
                    i=i+1 
                    if(contents[i]=="+"):
                        temp=temp+contents[i]
                        i=i+1
                    return temp  

        elif(contents[i]=="-"   and counts==0 and count==0):    
            if(len(temp)>0):
                return temp
            elif(len(temp)==0):
                temp=contents[i]
                i=i+1 
                if(contents[i]=="-"):
                    temp=temp+contents[i]
                    i=i+1
                return temp
        elif(contents[i]=="="  and counts==0 and count==0):    
                if(len(temp)>0):
                    return temp
                elif(len(temp)==0):
                    temp=contents[i]
                    i=i+1 
                    if(contents[i]=="="):
                        temp=temp+contents[i]
                        i=i+1
                    return temp
        elif(contents[i]=="<"  and counts==0 and count==0):    
                if(len(temp)>0):
                    return temp
                elif(len(temp)==0):
                    temp=contents[i]
                    i=i+1 
                    if(contents[i]=="="):
                        temp=temp+contents[i]
                        i=i+1
                    return temp
        elif(contents[i]==">"  and counts==0 and count==0):    
                if(len(temp)>0):
                    return temp
                elif(len(temp)==0 ):
                    temp=contents[i]
                    i=i+1 
                    if(contents[i]=="="):
                        temp=temp+contents[i]
                        i=i+1
                    return temp
        elif(contents[i]=="!"   and counts==0 and count==0):    
                if(len(temp)>0):
                    return temp
                elif(len(temp)==0):
                    temp=contents[i]
                    i=i+1 
                    if(contents[i]=="="):
                        temp=temp+contents[i]
                        i=i+1
                    return temp                                                 
        elif(contents[i]=="a" and contents[i+1]=="n" and contents[i+2]=="d" and contents[i+3]==" "  and counts==0 and count==0):
         
            if(len(temp)==0):
                temp=contents[i]+contents[i+1]+contents[i+2]
                i=i+3
                return temp
        elif(contents[i]=="n" and contents[i+1]=="o" and contents[i+2]=="t" and contents[i+3]==" " and counts==0 and count==0):
            if(len(temp)==0):
                temp=contents[i]+contents[i+1]+contents[i+2]
                i=i+3
                return temp        
        elif(contents[i]=="o" and contents[i+1]=="r" and contents[i+2]==" "   and counts==0 and count==0):
            if(len(temp)==0):
                temp=contents[i]+contents[i+1]
                i=i+2
                return temp      
        elif(contents[i]=="("):

            if(len(temp)>0):
                return temp
            elif(len(temp)==0):
                temp=contents[i]
                i=i+1 
                return temp
        elif(contents[i]==")"   and counts==0 and count==0):

            if(len(temp)>0):
                return temp
            elif(len(temp)==0):
                temp=contents[i]
                i=i+1 
                return temp
        elif(contents[i]=="{" and counts==0 and count==0):

            if(len(temp)>0):
                return temp
            elif(len(temp)==0):
                temp=contents[i]
                i=i+1 
                return temp
        elif(contents[i]=="}" and counts==0 and count==0):

            if(len(temp)>0):
                return temp
            elif(len(temp)==0):
                temp=contents[i]
                i=i+1 
                return temp
        elif(contents[i]=="["  and counts==0 and count==0):

            if(len(temp)>0):
                return temp
            elif(len(temp)==0):
                temp=contents[i]
                i=i+1 
                return temp
        elif(contents[i]=="]"  and count==0):

            if(len(temp)>0):
                return temp
            elif(len(temp)==0):
                temp=contents[i]
                i=i+1 
                return temp                        
        elif(contents[i]=="\"" ):

            if(len(temp)>0 and counts==1 and (not(contents[i-1]=="\\"))):
                temp=temp+contents[i]
                i=i+1
                return temp
            elif(len(temp)>0 and counts==0):
               # temp=temp+contents[i]
                return temp    
            elif(len(temp)==0):
                temp=contents[i]
                i=i+1 
                counts=1
            else:
                temp=temp+contents[i]
                i=i+1 
                #return temp        
        elif(contents[i]=="'" and counts==0):

            if(len(temp)>0 and count==1):
                temp=temp+contents[i]
                i=i+1
                return temp
            elif(len(temp)>0 and count==0):
               # temp=temp+contents[i]
                return temp    
            elif(len(temp)==0):
                temp=contents[i]
                i=i+1 
                count=1
            else:
                temp=temp+contents[i]
                i=i+1 
                #return temp        

        elif(contents[i]=="#" and counts==0 and count==0):
            comment=1
            if(count==1 or counts==1):
                temp=temp+contents[i]
                i=i+1
            elif(len(temp)>0 and count==0):
                return temp
            else:
                temp=temp+contents[i]
                i=i+1    
                    
        else:
            temp=temp+contents[i]
            i=i+1        
def isKw(tem):
   
    for x in KW:
        m=0
        while(m<len(KW[x])):
            if(KW[x][m]==tem):
               # print("match")
                return x 
            m=m+1    
        #print("not match")        
    return ""   
def isOpr(tem):
   
    for x in OPR:
        m=0
        while(m<len(OPR[x])):
            if(OPR[x][m]==tem):
               # print("INSIDE PUN")
                return x
            m=m+1      
          
    return isPun(tem)
def isPun(tem):
   
    for x in PUN:
        m=0
        while(m<len(PUN[x])):
            if(PUN[x][m]==tem):
                #print("INSIDE PUN")
                return x
            m=m+1     
     
    return regex.stringConst(tem)    
f = open("inputfile.txt", "r")
contents = f.read()
fw = open("Token.txt", "w")
i = 0
line = 1
k = 0
KW = {"DT": ["int", "char", "float", "boolean","void","string"], "break": ["break"], "skip": ["skip"], "if": ["if"],
      "elif": ["elif"], "else": ["else"], "floop": ["floop"], "wloop": ["wloop"], "return": ["return"],
      "class": ["class"], "abstract": ["abstract"], "final": ["final"], "o_static": ["static"], "this": ["this"], "super":["super"],"main":["main"],
      "AM": ["private", "public","protected"],"new":["new"]}
PUN = {":": [":"], "{": ["{"], "}": ["}"], "(": ["("], ")": [")"], ".": ["."], ";": [";"], "[": ["["], "]": ["]"],",":[","]}
OPR = {"PM": ["+", "-"], "MDM": [ "*", "/", "%"]  ,"AOP": ["="], "ROP": ["!=", "<=", ">=", "<", ">", "=="],
       "LOP": ["and", "or"], "NOT": ["not"], "INC/DEC": ["++", "--"]}
def main():
    global i
    global k
    global line
    TS = []
    Tokens = []



    # print(contents[125])
    # print("")
    while (i < len(contents)):
        #  temp=""
        temp = breakwords()  # calling for breaking word

        #print(temp)
        # print(len(temp))
        if (temp == None):
            break
        if (temp[0] == "_"):
            if (regex.identifiers(temp)):
                TS.append(Token("ID", temp, line))

                fw.write(json.dumps(TS[k].getTokens()) + "\n")
                k = k + 1
            else:
                TS.append(Token("Invalid Lexeme", temp, line))

                fw.write(json.dumps(TS[k].getTokens()) + "\n")
                k = k + 1
        elif (temp[0] == "#"):
            TS.append(Token("Comment", temp[1:], line))

            k = k + 1
        elif ((temp[0] >= "A" and temp[0] <= "Z") or (temp[0] >= "a" and temp[0] <= "z")):

            if (regex.identifiers(temp)):
                # print("Inside Indentifier")
                CP = isKw(temp)
                if (CP == ""):

                    TS.append(Token("ID", temp, line))

                    fw.write(json.dumps(TS[k].getTokens()) + "\n")
                    k = k + 1
                else:
                    # print("Inside Indentifier2")
                    TS.append(Token(CP, temp, line))

                    fw.write(json.dumps(TS[k].getTokens()) + "\n")
                    k = k + 1
            else:
                TS.append(Token("Invalid Lexeme", temp, line))

                fw.write(json.dumps(TS[k].getTokens()) + "\n")
                k = k + 1
        else:
            CP = isOpr(temp)
            # print("CP")
            # print(CP)
            if (not (CP == "")):
                # print("Inside ")
                TS.append(Token(CP, temp, line))

                fw.write(json.dumps(TS[k].getTokens()) + "\n")
                k = k + 1
            else:
                TS.append(Token("Invalid Lexeme", temp, line))

                fw.write(json.dumps(TS[k].getTokens()) + "\n")
                k = k + 1
    TS.append(Token('$', '$', line + 1))
    fw.write(json.dumps(TS[k].getTokens()))
    f.close()
    fw.close()
    return TS






        
    