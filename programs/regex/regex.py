import re


def stringConst():
   strconst=re.match("\A\"(([A-Z]|[a-z]|[0-9])*|([^A-Z]|[^a-z]|[^0-9])*)\"$",string)

   if strconst:
    print("String Constant")
   else:
    print("String does not matched")
        

def charConstant():
    chconst=re.match("\A\'((([a-z]|[A-Z])|([^0-9]|[^A-Z]|[^a-z]))|\(([a-z]|[A-Z])|('|\"|\\)))\'$",string)
    if chconst:
        print("Char Constant")
    else:
      stringConst()
            
def floatConst():
    fconst= re.match("\A(\+|-|^)(([0-9]*.[0-9]+)$)",string)
    if fconst:
        print("Float Constant")
        return
    else:
       charConstant() 
    
def integerConstant():
    
    IntConst = re.match("(\A(\+|-|^))([0-9])+$",string)
    if IntConst:
         print("integer Constant")
         return
    else:
         floatConst()
    
def identifiers():
       identifier = re.match("((\A([a-z]|[A-Z])+((([a-z]|[A-Z])|[0-9])*$))|\A_(([a-z]|[A-Z])|[0-9])+$)",string)
    
       if identifier:
         print("String matched with identifier")
         return
       else:
          integerConstant()
          
identifiers()         
