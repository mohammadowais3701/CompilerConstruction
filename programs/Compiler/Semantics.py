import LexSyntax as lx
import CC1
import pandas as pd
import regex
import json
import numpy as np

stack = []
CrP=''
CN=''
CT=''
CS=''
N=''
N2=''
CDrT=''
AM=''
TM=''
ST=''
OP=''
Types=[]
Opr=[]
comp={('float','int'):['int','float','+','-','*','/','='],('string'):['char','string','+'],('int'):['int','int','+','-','*','/'],('string'):['char','char','+']}
ScopeTable = pd.DataFrame({'Name': [], 'Type': [], 'Scope': []})
ClassTable = pd.DataFrame({'Name': [], 'Type': [], 'Parent': [], 'Ref': []})
scope=0
class classreftable:

    def __init__(self,CN):
        self.CN=CN
        self.Classreftable = pd.DataFrame({'Name': [], 'Type': [], 'AM': [], 'TM': []})

def lookUpCT(N):
    if(N in ClassTable['Name'].values):
        return True
    else:
        return False
def lookupCDT(CN,N,Parent):
    if (CN in ClassTable['Name'].values):
        mask = ClassTable['Name'] == CN

        df = ClassTable[mask]['Ref']
        if (N in df[0].Classreftable['Name'].values):
            mas=df[0].Classreftable['Name']==N
            value=df[0].Classreftable['AM'][mas]

            if(value[0]=='public'):
                    return (df[0].Classreftable['Type'][mas][0])
            elif(value[0]=='private' or value[0]=='protected'):
                print('You can\'t it because  you access private or protected varibale')
                return False
        elif(Parent in ClassTable['Name'].values):

            mask = ClassTable['Name'] == Parent

            df = ClassTable[mask]['Ref']
            if (N in df[0].Classreftable['Name'].values):
                mas = df[0].Classreftable['Name'] == N
                value = df[0].Classreftable['AM'][mas]
                if (value[0] == 'public' or value[0] == 'protected'):
                    return (df[0].Classreftable['Type'][mas][0])
                elif (value[0] == 'private'):
                    print('You can\'t it because  you access private or protected varibale')
                    return False
                else:
                    print(N + ' is not declared')
                    return False
        else:
            print(N+ ' is not declared')
            return False
def lookupST(N,SS,CN):
    global ScopeTable
    global ClassTable

    if(N in ScopeTable['Name'].values):

        mas=ScopeTable['Name']==N
        df=ScopeTable[mas]['Scope']
      #  print(int(df[1]))
        #print(SS)
       # t=int(df[1])==SS

        try:
            if(df[0]==SS):

                return(ScopeTable[mas]['Type'][0])

            else:
                return False

        except:
            if (df[1] == SS):

                return (ScopeTable[mas]['Type'][1])

            else:
                return False


    elif (CN in ClassTable['Name'].values):
        mask = ClassTable['Name'] == CN

        df = ClassTable[mask]['Ref']

        if (N in df[0].Classreftable['Name'].values):
            mas=df[0].Classreftable['Name']==N
            value=df[0].Classreftable['AM'][mas]

            if(value[0]=='public'):
                    return (df[0].Classreftable['Type'][mas][0])
            elif(value[0]=='private' or value[0]=='protected'):
                print('You can\'t it because  you access private or protected varibale')
                return False

        elif(CrP in ClassTable['Name'].values):

            mask = ClassTable['Name'] == CrP

            df = ClassTable[mask]['Ref']
            if (N in df[0].Classreftable['Name'].values):
                mas = df[0].Classreftable['Name'] == N
                value = df[0].Classreftable['AM'][mas]
                if (value[0] == 'public' or value[0] == 'protected'):
                    return (df[0].Classreftable['Type'][mas][0])
                elif (value[0] == 'private'):
                    print('You can\'t it because  you access private or protected varibale')
                    return False
                else:
                    print(N + ' is not declared')
                    return False
            else:
                return False
        else:
            print(N+ ' is not declared')
            return False


def createscope():
    global scope
    stack.append(scope)
    scope=scope+1
    return scope-1
def deletescope():
    global scope
    scope=stack.pop()
    return scope
def comp2(righttype,T):
    for i in range(len(T)):
        if(T[i]==righttype):
            return righttype

def compatibility(lefttype,righttype,opr):
    if(((((lefttype=='int' and righttype=='float')or(lefttype=='float' and righttype=='int') )or(lefttype == 'float' and righttype == 'float')) and( opr=='+' or opr=='-' or opr=='*'  or opr=='/' )) or ((lefttype == 'float' and (righttype == 'int' or righttype=='float')) and opr == '=')):
        return 'float'
    elif((lefttype=='int' and righttype=='int' and (opr=='+' or opr=='-' or opr=='*' or opr =='/')) or((lefttype=='int' and (righttype=='float' or righttype=='int')) and opr=='=')):
        return 'int'
    elif(lefttype == 'string' and righttype == 'string' and opr=='='):
        return 'string'
    elif (((lefttype == 'string' and righttype == 'string')or((lefttype == 'int' or lefttype=='float') and righttype == 'string')or (lefttype == 'string' and( righttype == 'int' or righttype=='float'))) and (  opr == '+')):
        return 'string'
    elif(lefttype=='char' and righttype=='char' and opr=='='):
        return 'char'
    elif(lefttype==righttype and righttype=='boolean' and (opr=='and' or opr =='or')):
        return 'boolean'
    else:
        return False
def compatibility2(operand,opr):
    if(operand=='boolean' and opr=='not'):
        return 'boolean'
    else:
        return False
def insertCDT(N,T,AM,TM,CN):
    global ClassTable
    if(AM==''):
        AM='public'
    if(CN in ClassTable['Name'].values):
        mask=ClassTable['Name']==CN

        df=ClassTable[mask]['Ref']

        if(N in df[0].Classreftable['Name'].values):
            return False
        else:
            df[0].Classreftable=df[0].Classreftable.append(pd.DataFrame({'Name':[N],'Type':[T],'AM':[AM],'TM':[TM]}))
            return True
    else:
        return False
    #print(ClassTable[mask]['Ref'].Classreftable)
  #  df.Classreftable=(df.Classreftable).append(pd.DataFrame({'Name':[N],'Type':[T],'AM':[AM],'TM':[TM]}))






def insertCT(Name,Type,Parent):
    global ClassTable
    if (Name in ClassTable['Name'].values):
        return False
    else:

        if(Parent!=''):

            if(Parent in ClassTable['Name'].values):

                ClassTable=ClassTable.append(pd.DataFrame({'Name':[Name],'Type':[Type],'Parent':[Parent],'Ref':[classreftable(Name)]}))

                return True
        else:
            ClassTable = ClassTable.append(pd.DataFrame({'Name': [Name], 'Type': [Type], 'Parent': [Parent], 'Ref': [classreftable(Name)]}))

            return True
def insertST(Name, Type, Scope):
    global ScopeTable
    if (Name in ScopeTable['Name'].values):
        mask = ScopeTable['Name'] == Name

        df = ScopeTable[mask]['Scope']
        try:
            if(Scope==df[0]):

                return False
            else:
                ScopeTable = ScopeTable.append(pd.DataFrame({'Name': [Name], 'Type': [Type], 'Scope': [Scope]}),ignore_index='True')
                return True
        except:
            if (Scope == df[1]):

                return False
            else:
                ScopeTable = ScopeTable.append(pd.DataFrame({'Name': [Name], 'Type': [Type], 'Scope': [Scope]}),ignore_index='True')
                return True



    else:
       ScopeTable = ScopeTable.append(pd.DataFrame({'Name': [Name], 'Type': [Type], 'Scope': [Scope]}),ignore_index='True')
       return True

#print(ScopeTable)
#check=insertST('a', 'int', '7')
#print(check)
#check=insertST('b', 'int', '7')
#print(check)
#insertCT('I','class','')
#check=insertCDT('b','char','public','static','I')
#print(check)
#type=lookupST('b',7,'I')
#print(type)

#insertCT('I','class','')
#insertCT('J','class','I')

#insertCT('D','class','E')
#check=insertCDT('a','int','public','static','J')
#check=insertCDT('d','float','private','static','I')
#check=insertCDT('b','char','public','static','I')
#check=insertCDT('c','string','protected','static','I')
#type=lookupCDT('J','d','I')
#print(type)
#type=lookupCDT('J','b','I')
#print(type)
#type=lookupCDT('J','c','I')
#print(type)
#check=insertCDT('a','int','public','static','A')
#print(check)
#print(ClassTable[0:3])
# def main():
#   global TS

#  TS=lx.main()


# main()

TS = []
i = 0


def ARRAYDEC():
    global i
    if (TS[i].getTokens()[0] == "DT"):
        if (DT2()):
            if (TS[i].getTokens()[0] == "["):
                i = i + 1
                if (E()):
                    if (TS[i].getTokens()[0] == "]"):
                        i = i + 1
                        if (OPT()):
                            if (TS[i].getTokens()[0] == "ID"):
                                i = i + 1
                                if (OPT2()):
                                    return True
    return False


def FUNC_CALL():
    global i
    if (TS[i].getTokens()[0] == "ID"):
        i = i + 1
        if (TS[i].getTokens()[0] == "("):
            i = i + 1
            if (ARGS2()):
                if (TS[i].getTokens()[0] == ")"):
                    i = i + 1
                    if (TS[i].getTokens()[0] == ";"):
                        i = i + 1
                        return True
    return False


def COND():
    global i
    if (TS[i].getTokens()[0] == "ID" or regex.charConstant(
            TS[i].getTokens()[1]) == "char Constant" or regex.stringConst(
            TS[i].getTokens()[1]) == "string_const" or regex.integerConstant(TS[i].getTokens()[1]) == "integer_const" or
            TS[i].getTokens()[0] == "INC/DEC" or TS[i].getTokens()[0] == "NOT" or TS[i].getTokens()[0] == "this" or
            TS[i].getTokens()[0] == "super"):
        if (OE()):
            return True
    elif (TS[i].getTokens()[1] == "true" or TS[i].getTokens()[1] == "false"):
        return True
    return False


def IF_ST():
    global i

    if (TS[i].getTokens()[1] == "if" or TS[i].getTokens()[0][2:4] == 'if'):
        i = i + 1
        if (TS[i].getTokens()[1] == "("):
            i = i + 1

            if (COND()):

                if (TS[i].getTokens()[1] == ")"):
                    i = i + 1

                    if (TS[i].getTokens()[1] == "{"):
                        i = i + 1

                        if (MST()):

                            if (TS[i].getTokens()[1] == "}"):
                                i = i + 1

                                if (OELIF()):

                                    if (OELSE()):
                                        return True
                                return True

    return False


def OELIF():
    global i

    if (TS[i].getTokens()[0] == "elif"):

        if (IF_ST()):
            return True
    elif (TS[i].getTokens()[0] == "else"):
        return True
    return False


def OELSE():
    global i

    if (TS[i].getTokens()[0] == "else"):
        i = i + 1
        if (TS[i].getTokens()[0] == "{"):
            i = i + 1
            if (MST()):
                if (TS[i].getTokens()[0] == "}"):
                    i = i + 1
                    return True
    return False


def Q():
    global i

    if (TS[i].getTokens()[0] == "ID"):

        if (P()):
            return True

    if (TS[i].getTokens()[0] == "ID" or regex.charConstant(
            TS[i].getTokens()[1]) == "char" or regex.stringConst(
            TS[i].getTokens()[1]) == "string" or regex.floatConst(
            TS[i].getTokens()[1]) == "float" or regex.integerConstant(TS[i].getTokens()[1]) == "int" or
            TS[i].getTokens()[0] == "INC/DEC" or TS[i].getTokens()[0] == "NOT" or TS[i].getTokens()[0] == "this" or
            TS[i].getTokens()[0] == "super"):

        if (OE()):
            return True

    return False


def ASSIGN():
    global i
    if (TS[i].getTokens()[0] == 'ID'):
        if (P()):
            if (TS[i].getTokens()[1] == '='):
                i = i + 1
                if (Q()):
                    return True
    return False


def CLASSDEF():
    global i
    global CrP
    global CN
    global CT
    global Types
    global AM
    global TM
    # print(TS[i].getTokens()[1])

    if (TS[i].getTokens()[0] == 'AM' or TS[i].getTokens()[0] == 'class'):

        if (AMs()):

            if (TS[i].getTokens()[0] == 'class'):
                CT='class'

                i = i + 1

                if (TS[i].getTokens()[0] == 'ID'):
                    CN=TS[i].getTokens()[1]
                    i = i + 1
                    CrP=''
                    if (INH()):
                        k=insertCT(CN,CT,CrP)
                        if(k):
                            if (TS[i].getTokens()[1] == '{'):
                                i = i + 1

                                if (CLASS_BODY()):

                                    if (TS[i].getTokens()[1] == '}'):
                                        i = i + 1

                                        return True
                        else:
                            print('Your Class is already defined')
                            return False
                    else:
                        i = i - 3

    return False


def OPT():
    global i

    if (TS[i].getTokens()[0] == '['):
        i = i + 1
        if (OE()):

            if (TS[i].getTokens()[1] == ']'):
                i = i + 1

                return True
    elif (TS[i].getTokens()[0] == 'ID' or TS[i].getTokens()[0] == '.' or TS[i].getTokens()[0] == ',' or
          TS[i].getTokens()[0] == ')' or TS[i].getTokens()[1] == '='):
        return True
    return False


def OPT2():
    global i

    if (TS[i].getTokens()[0] == ','):
        i = i + 1
        if (TS[i].getTokens()[0] == 'ID'):
            i = i + 1
            if (OPT2()):
                return True
    elif (TS[i].getTokens()[0] == 'AOP'):
        i = i + 1
        if (TS[i].getTokens()[0] == 'new'):
            i = i + 1
            if (DT2()):
                if (TS[i].getTokens()[0] == '('):
                    i = i + 1
                    if (ARGS2()):
                        if (TS[i].getTokens()[0] == ')'):
                            i = i + 1

                            return True
    elif (TS[i].getTokens()[1] == ';'):

        return True
    return False


def P():
    global i


    if (TS[i].getTokens()[0] == 'ID'):

        k=lookupST(TS[i].getTokens()[1],CS,Types[0])

        if(k!=False):
            Types.append(k)

            i = i + 1

            if (P22()):

                return True

        else:

            i = i - 1

            return False
    return False


def P1():
    global i

    if (TS[i].getTokens()[0] == '.'):
            i = i + 1
       # k = lookupST(N, CS, CN)
       # if (k != False):
            if (P()):

                return True

    elif (TS[i].getTokens()[0] == 'AOP' or TS[i].getTokens()[0] == ';' or TS[i].getTokens()[0] == ')'):

        return True
    return False


def P22():
    global i

    if (TS[i].getTokens()[0] == '.'):

        if (P1()):
            return True
    elif (TS[i].getTokens()[0] == '('):
        i = i + 1

        if (ARGS2()):

            if (TS[i].getTokens()[0] == ')'):
                i = i + 1

                if (TS[i].getTokens()[0] == ';'):

                    if (P1()):
                        return True
                elif (TS[i].getTokens()[0] == 'AOP'):

                    if (P1()):
                        return True
                elif (TS[i].getTokens()[0] == ','):

                    i = i + 1

                    if (Q()):
                        return True
                elif (TS[i].getTokens()[0] == '.'):
                    i = i + 1

                    if (P()):
                        return True

    elif (TS[i].getTokens()[0] == '['):
        i = i + 1

        if (E()):

            if (TS[i].getTokens()[0] == ']'):

                i = i + 1

                if (OPT()):

                    if (P1()):
                        return True

    elif (TS[i].getTokens()[0] == ','):

        i = i + 1

        if (Q()):
            return True
    elif (TS[i].getTokens()[0] == 'AOP' or TS[i].getTokens()[0] == ';' or TS[i].getTokens()[0] == ')' or
          TS[i].getTokens()[0] == ';'):


        return True
    return False


def DT2():
    global i
    if (TS[i].getTokens()[0] == 'DT' or TS[i].getTokens()[0] == 'ID'):
        if (len(Types) != 0):
            if (Types[0] == TS[i].getTokens()[1]):
                pass
            else:

                if (TS[i].getTokens()[1] in ClassTable['Name'].values):

                    mask = ClassTable['Name'] == TS[i].getTokens()[1]

                    df = ClassTable[mask]['Parent']

                    if (Types[0] in df[0].Classreftable['Name'].values):
                        pass
                    else:
                        print('Type Mismatch in object declaration')
                        return False
                else:
                    print('Type Mismatch in object declaration')
                    return False
        else:
            Types.append(TS[i].getTokens()[1])
        i = i + 1
        return True
    return False


def DT1():
    global i
    global Types

    if (TS[i].getTokens()[0] == '['):
        i = i + 1
        if (TS[i].getTokens()[0] == ']'):
            i = i + 1
            if (TS[i].getTokens()[0] == '['):
                i = i + 1
                if (TS[i].getTokens()[0] == ']'):
                    i = i + 1
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    return True


def DT():
    global i
    global CrP
    global CN
    global CT
    global CS
    global CDrT
    global N
    global TM
    global AM
    global ST
    global OP
    global Types
    global Opr
    #Types.append('k')

    if (TS[i].getTokens()[0] == 'DT' or TS[i].getTokens()[0] == 'ID'):

        if(len(Types)!=0):
            if(Types[0]==TS[i].getTokens()[1]):

                pass
            else:

                if(TS[i].getTokens()[1] in ClassTable['Name'].values):

                    mask = ClassTable['Name'] == TS[i].getTokens()[1]

                    df = ClassTable[mask]['Parent']

                    if (Types[0] in df[0].Classreftable['Name'].values):
                        pass
                    else:
                        print('Type Mismatch in object declaration')
                        return False
                else:
                    print('Type Mismatch in object declaration')
                    return False
        else:
            Types.append(TS[i].getTokens()[1])

        i = i + 1
        if (DT1()):
            return True



    return False


def Y1():
    global i
    if (TS[i].getTokens()[0] == "["):
        i = i + 1
        if (OE()):
            if (TS[i].getTokens()[0] == "]"):
                i = i + 1
                if (OPT()):
                    return True
    elif (TS[i].getTokens()[0] == "," or TS[i].getTokens()[0] == ")"):
        return True
    return False


def X1():
    global i

    if (TS[i].getTokens()[0] == 'ID'):
        i = i + 1
        if (Y1()):
            return True
    return False


def ARRAYDEC1():
    global i
    if (TS[i].getTokens()[0] == '['):
        i = i + 1
        if (E()):
            if (TS[i].getTokens()[1] == ']'):
                if (OPT()):
                    if (TS[i].getTokens()[0] == 'ID'):
                        i = i + 1
                        if (OPT2()):
                            return True
    return False


def OBJ1():
    global i

    if (TS[i].getTokens()[0] == 'ID'):

        if (TS[i].getTokens()[0] == 'ID'):
            i = i + 1

            if (TS[i].getTokens()[1] == '='):

                i = i + 1

                if (TS[i].getTokens()[1] == 'new'):
                    i = i + 1
                    if (DT()):
                        if (TS[i].getTokens()[1] == '('):
                            i = i + 1
                            if (ARGS2()):
                                if (TS[i].getTokens()[1] == ')'):
                                    i = i + 1
                                    # if(TS[i].getTokens()[1]==';'):
                                    #     i=i+1
                                    return True
                else:
                    i = i - 2

    return False


def SST13():
    global i
    if (TS[i].getTokens()[0] == '['):
        i = i + 1
        if (TS[i].getTokens()[0] == ']'):
            i = i + 1

        if (SST12()):
            return True
    elif (TS[i].getTokens()[0] == 'ID'):
        if (SST7()):
            return True
    return False


def SST12():
    global i
    global CrP
    global CN
    global CT
    global CS
    global CDrT
    global N
    global TM
    global AM
    global ST
    global OP
    global N2
    global Types
    if (TS[i].getTokens()[0] == 'ID' or regex.charConstant(
            TS[i].getTokens()[1]) == "char" or regex.stringConst(
            TS[i].getTokens()[1]) == "string" or regex.integerConstant(
            TS[i].getTokens()[1]) == 'int' or regex.floatConst(TS[i].getTokens()[1]) == "float" or
            TS[i].getTokens()[0] == 'INC/DEC' or TS[i].getTokens()[0] == '(' or TS[i].getTokens()[0] == 'not' or
            TS[i].getTokens()[0] == 'this' or TS[i].getTokens()[0] == 'super'):

        if (OE()):


            if (M1()):
                return True
    elif (TS[i].getTokens()[0] == 'new'):

        i = i + 1

        if (DT()):

            if (TS[i].getTokens()[0] == '('):
                i = i + 1

                if (ARGS2()):
                    if (TS[i].getTokens()[0] == ')'):
                        i = i + 1
                        return True
    elif (TS[i].getTokens()[0] == ';'):

        return True
    return False


def SST11():
    global i


    if TS[i].getTokens()[0] == 'ID' or regex.charConstant(TS[i].getTokens()[1]) == "char" or regex.integerConstant(
            TS[i].getTokens()[1]) == 'int' or  \
            TS[i].getTokens()[0] == 'INC/DEC' or TS[i].getTokens()[0] == '(' or TS[i].getTokens()[0] == 'not' or \
            TS[i].getTokens()[0] == 'this' or TS[i].getTokens()[0] == 'super':

        if (E()):

            if (TS[i].getTokens()[0] == ']'):
                i = i + 1

                if (OPT()):

                    if (OPT3()):

                        k = insertST(N, Types[0], CS)

                        if (k):

                            return True
                        else:
                            print('Redeclaration of ' + N)
                            return False

    elif (TS[i].getTokens()[0] == ']'):
        i = i + 1
        if (SST13()):
            return True
    return False


def SST10():
    global i
    global CrP
    global CN
    global CT
    global CS
    global CDrT
    global N
    global TM
    global AM
    global ST

    global Types
    if (TS[i].getTokens()[0] == 'AOP'):
        Opr.append(TS[i].getTokens()[1])
        i = i + 1

        if (SST12()):

            for j in range(len(Opr)):

                type = compatibility(Types[len(Types) - 2], Types[len(Types) - 1], Opr[len(Opr) - j - 1])

                if (type != False):
                    Types.pop()
                    Types.pop()
                    Types.append(type)


                # print(Opr)
                else:
                    print('Type Mismatch')
                    return False

            k=insertST(N,Types[0],CS)


            if(k):

              return True
            else:
              print('Redeclaration of '+ N)
              return False

    elif (TS[i].getTokens()[0] == ','):

        if (M1()):
            return True
    elif (TS[i].getTokens()[0] == ';'):
        k = insertST(N, Types[0], CS)

        if (k):

            return True


        else:
            print('Redeclaration of ' + N)
            return False
    elif (TS[i].getTokens()[0] == '.'):

        if (P22()):
            if (TS[i].getTokens()[0] == 'AOP'):
                i = i + 1
                if (Q()):
                    if (TS[i].getTokens()[0] == '('):
                        i = i + 1
                        if (ARGS2()):
                            if (TS[i].getTokens()[0] == ')'):
                                return True

    return False


def OPT3():
    global i
    global N
    if (TS[i].getTokens()[0] == 'ID'):
        N=TS[i].getTokens()[1]
        i = i + 1

        if (OPT2()):
            return True
    elif (TS[i].getTokens()[0] == '.'):

        i = i + 1
        if (TS[i].getTokens()[0] == 'ID'):
            i = i + 1
            if (TS[i].getTokens()[0] == 'AOP'):
                i = i + 1

                if (Q()):
                    return True
            elif (TS[i].getTokens()[0] == ';'):
                return True

    elif (TS[i].getTokens()[0] == 'AOP'):
        i = i + 1

        if (Q()):
            return True
    elif (TS[i].getTokens()[0] == ';'):
        return True
    return False


def SST9():
    global i

    if (TS[i].getTokens()[0] == 'ID' or regex.charConstant(
            TS[i].getTokens()[1]) == "char Constant" or regex.stringConst(
            TS[i].getTokens()[1]) == "string_const" or regex.integerConstant(
            TS[i].getTokens()[1]) == 'integer_const' or regex.floatConst(TS[i].getTokens()[1]) == "float_const" or
            TS[i].getTokens()[0] == 'INC/DEC' or TS[i].getTokens()[0] == '(' or TS[i].getTokens()[0] == 'not' or
            TS[i].getTokens()[0] == 'this' or TS[i].getTokens()[0] == 'super'):
        if (E()):

            if (TS[i].getTokens()[0] == ']'):
                i = i + 1

                if (OPT()):

                    if (OPT3()):
                        return True
    elif (TS[i].getTokens()[0] == ']'):
        i = i + 1
        if (SST8()):
            return True
    return False


def SST8():
    global i
    if (TS[i].getTokens()[0] == '['):
        i = i + 1
        if (TS[i].getTokens()[0] == ']'):
            i = i + 1
            if (TS[i].getTokens()[0] == 'ID'):
                i = i + 1
                if (M()):
                    return True

    elif (TS[i].getTokens()[0] == 'ID'):
        if (M()):
            return True
    return False


def SST7():
    global i
    global Types,Opr
    if (TS[i].getTokens()[0]=='AOP'):
        Opr.append(TS[i].getTokens()[1])
        i=i+1

        if (SST12()):

            return True
    elif (TS[i].getTokens()[0] == ',' or TS[i].getTokens()[0] == ';'):
        if (M1()):
            return True
        elif (TS[i].getTokens()[0] == ';'):
            return True
    return False


def SST3():
    global i

    if (TS[i].getTokens()[0] == '='):
        i = i + 1
        if (TS[i].getTokens()[0] == 'new'):
            i = i + 1
            if (DT()):
                return True
    elif (TS[i].getTokens()[0] == '.'):
        if (P22()):
            if (TS[i].getTokens()[0] == 'AOP'):
                i = i + 1
                if (Q()):
                    return True
    return False


def SST2():

    global i
    global CrP
    global CN
    global CT
    global CS
    global CDrT
    global N
    global TM
    global AM
    global ST
    global OP
    global Types
    global Opr
    # if(TS[i].getTokens()[0]=='DT' or TS[i].getTokens()[0]=='ID' or TS[i].getTokens()[1]=='['): i=i+1  # im here if(DT1()): if(OBJ1()): return True elif(P()): if(TS[i].getTokens()[1]=='='): i=i+1 if(Q()): return True else: i=i-2 return False elif(TS[i].getTokens()[0]=='ID'): pass elif(ARRAYDEC1()): return True return False
    if (TS[i].getTokens()[0] == '['):
        i = i + 1

        if (SST11()):

            if (TS[i].getTokens()[0] == ';'):
                Types.clear()
                Opr.clear()
                i = i + 1
                return True
    elif (TS[i].getTokens()[0] == 'ID'):
        N=TS[i].getTokens()[1]
        i = i + 1

        if (SST10()):
            if (TS[i].getTokens()[0] == ';'):
                i = i + 1
                Types.clear()
                Opr.clear()
                return True


    elif (TS[i].getTokens()[0] == 'this' or TS[i].getTokens()[0] == 'super'):
        i = i + 1
        if (TS[i].getTokens()[0] == '.'):
            i = i + 1

            if (this1() or super1()):
                return True
    return False


def SST1():
    global i
    global CrP
    global CN
    global CT
    global CS
    global CDrT
    global N
    global TM
    global AM
    global ST
    global OP
    global Types
    global Opr
    if (TS[i].getTokens()[0] == '('):
        CS=createscope()
        i = i + 1

        if (ARGS2()):

            if (TS[i].getTokens()[1] == ')'):
                i = i + 1
                if (OPT3()):

                    if (TS[i].getTokens()[1] == ';'):
                        i = i + 1

                        return True
    elif (TS[i].getTokens()[0] == 'ID'):

        N=TS[i].getTokens()[1]

        i = i + 1

        if (SST7()):
            if (TS[i].getTokens()[1] == ';'):
                k=insertST(N,Types[0],CS)
                if(k):
                    i = i + 1
                    Opr.clear()
                    Types.clear()
                    return True
                else:
                    return False


    # if(OBJ1()):return True elif (TS[i].getTokens()[1] == '='):i=i+1if(Q()):return True elif(TS[i].getTokens()[1] == '('):if(SST1()):return True
    elif (TS[i].getTokens()[0] == '['):
        i = i + 1

        if (SST9()):
            if (TS[i].getTokens()[1] == ';'):
                i = i + 1
                return True
    elif (TS[i].getTokens()[1] == '.'):

            if (P22()):

                if (TS[i].getTokens()[0] == 'AOP'):
                    Opr.append(TS[i].getTokens()[1])

                    i = i + 1

                    if (Q()):
                        for j in range(len(Opr)):
                            if(Opr[len(Opr) - j - 1]!='not'):
                                type = compatibility(Types[len(Types) - 2], Types[len(Types) - 1], Opr[len(Opr) - j - 1])
                            else:
                                type=compatibility2(Types[len(Types) - 2],Opr[len(Opr) - j - 1])
                            if (type != False):
                                Types.pop()
                                Types.pop()
                                Types.append(type)

                            # print(Types)
                            # print(Opr)
                            else:
                                print('Type Mis-match')
                                return False
                        if (TS[i].getTokens()[1] == ';'):
                            i = i + 1
                            Types.clear()
                            Opr.clear()
                            return True
    elif (TS[i].getTokens()[1] == '='):

        Opr.append(TS[i].getTokens()[1])
        i = i + 1

        if (SST12()):

           for j in range(len(Opr)):

               if (Opr[len(Opr) - j - 1] != 'not'):
                   type = compatibility(Types[len(Types) - 2], Types[len(Types) - 1], Opr[len(Opr) - j - 1])
               else:
                   type = compatibility2(Types[len(Types) - 2], Opr[len(Opr) - j - 1])

               if(type!=False):
                  Types.pop()
                  Types.pop()
                  Types.append(type)

                 # print(Types)
                 # print(Opr)
               else:
                   print('Type Mis-match')
                   return False
           if(TS[i].getTokens()[0] == ';'):
                i = i + 1
                Types.clear()
                Opr.clear()
                return True
    elif (TS[i].getTokens()[0] == 'INC/DEC'):
        if (INCDEC()):
            if (TS[i].getTokens()[0] == ';'):
                i = i + 1
                return True
    elif (TS[i].getTokens()[0] == 'this' or TS[i].getTokens()[0] == 'super'):
        i = i + 1
        if (TS[i].getTokens()[0] == '.'):
            i = i + 1

            if (this1() or super1()):
                return True
    return False


def SST():
    global i
    global CrP
    global CN
    global CT
    global CS
    global CDrT
    global N
    global TM
    global AM
    global ST
    global OP
    global Types


    if (TS[i].getTokens()[0] == 'ID'):


        Type=lookupST(TS[i].getTokens()[1],CS,CN)

        if(Type!=False):
            Types.append(Type)
            ST=ST+Type
            N=TS[i].getTokens()[1]
            i = i + 1
            if (SST1()):
                return True




        elif(lookUpCT(TS[i].getTokens()[1])):

            N=TS[i].getTokens()[1]
            i=i+1
            Types.append(N)
            if (SST1()):
                return True
        else:
            print(TS[i].getTokens()[1]+' is not declared')


    elif (TS[i].getTokens()[0] == 'DT'):

        Types.append(TS[i].getTokens()[1])

        ST=ST+TS[i].getTokens()[1]

        i = i + 1

        if (SST2()):

            return True
    # elif(FUNC_DEF()):

    #  return True
    elif (TS[i].getTokens()[1] == 'floop'):

        if (FORLOOP()):
            return True
    elif (TS[i].getTokens()[1] == 'wloop'):

        if (WHILELOOP()):
            return True
    elif (TS[i].getTokens()[1] == 'if'):

        if (IF_ST()):
            return True
    elif (TS[i].getTokens()[0] == 'INC/DEC'):
        if (INCDEC()):
            return True

    elif (TS[i].getTokens()[0] == 'this' or TS[i].getTokens()[0] == 'super'):
        i = i + 1
        if (TS[i].getTokens()[0] == '.'):
            i = i + 1

            if (this1() or super1()):
                return True
    return False


def MST():
    global i
    global CrP
    global CN
    global CT
    global CS
    global CDrT
    global N
    global TM
    global AM
    global ST
    global Types
    # if(TS[i].getTokens()[1]=='static' or TS[i].getTokens()[1]=='public' or TS[i].getTokens()[1]=='private' or TS[i].getTokens()[1]=='protected'): if(SST()):if(MST()):return True
    if (TS[i].getTokens()[0] == 'ID'):

        if (SST()):

            if (MST()):
                return True
            else:
                return True
    elif (TS[i].getTokens()[0] == 'DT'):

        if (SST()):

            if (MST()):
                return True


    elif (TS[i].getTokens()[0] == 'floop'):

        if (SST()):
            if (MST()):
                return True
    elif (TS[i].getTokens()[1] == 'wloop'):
        if (SST()):
            if (MST()):
                return True
    elif (TS[i].getTokens()[1] == 'if'):
        if (SST()):
            if (MST()):
                return True
    elif (TS[i].getTokens()[1] == '++' or TS[i].getTokens()[1] == '--'):
        if (SST()):

            if (MST()):
                return True
    elif (TS[i].getTokens()[0] == 'this' or TS[i].getTokens()[0] == 'super'):
        if (SST()):
            if (MST()):
                return True

    elif (TS[i].getTokens()[1] == '}'):
        return True
    else:
        return False


def ARGS():
    global i

    if (TS[i].getTokens()[0] == ')'):
        return True
    elif (TS[i].getTokens()[0] == 'DT' or TS[i].getTokens()[0] == 'ID'):
        if (DT()):
            if (X1()):

                if (NEXT()):
                    return True
    return False


def AMs():
    global i

    if (TS[i].getTokens()[1] == 'public' or TS[i].getTokens()[1] == 'private' or TS[i].getTokens()[1] == 'protected'):

        i = i + 1
        return True
    elif (TS[i].getTokens()[0] == 'class' or TS[i].getTokens()[0] == 'ID' or TS[i].getTokens()[0] == 'DT'):
        return True
    return False


def CONSTRUCTOR_CALLING():
    global i

    if (TS[i].getTokens()[0] == "super"):
        i = i + 1
        if (TS[i].getTokens()[0] == "("):
            i = i + 1
            if (ARGS2()):
                if (TS[i].getTokens()[0] == ")"):
                    i = i + 1
                    if (TS[i].getTokens()[0] == ";"):
                        i = i + 1
                        return True
    elif (TS[i].getTokens()[0] == "this"):

        i = i + 1

        if (TS[i].getTokens()[0] == "("):
            i = i + 1
            if (ARGS2()):
                if (TS[i].getTokens()[0] == ")"):
                    i = i + 1
                    if (TS[i].getTokens()[0] == ";"):
                        i = i + 1
                        return True

    elif (TS[i].getTokens()[1] == "static" or TS[i].getTokens()[0] == "AM" or TS[i].getTokens()[0] == "ID" or
          TS[i].getTokens()[0] == "DT" or TS[i].getTokens()[0] == "floop" or TS[i].getTokens()[0] == "wloop" or
          TS[i].getTokens()[0] == "if" or TS[i].getTokens()[0] == "INC/DEC"):
        return True
    return False


def CONSTRUCTOR():
    global i
    if (TS[i].getTokens()[0] == "AM"):
        if (AMs()):
            if (TS[i].getTokens()[0] == "ID"):
                i = i + 1
                if (TS[i].getTokens()[0] == "("):
                    i = i + 1
                    if (ARGS()):
                        if (TS[i].getTokens()[0] == ")"):
                            i = i + 1
                            if (TS[i].getTokens()[0] == "{"):
                                i = i + 1
                                if (CONSTRUCTOR_CALLING()):
                                    if (MST()):
                                        if (TS[i].getTokens()[0] == "}"):
                                            i = i + 1
                                            return True
    return False


def OBJ():
    global i
    global Types
    global Opr

    if (TS[i].getTokens()[0] == "DT" or TS[i].getTokens()[0] == "ID"):

        if (DT()):

            if (TS[i].getTokens()[0] == "ID"):

                i = i + 1

                if (TS[i].getTokens()[0] == "AOP"):
                    i = i + 1
                    if (TS[i].getTokens()[0] == "new"):
                        i = i + 1
                        if (DT()):
                            if (TS[i].getTokens()[0] == "("):
                                i = i + 1
                                if (ARGS2()):
                                    if (TS[i].getTokens()[0] == ")"):
                                        i = i + 1
                                        return True
                else:

                    i = i - 2
                    return False
            else:

                i = i - 1
                return False

    return False


def this_super2():
    global i

    if (X()):
        return True
    elif (TS[i].getTokens()[0] == "("):
        i = i + 1
        if (ARGS2()):

            if (TS[i].getTokens()[0] == ")"):
                i = i + 1
                if (TS[i].getTokens()[0] == ";"):
                    i = i + 1

                    if (X()):
                        return True

    return False


def this1():
    global i

    if (TS[i].getTokens()[0] == "ID"):
        i = i + 1

        if (this_super2()):

            return True
        elif (TS[i].getTokens()[0] == 'AOP'):

            i = i + 1
            if (Q()):
                if (TS[i].getTokens()[0] == ';'):
                    i = i + 1

                    return True

    return False


def super1():
    global i
    if (TS[i].getTokens()[0] == "ID"):
        i = i + 1
        if (this_super2()):
            return True
    return False


def F3():
    global i
    if (TS[i].getTokens()[0] == "PM"):
        if (X()):
            return True
    elif (TS[i].getTokens()[0] == "["):
        i = i + 1
        if (OE()):
            if (TS[i].getTokens()[0] == "]"):
                i = i + 1
                if (X()):
                    return True
    return False


def F2():
    global i
    if (TS[i].getTokens()[0] == "INC/DEC"):
        i = i + 1
        return
    elif (TS[i].getTokens()[1] == "PM" or TS[i].getTokens()[1] == "]" or TS[i].getTokens()[1] == "and" or
          TS[i].getTokens()[1] == "or" or TS[i].getTokens()[0] == ")" or TS[i].getTokens()[0] == ";" or
          TS[i].getTokens()[1] == ","):

        return True
    return False


def F1():
    global i

    if (TS[i].getTokens()[0] == "PM"):
        if (X()):

            if (F2()):
                return True
    elif (TS[i].getTokens()[0] == "MDM" or TS[i].getTokens()[0] == "]" or TS[i].getTokens()[0] == "ROP" or
          TS[i].getTokens()[0] == "and" or TS[i].getTokens()[0] == "or" or TS[i].getTokens()[0] == ")" or
          TS[i].getTokens()[0] == "]" or TS[i].getTokens()[0] == ";" or TS[i].getTokens()[0] == ","):

        return True
    elif (TS[i].getTokens()[0] == "("):
        i = i + 1
        if (ARGS2()):
            if (TS[i].getTokens()[0] == ")"):
                i = i + 1
                if (X()):
                    return True
    elif (TS[i].getTokens()[0] == "["):
        i = i + 1
        if (OE()):
            if (TS[i].getTokens()[0] == "]"):
                if (F3()):
                    return True
    elif (TS[i].getTokens()[1] == '.'):

        if (P22()):

            if (TS[i].getTokens()[0] == 'AOP'):
                i = i + 1
                if (Q()):
                    if (TS[i].getTokens()[1] == ';'):
                        i = i + 1
                        return True
            elif (TS[i].getTokens()[0] == ';' or TS[i].getTokens()[0] == ')'):

                return True
    return False


def F():
    global i
    global CrP
    global CN
    global CT
    global CS
    global CDrT
    global N
    global TM
    global AM
    global ST
    global OP
    global N2

    global Types

    if (TS[i].getTokens()[0] == "ID"):

        i = i + 1

        if (F1()):
            return True
    elif (regex.charConstant(TS[i].getTokens()[1]) == "char" or regex.stringConst(
            TS[i].getTokens()[1]) == "string" or regex.integerConstant(
            TS[i].getTokens()[1]) == "int" or regex.floatConst(TS[i].getTokens()[1]) == "float"):
        Types.append(regex.stringConst(TS[i].getTokens()[1]))

        i = i + 1

        if (X()):
            return True
    elif (TS[i].getTokens()[0] == "INC/DEC"):
        i = i + 1
        if (TS[i].getTokens()[0] == "ID"):
            if (X()):
                return True
    elif (TS[i].getTokens()[0] == "NOT"):
        i = i + 1
        if (F()):
            return True
    elif (TS[i].getTokens()[0] == "("):
        i = i + 1
        if (OE()):
            if (TS[i].getTokens()[0] == ")"):
                i = i + 1
                return True
    elif (TS[i].getTokens()[0] == "this"):
        i = i + 1
        if (TS[i].getTokens()[0] == "."):
            i = i + 1
            if (this1()):
                return True
    elif (TS[i].getTokens()[0] == "super"):
        i = i + 1
        if (TS[i].getTokens()[0] == "."):
            i = i + 1
            if (super1()):
                return True

    return False


def T1():
    global i
    m=''
    o=''
    m=len(Types)
    o=len(Opr)

    if (TS[i].getTokens()[0] == "MDM"):
        Opr.append(TS[i].getTokens()[1])

        i = i + 1

        if (F()):

            type=compatibility(Types[m-1],Types[m],Opr[o])
            if(type!=False):
                Opr.pop(o)
                Types.pop(m)
                Types.pop(m-1)

                Types.insert(m-1,type)

                if (T1()):
                    return True
            else:
                'Type Mismatch'
    elif (TS[i].getTokens()[0] == 'PM' or TS[i].getTokens()[0] == ']' or TS[i].getTokens()[0] == 'ROP' or
          TS[i].getTokens()[0] == 'or' or TS[i].getTokens()[0] == 'and' or TS[i].getTokens()[0] == ';' or
          TS[i].getTokens()[0] == ',' or TS[i].getTokens()[0] == ')'):

        return True
    return False


def T():
    global i
    global CrP
    global CN
    global CT
    global CS
    global CDrT
    global N
    global TM
    global AM
    global ST
    global OP
    global N2
    global Types
    if (TS[i].getTokens()[0] == 'ID' or regex.charConstant(
            TS[i].getTokens()[1]) == "char" or regex.stringConst(
        TS[i].getTokens()[1]) == "string" or regex.integerConstant(
        TS[i].getTokens()[1]) == 'int' or regex.floatConst(TS[i].getTokens()[1]) == "float" or
            TS[i].getTokens()[0] == 'INC/DEC' or TS[i].getTokens()[0] == '(' or TS[i].getTokens()[0] == 'not' or
            TS[i].getTokens()[0] == 'this' or TS[i].getTokens()[0] == 'super'):

        if (F()):

            if (T1()):

                return True
    return False


def X():
    global i
    m=''
    m=len(Types)
    if (TS[i].getTokens()[0] == "PM"):

        Opr.append(TS[i].getTokens()[1])

        i = i + 1

        if (T()):

            if (X()):
                return True
    # elif(TS[i].getTokens()[1]=="static" or TS[i].getTokens()[1]=="public" or TS[i].getTokens()[1]=="private" or TS[i].getTokens()[1]=="protected" or TS[i].getTokens()[0]=="ID" or TS[i].getTokens()[0]=="DT" or  TS[i].getTokens()[1]=="floop" or TS[i].getTokens()[1]=="wloop" or  TS[i].getTokens()[1]=="if" or TS[i].getTokens()[1]=="++" or TS[i].getTokens()[1]=="--" or TS[i].getTokens()[1]=="," or  TS[i].getTokens()[1]=="[" or TS[i].getTokens()[1]=="]" or  TS[i].getTokens()[1]==";" or TS[i].getTokens()[1]==")"   ):
    elif (TS[i].getTokens()[0] == ')' or TS[i].getTokens()[0] == ']' or TS[i].getTokens()[0] == 'ROP' or
          TS[i].getTokens()[0] == 'LOP' or TS[i].getTokens()[0] == ';' or TS[i].getTokens()[0] == ',' or
          TS[i].getTokens()[0] == 'PM' or TS[i].getTokens()[0] == 'MDM' or TS[i].getTokens()[0] == 'INC/DEC' or
          TS[i].getTokens()[0] == '}' or TS[i].getTokens()[0] == 'this' or TS[i].getTokens()[0] == 'super'):

        return True

    return False


def E():
    global i
    global CrP
    global CN
    global CT
    global CS
    global CDrT
    global N
    global TM
    global AM
    global ST
    global OP
    global N2
    global Types
    if (TS[i].getTokens()[0] == 'ID' or regex.charConstant(
            TS[i].getTokens()[1]) == "char" or regex.stringConst(
        TS[i].getTokens()[1]) == "string" or regex.integerConstant(
        TS[i].getTokens()[1]) == 'int' or regex.floatConst(TS[i].getTokens()[1]) == "float" or
            TS[i].getTokens()[0] == 'INC/DEC' or TS[i].getTokens()[0] == '(' or TS[i].getTokens()[0] == 'not' or
            TS[i].getTokens()[0] == 'this' or TS[i].getTokens()[0] == 'super'):

        if (T()):

            if (X()):
                return True
    return False


def RE1():
    global i

    if (TS[i].getTokens()[0] == "ROP"):
        i = i + 1

        if (E()):

            if (RE1()):
                return True
    #  elif(TS[i].getTokens()[1]=="static" or TS[i].getTokens()[1]=="public" or TS[i].getTokens()[1]=="private" or TS[i].getTokens()[1]=="protected" or TS[i].getTokens()[0]=="ID" or TS[i].getTokens()[0]=="DT" or  TS[i].getTokens()[1]=="floop" or TS[i].getTokens()[1]=="wloop" or  TS[i].getTokens()[1]=="if" or TS[i].getTokens()[1]=="++" or TS[i].getTokens()[1]=="--" or TS[i].getTokens()[1]=="," or  TS[i].getTokens()[1]=="[" or TS[i].getTokens()[1]=="]" or  TS[i].getTokens()[1]==";" or TS[i].getTokens()[1]==")"   ):
    elif (TS[i].getTokens()[0] == ')' or TS[i].getTokens()[0] == ']' or TS[i].getTokens()[1] == 'and' or
          TS[i].getTokens()[1] == 'or' or TS[i].getTokens()[0] == ';' or TS[i].getTokens()[0] == ','):
        return True
    return False


def RE():
    global i
    global CrP
    global CN
    global CT
    global CS
    global CDrT
    global N
    global TM
    global AM
    global ST
    global OP
    global N2
    global Types
    if (TS[i].getTokens()[0] == 'ID' or regex.charConstant(
            TS[i].getTokens()[1]) == "char" or regex.stringConst(
        TS[i].getTokens()[1]) == "string" or regex.integerConstant(
        TS[i].getTokens()[1]) == 'int' or regex.floatConst(TS[i].getTokens()[1]) == "float" or
            TS[i].getTokens()[0] == 'INC/DEC' or TS[i].getTokens()[0] == '(' or TS[i].getTokens()[0] == 'not' or
            TS[i].getTokens()[0] == 'this' or TS[i].getTokens()[0] == 'super'):

        if (E()):

            if (RE1()):
                return True
    return False


def AE1():
    global i
    if (TS[i].getTokens()[0] == "LOP"):
        if (TS[i].getTokens()[1] == "and"):
            i = i + 1
            if (RE()):
                if (AE1()):
                    return True
    # elif(TS[i].getTokens()[1]=="static" or TS[i].getTokens()[1]=="public" or TS[i].getTokens()[1]=="private" or TS[i].getTokens()[1]=="protected" or TS[i].getTokens()[0]=="ID" or TS[i].getTokens()[0]=="DT" or  TS[i].getTokens()[1]=="floop" or TS[i].getTokens()[1]=="wloop" or  TS[i].getTokens()[1]=="if" or TS[i].getTokens()[1]=="++" or TS[i].getTokens()[1]=="--" or TS[i].getTokens()[1]=="," or  TS[i].getTokens()[1]=="[" or TS[i].getTokens()[1]=="]" or  TS[i].getTokens()[1]==";" or TS[i].getTokens()[1]==")"   ):
    elif (TS[i].getTokens()[0] == ')' or TS[i].getTokens()[0] == ']' or TS[i].getTokens()[0] == 'or' or
          TS[i].getTokens()[0] == ';' or TS[i].getTokens()[0] == ','):

        return True
    return False


def AE():
    global i
    global CrP
    global CN
    global CT
    global CS
    global CDrT
    global N
    global TM
    global AM
    global ST
    global OP
    global N2
    global Types

    if (TS[i].getTokens()[0] == 'ID' or regex.charConstant(
            TS[i].getTokens()[1]) == "char" or regex.stringConst(
        TS[i].getTokens()[1]) == "string" or regex.integerConstant(
        TS[i].getTokens()[1]) == 'int' or regex.floatConst(TS[i].getTokens()[1]) == "float" or
            TS[i].getTokens()[0] == 'INC/DEC' or TS[i].getTokens()[0] == '(' or TS[i].getTokens()[0] == 'not' or
            TS[i].getTokens()[0] == 'this' or TS[i].getTokens()[0] == 'super'):

        if (RE()):

            if (AE1()):
                return True
    return False


def OE1():
    global i

    if (TS[i].getTokens()[0] == "LOP"):
        if (TS[i].getTokens()[1] == "or"):
            i = i + 1
            if (AE()):
                if (OE1()):
                    return True
    # elif(TS[i].getTokens()[1]=="static" or TS[i].getTokens()[1]=="public" or TS[i].getTokens()[1]=="private" or TS[i].getTokens()[1]=="protected" or TS[i].getTokens()[0]=="ID" or TS[i].getTokens()[0]=="DT" or  TS[i].getTokens()[1]=="floop" or TS[i].getTokens()[1]=="wloop" or  TS[i].getTokens()[1]=="if" or TS[i].getTokens()[1]=="++" or TS[i].getTokens()[1]=="--" or TS[i].getTokens()[1]=="," or  TS[i].getTokens()[1]=="[" or TS[i].getTokens()[1]=="]" or  TS[i].getTokens()[1]==";" or TS[i].getTokens()[1]==")"   ):
    elif (TS[i].getTokens()[0] == ')' or TS[i].getTokens()[0] == ']' or TS[i].getTokens()[0] == ';' or
          TS[i].getTokens()[0] == ','):

        return True
    return False


def OE():
    global i
    global CrP
    global CN
    global CT
    global CS
    global CDrT
    global N
    global TM
    global AM
    global ST
    global OP
    global N2
    global Types
    if (TS[i].getTokens()[0] == "ID" or regex.charConstant(
            TS[i].getTokens()[1]) == "char" or regex.stringConst(
            TS[i].getTokens()[1]) == "string" or regex.floatConst(
            TS[i].getTokens()[1]) == "float" or regex.integerConstant(TS[i].getTokens()[1]) == "int" or
            TS[i].getTokens()[0] == "INC/DEC" or TS[i].getTokens()[0] == "NOT" or TS[i].getTokens()[0] == "this" or
            TS[i].getTokens()[0] == "super"):

        if (AE()):

            if (OE1()):
                return True
        elif (TS[i].getTokens()[0] == ';'):
            #   i=i+1 WITHOUT ANALYZE COMMENT KIYA HAI

            return True

    return False


def M1():
    global i
    global CrP
    global CN
    global CT
    global CS
    global CDrT
    global N
    global TM
    global AM
    global ST
    global OP
    global N2

    if (TS[i].getTokens()[1] == ','):
        i = i + 1
        k=insertST(N,ST,CS)
        if (k and TS[i].getTokens()[0] == 'ID'):
            i = i + 1

            if (M()):
                return True
    elif (TS[i].getTokens()[1] == 'public' or TS[i].getTokens()[1] == 'private' or TS[i].getTokens()[1] == 'protected'):
        #  i=i+1  //yaha comment analyze kiye baghair lagaya hai
        return True
    elif (TS[i].getTokens()[0] == ';'):

        return True
    return False


def M():
    global i,AM,TM,Types,CN,N
    if (TS[i].getTokens()[1] == '='):
        i = i + 1
        if (OE()):
            if (M1()):
                return True
    elif (TS[i].getTokens()[1] == ','):
        if(insertCDT(N,Types[0],AM,TM,CN)):
            i = i + 1
            if (TS[i].getTokens()[0] == 'ID'):
                N=TS[i].getTokens()[1]
                i = i + 1
                if (M()):
                    return True
    elif (TS[i].getTokens()[0] == ';'):
        return True
    return False


def NEXT2():
    global i

    if (TS[i].getTokens()[0] == ","):
        i = i + 1

        if (OE()):

            if (TS[i].getTokens()[0] == ';'):
                i = i + 1
                return True
            elif (NEXT2()):

                return True
            elif (MST()):

                return True
    elif (TS[i].getTokens()[0] == ")"):

        return True
    return False


def NEXT():
    global i

    if (TS[i].getTokens()[0] == ","):
        i = i + 1

        if (DT()):

            if (X1()):

                if (NEXT()):
                    return True
    elif (TS[i].getTokens()[0] == ")"):

        return True
    return False


def ARGS2():
    global i

    if (TS[i].getTokens()[0] == "ID" or regex.charConstant(
            TS[i].getTokens()[1]) == "char" or regex.stringConst(
            TS[i].getTokens()[1]) == "string" or regex.integerConstant(
            TS[i].getTokens()[1]) == 'int' or regex.floatConst(TS[i].getTokens()[1]) == "float" or
            TS[i].getTokens()[0] == "INC/DEC" or TS[i].getTokens()[0] == "NOT" or TS[i].getTokens()[0] == "this" or
            TS[i].getTokens()[0] == "super"):

        if (Q()):

            if (NEXT2()):
                return True
    elif (TS[i].getTokens()[0] == ')'):

        return True
    return False


def CLASS_BODY3():
    global i

    if (TS[i].getTokens()[0] == "ID"):
        i = i + 1
        if (CLASS_BODY1()):
            return True
    elif (TS[i].getTokens()[0] == "("):
        i = i + 1

        if (ARGS()):

            if (TS[i].getTokens()[0] == ")"):
                i = i + 1

                if (TS[i].getTokens()[0] == "{"):
                    i = i + 1

                    if (CONSTRUCTOR_CALLING()):

                        if (MST()):

                            if (TS[i].getTokens()[0] == "}"):
                                i = i + 1
                                if (CLASS_BODY()):
                                    return True
    return False


def CLASS_BODY2():
    global i
    global N
    global Types
    global Opr
    Types.clear()
    Opr.clear()
    if (TS[i].getTokens()[0] == "DT"):
        Types.append(TS[i].getTokens()[1])
        i = i + 1
        if (TS[i].getTokens()[0] == "ID"):
            N=TS[i].getTokens()[1]
            i = i + 1

            if (CLASS_BODY1()):

                return True
            elif (NEXT2()):

                return True
    elif (TS[i].getTokens()[0] == "ID"):

        i = i + 1

        if (CLASS_BODY3()):
            return True
    return False


def CLASS_BODY1():
    global i,N,Types,Opr,CN,TM,AM

    if (TS[i].getTokens()[0] == "AOP" or TS[i].getTokens()[0] == ','):

        if (M()):

            if (TS[i].getTokens()[1] == ";"):
                if(insertCDT(N,Types[0],AM,TM,CN)):
                    i = i + 1
                    Types.clear()
                    Opr.clear()
                    if (CLASS_BODY()):
                        return True
                else:
                    print("Redeclaration on line "+i)
                    return False
    elif (TS[i].getTokens()[0] == "("):
        i = i + 1

        if (ARGS()):
            if (TS[i].getTokens()[1] == ")"):
                i = i + 1
                if (TS[i].getTokens()[1] == "{"):
                    i = i + 1
                    if (MST()):
                        if (TS[i].getTokens()[1] == "}"):
                            i = i + 1
                            if (CLASS_BODY()):
                                return True

    return False


def defs():
    global i

    if (TS[i].getTokens()[0] == "AM" or TS[i].getTokens()[0] == 'class'):

        if (CLASSDEF()):

            if (defs()):

                return True

        elif (TS[i].getTokens()[1] == 'public'):
            return True
    elif (TS[i].getTokens()[0] == '$'):
        return True

    return False


def INH():
    global i
    global CrP
    if (TS[i].getTokens()[0] == ':'):

        i = i + 1

        if (TS[i].getTokens()[0] == 'ID'):
            k=lookUpCT(TS[i].getTokens()[1])

            if(k):

                CrP=CrP+TS[i].getTokens()[1]

                i = i + 1
                return True
            else:
                print('Your Inherited Class is not accessible')
                return False
    elif (TS[i].getTokens()[0] == '{'):
        return True

    return False


def DEC():
    global i
    if (TS[i].getTokens()[0] == "AM" or TS[i].getTokens()[0] == 'o_static'):
        if (O_STATIC()):
            if (AMs()):
                if (DT()):
                    if (TS[i].getTokens()[0] == 'ID'):
                        i = i + 1
                        if (M()):
                            if (TS[i].getTokens()[0] == ";"):
                                i = i + 1
                                return True
    return False


def O_STATIC():
    global i

    if (TS[i].getTokens()[0] == "AM" or TS[i].getTokens()[0] == 'o_static'):
        if (TS[i].getTokens()[1] == 'static'):
            i = i + 1
            return True
        return True
    return True


def FUNC_DEF():
    global i

    if (TS[i].getTokens()[0] == "AM" or TS[i].getTokens()[0] == 'o_static' or TS[i].getTokens()[0] == "DT" or
            TS[i].getTokens()[0] == "ID"):

        if (O_STATIC()):

            if (AMs()):
                pass

            if (DT()):

                if (TS[i].getTokens()[0] == "ID"):
                    i = i + 1
                    if (TS[i].getTokens()[0] == "("):

                        i = i + 1

                        if (ARGS()):

                            if (TS[i].getTokens()[0] == ")"):
                                i = i + 1

                            if (TS[i].getTokens()[0] == "{"):

                                i = i + 1

                                if (MST()):

                                    if (TS[i].getTokens()[0] == "}"):
                                        i = i + 1

                                        return True

    return False


def CLASS_BODY():
    global i
    global TM,AM,T,Types,Opr
    AM=''
    TM=''

    if (TS[i].getTokens()[0] == 'o_static'):
        if (TS[i].getTokens()[1] == 'static'):

            i = i + 1

            if (AMs()):

                if (DT()):

                    if (CLASS_BODY1()):

                        return True
                    else:
                        i = i - 3
    elif (TS[i].getTokens()[0] == "AM"):
        i = i + 1

        if (CLASS_BODY2()):

            return True
        elif (TS[i].getTokens()[1] == 'public'):
            return True

    elif (TS[i].getTokens()[0] == "DT" or TS[i].getTokens()[0] == "ID"):

        if (OBJ()):

            if (CLASS_BODY()):
                return True
        elif (CLASS_BODY2()):

            return True


    elif (TS[i].getTokens()[0] == "}"):

        return True

    return False


def INCDEC():
    global i
    if (TS[i].getTokens()[0] == "INC/DEC"):
        i = i + 1

        return True
    return False


def FORLOOP1():
    global i
    # if(TS[i].getTokens()[1] == "static" or TS[i].getTokens()[1] == "public" or TS[i].getTokens()[1] == "private" or TS[i].getTokens()[1] == "protected"):
    #    if(DEC()):
    #       return True
    if (TS[i].getTokens()[0] == "ID"):

        if (P()):
            return True
    return False


def FORLOOP():
    global i
    if (TS[i].getTokens()[0] == "floop"):
        i = i + 1
        if (TS[i].getTokens()[0] == "("):
            i = i + 1

            if (P()):
                if (TS[i].getTokens()[0] == 'AOP'):
                    i = i + 1
                    if (Q()):

                        if (TS[i].getTokens()[0] == ";"):
                            i = i + 1

                            if (OE()):

                                if (TS[i].getTokens()[0] == ";"):

                                    i = i + 1
                                    if (TS[i].getTokens()[0] == "ID"):
                                        i = i + 1

                                        if (INCDEC()):

                                            if (TS[i].getTokens()[0] == ")"):
                                                i = i + 1
                                                if (TS[i].getTokens()[0] == "{"):
                                                    i = i + 1

                                                    if (MST()):
                                                        if (TS[i].getTokens()[0] == "}"):
                                                            i = i + 1
                                                            return True
    return False


def WHILELOOP():
    global i
    if (TS[i].getTokens()[0] == "wloop"):
        i = i + 1
        if (TS[i].getTokens()[0] == "("):
            i = i + 1
            if (COND()):
                if (TS[i].getTokens()[0] == ")"):
                    i = i + 1
                    if (TS[i].getTokens()[0] == "{"):
                        i = i + 1
                        if (MST()):
                            if (TS[i].getTokens()[0] == "}"):
                                i = i + 1
                            return True
    return False


def S():
    global i
    global CrP
    global CN
    global CT
    global CS
    global CDrT
    global N
    global TM
    global AM
    if (TS[i].getTokens()[0] == "AM" or TS[i].getTokens()[0] == 'class'):

        if (defs() or TS[i].getTokens()[0] == 'AM'):

            if (TS[i].getTokens()[1] == 'public'):

                i = i + 1

                if (TS[i].getTokens()[0] == 'class'):
                    CrP=''
                    CN=''
                    CT=''
                    CT='class'
                    i = i + 1

                    if (TS[i].getTokens()[1] == 'Main'):
                        CN=TS[i].getTokens()[1]
                        i = i + 1
                        if (TS[i].getTokens()[0] == '('):
                            i = i + 1
                            if (TS[i].getTokens()[0] == ')'):
                                i = i + 1

                                if (INH()):
                                    k=insertCT(CN,CT,CrP)

                                    if (k and TS[i].getTokens()[0] == '{'):
                                        i = i + 1

                                        if (CLASS_BODY() or TS[i].getTokens()[1] == 'static'):

                                            if (TS[i].getTokens()[1] == 'static'):
                                                TM = TS[i].getTokens()[1]
                                                i = i + 1


                                                if (TS[i].getTokens()[1] == 'public'):
                                                    AM=TS[i].getTokens()[1]
                                                    i = i + 1

                                                    if (TS[i].getTokens()[1] == 'void'):
                                                        CDrT='void'
                                                        i = i + 1
                                                        if (TS[i].getTokens()[1] == 'main'):
                                                            N=TS[i].getTokens()[1]
                                                            i = i + 1

                                                            if (TS[i].getTokens()[1] == '('):
                                                                i = i + 1
                                                                CS=createscope()
                                                                CDrT=CDrT+'-->'+'void'
                                                                if (TS[i].getTokens()[1] == ')'):
                                                                    i = i + 1
                                                                    k=insertCDT(N,CDrT,AM,TM,CN)
                                                                    if (k and TS[i].getTokens()[1] == '{'):
                                                                        i = i + 1
                                                                        Types.clear()
                                                                        Opr.clear()
                                                                        if (MST()):

                                                                            if (TS[i].getTokens()[1] == '}'):
                                                                                i = i + 1

                                                                                if (CLASS_BODY()):

                                                                                    if (TS[i].getTokens()[1] == '}'):

                                                                                        i = i + 1

                                                                                        if (defs()):
                                                                                            return True

    return False


def SA(TS=[]):
    global i
    if (S()):

        if (TS[i].getTokens()[1] == '$'):
            return True

    print("Invalid Syntax at line number", TS[i].getTokens()[2])


def main():
    global TS
    TS = CC1.main()
    if ((TS[-1].getTokens()[1]) == '$'):
        print("Successfully Parsed")
    S = SA(TS)
    if (S):

        print("Syntax Analyzer Completed Successfully")
    return TS


main()
