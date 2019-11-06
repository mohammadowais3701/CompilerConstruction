import re
string1="'\\n'"

def stringConst(string):
   strconst=re.match("\A\"(([A-Z]|[a-z]|[0-9])*|([^A-Z]|[^a-z]|[^0-9])*)\"$",string)

   if strconst:
       return "string_const"
   else:
        CP=charConstant(string)
        return CP
        

def charConstant(string):
    if(string=="'\\'"):
        CP=floatConst(string)
        return CP
    if(string=="'\\\\'"):
        string="'\\'"
    if(string1==string):
       string="'\n'"
    
    chconst=re.match("\A\'((([a-z]|[A-Z])|([^0-9]|[^A-Z]|[^a-z]))|\(([a-z]|[A-Z])|('|\"|\\)))\'$",string)
    if chconst:
       
        return "char Constant"
    else:
        CP=floatConst(string)
        return CP
            
def floatConst(string):
    fconst= re.match("\A(\+|-|^)(([0-9]*.[0-9]+)$)",string)
    if fconst:
        return "float_const"
    else:
        CP=integerConstant(string)
        return CP
    
def integerConstant(string):
    
    IntConst = re.match("(\A(\+|-|^))([0-9])+$",string)
    if IntConst:
         
         return "integer_const"
    else:
         return ""
    
def identifiers(string):
       identifier = re.match("((\A([a-z]|[A-Z])+((([a-z]|[A-Z])|[0-9])*$))|\A_(([a-z]|[A-Z])|[0-9])+$)",string)
    
       if identifier:
         #print("IDent")
         return True
       else:
        return False
          
      
