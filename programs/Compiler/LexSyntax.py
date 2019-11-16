import CC1
import regex
import json
TS=[]
i = 0


def ARRAYDEC():
    global i
    if (TS[i].getTokens()[0] == "DT"):
        if(DT2()):
            if (TS[i].getTokens()[0] == "["):
                i=i+1
                if(E()):
                    if (TS[i].getTokens()[0] == "]"):
                        i=i+1
                        if(OPT()):
                            if (TS[i].getTokens()[0] == "ID"):
                                i=i+1
                                if(OPT2()):
                                    return True
    return False

def FUNC_CALL():
    global i
    if(TS[i].getTokens()[0]=="ID"):
        i=i+1
        if(TS[i].getTokens()[0]=="("):
            i=i+1
            if(ARGS2()):
                if(TS[i].getTokens()[0]==")"):
                    i=i+1
                    if(TS[i].getTokens()[0]==";"):
                        i=i+1
                        return True
    return False
def COND():
    global i
    if (TS[i].getTokens()[0] == "ID" or regex.integerConstant(TS[i].getTokens()[1]) == "integer_const" or TS[i].getTokens()[0] == "INC/DEC" or TS[i].getTokens()[0] == "NOT" or TS[i].getTokens()[0] == "this" or TS[i].getTokens()[0] == "super"):
        if(OE()):
            return True
    elif(TS[i].getTokens()[1]=="true" or TS[i].getTokens()[1]=="false"):
        return True
    return False


def IF_ST():
    global i
    if(TS[i].getTokens()[1]=="if"):
        i=i+1
        if(TS[i].getTokens()[1]=="("):
            i=i+1
            if(COND()):
                if(TS[i].getTokens()[1]==")"):
                    i=i+1
                    if(TS[i].getTokens()[1]=="{"):
                        i=i+1
                        if(MST()):
                            if(TS[i].getTokens()[1]=="}"):
                                if(OELIF()):
                                    if(OELSE):
                                        return True
    return False

def OELIF():
    global  i
    if(TS[i].getTokens()[0]=="elif"):
        i=i+1
        if(IF_ST()):
            return True
    elif(TS[i].getTokens()[0]=="else"):
        return True
    return False
def OELSE():
    global i
    if(TS[i].getTokens()[0]=="else"):
        if(TS[i].getTokens()[0]=="{"):
            i=i+1
            if(MST()):
                if(TS[i].getTokens()[0]=="}"):
                    i=i+1
                    return True
    return False
def Q():
    global i
    if(TS[i].getTokens()[0]=="ID" or regex.integerConstant(TS[i].getTokens()[1])=="integer_const" or TS[i].getTokens()[0]=="INC/DEC" or TS[i].getTokens()[0]=="NOT" or TS[i].getTokens()[0]=="this" or TS[i].getTokens()[0]=="super" ):
        i=i+1
        return True
    return False
def ASSIGN():
    global i
    if(TS[i].getTokens()[0]=='ID'):
        if(P()):
            if(TS[i].getTokens()[1]=='='):
                i=i+1
                if(Q()):
                    return True
    return False

def CLASSDEF():
    global i
   # print(TS[i].getTokens()[1])

    if(TS[i].getTokens()[0]=='AM'):



        if(AM()):


            if(TS[i].getTokens()[0]=='class'):


                i=i+1

                if(TS[i].getTokens()[0]=='ID'):

                    i=i+1


                    if(INH()):


                        if(TS[i].getTokens()[1]=='{'):
                            i=i+1

                            if(CLASS_BODY()):

                                if(TS[i].getTokens()[1]=='}'):
                                    i=i+1

                                    return True
                    else:
                        i=i-3

    return False

def OPT():
    global i
    if(TS[i].getTokens()[0]=='['):
        i=i+1
        if(OE()):
            if(TS[i].getTokens()[1]==']'):
                i=i+1
    elif(TS[i].getTokens()[0]=='ID' or TS[i].getTokens()[0]=='.' or TS[i].getTokens()[0]==',' or TS[i].getTokens()[0]==')'):
        i=i+1
        return True
    return False
def OPT2():
    global i
    if(TS[i].getTokens()[0]==','):
        i=i+1
        if(TS[i].getTokens()[0]=='ID'):
            i=i+1
            if(OPT2()):
                return True
    elif(TS[i].getTokens()[1]==';'):
        i=i+1
        return True
    return False
def P():
    global i
    if(TS[i].getTokens()[0]=='ID'):
        i=i+1

        if(P22()):


            return True

    return True
    return False

def P1():
    global i
    if(TS[i].getTokens()[0]=='.'):
        if(P()):
            return True
    elif(TS[i].getTokens()[1]=='='):
        i=i+1
        return True
    return False

def P22():

    if(TS[i].getTokens()[0]=='.'):
        if(P1()):
            return True
    return False
def DT2():
    global i
    if(TS[i].getTokens()[0]=='DT' or  TS[i].getTokens()[0]=='ID'):
        i=i+1
        return True
    return False

def DT1():
    global i

    if(TS[i].getTokens()[0]=='['):
        i=i+1
        if(TS[i].getTokens()[0]==']'):
            i=i+1
            if(TS[i].getTokens()[0]=='['):
                i=i+1
                if(TS[i].getTokens()[0]==']'):
                    i=i+1
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
    if(TS[i].getTokens()[0]=='DT' or TS[i].getTokens()[0]=='ID'):
        i=i+1
        if(DT1()):
            return True
    return False
def Y1():
    global i
    if(TS[i].getTokens()[0]=="["):
        i=i+1
        if(OE()):
            if(OPT()):
                return True
    elif(TS[i].getTokens()[0]=="," or TS[i].getTokens()[0]==")"):
        return True
    return False
def X1():
    global i

    if(TS[i].getTokens()[0]=='ID'):
        i=i+1
        if(Y1()):

            return True
    return False


def ARRAYDEC1():
    global i
    if(TS[i].getTokens()[0]=='['):
        i=i+1
        if(E()):
            if(TS[i].getTokens()[1]==']'):
                if(OPT()):
                    if(TS[i].getTokens()[0]=='ID'):
                        i=i+1
                        if(OPT2()):
                            return True
    return False

def OBJ1():
    global i


    if(TS[i].getTokens()[0]=='ID'):

        if(TS[i].getTokens()[0]=='ID'):
            i=i+1

            if(TS[i].getTokens()[1]=='='):

                i=i+1


                if(TS[i].getTokens()[1]=='new'):
                    i=i+1
                    if(DT()):
                        if(TS[i].getTokens()[1]=='('):
                            i=i+1
                            if(ARGS2()):
                                if(TS[i].getTokens()[1]==')'):
                                    i=i+1
                                    if(TS[i].getTokens()[1]==';'):
                                        i=i+1
                                        return True
                else:
                    i=i-2

    return False
def SST13():
    global i
    if (TS[i].getTokens()[0] == '['):
        i = i + 1
        if(TS[i].getTokens()[0] == ']'):
            i=i+1

        if (SST12()):
            return True
    elif (TS[i].getTokens()[0] == 'ID'):
        if (SST7()):
            return True
    return False
def SST12():
    global i

    if (TS[i].getTokens()[0] == 'ID' or TS[i].getTokens()[0] == 'integer_const' or TS[i].getTokens()[0] == 'INC/DEC' or TS[i].getTokens()[0] == '(' or TS[i].getTokens()[0] == 'not' or TS[i].getTokens()[0] == 'this' or TS[i].getTokens()[0] == 'super'):

        if (OE()):

            if (M1()):

                return True
    elif (TS[i].getTokens()[0] == 'new'):
        if (DT()):
            if(TS[i].getTokens()[0] == '('):
                i=i=1
                if(ARGS2()):
                    if(TS[i].getTokens()[0] == ')'):
                        i=i+1
                        return True

    return False

def SST11():
    global i
    if (TS[i].getTokens()[0] == 'ID' or TS[i].getTokens()[0] == 'integer_const' or TS[i].getTokens()[0] == 'INC/DEC' or TS[i].getTokens()[0] == '(' or TS[i].getTokens()[0] == 'not' or TS[i].getTokens()[0] == 'this' or TS[i].getTokens()[0] == 'super'):
        if (E()):
            if (TS[i].getTokens()[0] == ']'):
                i = i + 1
                if (OPT()):
                    if (TS[i].getTokens()[0] == 'ID'):
                        i = i + 1
                        if (OPT2()):
                            return True
    elif (TS[i].getTokens()[0] == ']'):
        if (SST13()):
            return True
    return False
def SST10():
    global i

    if(TS[i].getTokens()[0] == 'AOP'):
        i=i+1

        if(SST12()):

            return True

    elif(TS[i].getTokens()[0] == ','):
        if(M1()):
            return True
    elif(TS[i].getTokens()[0] == '.'):
        if(P22()):
            if(TS[i].getTokens()[0] == 'AOP'):
                i=i+1
                if(Q()):
                    if(TS[i].getTokens()[0] == '('):
                        i=i+1
                        if(ARGS2()):
                            if(TS[i].getTokens()[0] == ')'):
                                return True

    return False
def SST9():
    global i
    if(TS[i].getTokens()[0] == 'ID' or TS[i].getTokens()[0] == 'integer_const' or TS[i].getTokens()[0] == 'INC/DEC' or TS[i].getTokens()[0] == '(' or TS[i].getTokens()[0] == 'not' or TS[i].getTokens()[0] == 'this' or TS[i].getTokens()[0] == 'super'):
        if(E()):
            if(TS[i].getTokens()[0] == ']'):
                i=i+1
                if(OPT()):
                    if(TS[i].getTokens()[0] == 'ID'):
                        i=i+1
                        if(OPT2()):
                            return True
    elif(TS[i].getTokens()[0] == ']'):
        if(SST8()):
            return True
    return False
def SST8():
    global i
    if (TS[i].getTokens()[0] == '['):
        i = i + 1
        if(TS[i].getTokens()[0] == ']'):
            i=i+1
            if(TS[i].getTokens()[0] == 'ID'):
                i=i+1
                if(M()):
                    return True

    elif (TS[i].getTokens()[0] == 'ID'):
        if (M()):
            return True
    return False

def SST7():
    global i
    if(TS[i].getTokens()[0] == '='):
        if(SST12()):
            if(TS[i].getTokens()[0] == ';'):
                return True
    elif(TS[i].getTokens()[0] == ',' or TS[i].getTokens()[0] == ';'):
        if(M1()):
            return True
        elif(TS[i].getTokens()[0] == ';'):
            return True
    return False
def SST3():
    global i

    if (TS[i].getTokens()[0] == '='):
        i=i+1
        if (TS[i].getTokens()[0] == 'new'):
            i=i+1
            if(DT()):
                return True
    elif(TS[i].getTokens()[0]=='.'):
        if(P22()):
            if(TS[i].getTokens()[0]=='AOP'):
                i=i+1
                if(Q()):
                    return True
    return False
def SST2():
    global i

   # if(TS[i].getTokens()[0]=='DT' or TS[i].getTokens()[0]=='ID' or TS[i].getTokens()[1]=='['): i=i+1  # im here if(DT1()): if(OBJ1()): return True elif(P()): if(TS[i].getTokens()[1]=='='): i=i+1 if(Q()): return True else: i=i-2 return False elif(TS[i].getTokens()[0]=='ID'): pass elif(ARRAYDEC1()): return True return False
    if(TS[i].getTokens()[0]=='['):
        i=i+1
        if(SST11()):
            return True
    elif(TS[i].getTokens()[0]=='ID'):
        i=i+1

        if(SST10()):
            return True
    return False
def SST1():
    global i



    if(TS[i].getTokens()[0]=='('):
        i=i+1
        if(ARGS2()):
            if(TS[i].getTokens()[1]==')'):
                i=i+1
                if(TS[i].getTokens()[1]==';'):
                    i=i+1

                    return True
    elif(TS[i].getTokens()[0]=='ID'):
        i=i+1
        if(SST7()):
            if (TS[i].getTokens()[1] == ';'):
                i = i + 1
                return True


       # if(OBJ1()):return True elif (TS[i].getTokens()[1] == '='):i=i+1if(Q()):return True elif(TS[i].getTokens()[1] == '('):if(SST1()):return True
    elif(TS[i].getTokens()[0]=='['):
        if(SST9()):
            if (TS[i].getTokens()[1] == ';'):
                i = i + 1
                return True
    elif(TS[i].getTokens()[1]=='.'):
        if(P22()):
            if (TS[i].getTokens()[0] == 'AOP'):
                i = i + 1
                if(Q()):
                    if (TS[i].getTokens()[1] == ';'):
                        i = i + 1
                        return True
    return False

def SST():
    global i


    if(TS[i].getTokens()[0]=='ID'):
        i=i+1
        if(SST1()):

            return True
    elif(TS[i].getTokens()[0]=='DT'):
        i=i+1

        if(SST2()):


            return True
       # elif(FUNC_DEF()):

          #  return True
    elif(TS[i].getTokens()[1]=='floop'):
        if(FORLOOP()):
            return True
    elif(TS[i].getTokens()[1]=='wloop'):
        if(WHILELOOP()):
            return True
    elif(TS[i].getTokens()[1]=='if'):
        if(IF_ST()):
            return True
    elif(TS[i].getTokens()[0]=='INC/DEC' ):
        if(INCDEC()):
            return True
    return False
def MST():
    global i

    if(TS[i].getTokens()[1]=='static' or TS[i].getTokens()[1]=='public' or TS[i].getTokens()[1]=='private' or TS[i].getTokens()[1]=='protected'):

        if(SST()):

            if(MST()):
                return True
    elif(TS[i].getTokens()[0]=='ID'):

        if(SST()):

            if (TS[i].getTokens()[0] == ';'):

                i = i + 1


                if(MST()):
                        return True
                else:
                    return True
    elif(TS[i].getTokens()[0]=='DT'):

        if(SST()):

            if(TS[i].getTokens()[0]==';'):


                i=i+1


                if(MST()):

                    return True
                else:


                    return True
            else:
                return True

    elif(TS[i].getTokens()[1]=='floop'):
        if(SST()):
            if(MST()):
                return True
    elif(TS[i].getTokens()[1]=='wloop'):
        if(SST()):
            if(MST()):
                return True
    elif(TS[i].getTokens()[1]=='if'):
        if(SST()):
            if(MST()):
                return True
    elif(TS[i].getTokens()[1]=='++' or TS[i].getTokens()[1]=='--' ):
        if(SST()):
            if(MST()):
                return True
    elif(TS[i].getTokens()[1]=='}'):
        return True
    else:
       return False

def ARGS():
    global i

    if(TS[i].getTokens()[0]==')'):
        return True
    elif(TS[i].getTokens()[0]=='DT' or  TS[i].getTokens()[0]=='ID'):
        if(DT()):
            if(X1()):

               if(NEXT()):

                    return True
    return False


def AM():
    global i

    if(TS[i].getTokens()[1]=='public' or TS[i].getTokens()[1]=='private' or TS[i].getTokens()[1]=='protected' ):

        i=i+1
        return True

    return False
def CONSTRUCTOR_CALLING():
    global i

    if(TS[i].getTokens()[0]=="super"):
        i=i+1
        if(TS[i].getTokens()[0]=="("):
            i=i+1
            if(ARGS2()):
                if(TS[i].getTokens()[0]==")"):
                    i=i+1
                    if(TS[i].getTokens()[0]==";"):
                        i=i+1
                        return True
    elif(TS[i].getTokens()[0]=="this"):
        i=i+1
        if(TS[i].getTokens()[0]=="("):
            i=i+1
            if(ARGS2()):
                if(TS[i].getTokens()[0]==")"):
                    i=i+1
                    if(TS[i].getTokens()[0]==";"):
                        i=i+1
                        return True
    elif(TS[i].getTokens()[1]=="static" or TS[i].getTokens()[0]=="AM" or TS[i].getTokens()[0]=="ID" or TS[i].getTokens()[0]=="DT" or TS[i].getTokens()[0]=="floop" or TS[i].getTokens()[0]=="wloop" or TS[i].getTokens()[0]=="if" or TS[i].getTokens()[0]=="INC/DEC" ):
        return True
    return False

def CONSTRUCTOR():
    global i
    if(TS[i].getTokens()[0]=="AM"):
        if(AM()):
            if(TS[i].getTokens()[0]=="ID"):
                i=i+1
                if(TS[i].getTokens()[0]=="("):
                    i=i+1
                    if(ARGS()):
                        if(TS[i].getTokens()[0]==")"):
                            i=i+1
                            if(TS[i].getTokens()[0]=="{"):
                                i=i+1
                                if(CONSTRUCTOR_CALLING()):
                                    if(MST()):
                                        if(TS[i].getTokens()[0]=="}"):
                                            i=i+1
                                            return True
    return False

def OBJ():
    global i

    if(TS[i].getTokens()[0]=="DT" or TS[i].getTokens()[0]=="ID"):
        if(DT()):

            if(TS[i].getTokens()[0]=="ID"):

                i=i+1
                if(TS[i].getTokens()[0]=="AOP"):
                    i=i+1
                    if(TS[i].getTokens()[0]=="new"):
                        i=i+1
                        if(DT()):
                            if(TS[i].getTokens()[0]=="("):
                                i=i+1
                                if(ARGS2()):
                                    if(TS[i].getTokens()[0]==")"):
                                        i=i+1
                                        return True
            else:
                i=i-1


    return False


def this_super2():
    global i
    if(X()):
        return True
    elif(TS[i].getTokens()[0]=="("):
        if(ARGS2()):
            if (TS[i].getTokens()[0] == ")"):
                if (TS[i].getTokens()[0] == ";"):
                    if(X()):
                        return True
    return False

def this1():
    global i
    if(TS[i].getTokens()[0]=="ID" ):
        i=i+1
        if(this_super2()):
            return True
    return False
def super():
    global i
    if(TS[i].getTokens()[0]=="ID" ):
        i=i+1
        if(this_super2()):
            return True
    return False
def F3():
    global i
    if(TS[i].getTokens()[0]=="PM"):
        if(X()):
            return True
    elif(TS[i].getTokens()[0]=="["):
        i=i+1
        if(OE()):
            if(TS[i].getTokens()[0]=="]"):
                i=i+1
                if(X()):
                    return True
    return False

def F2():
    global i
    if(TS[i].getTokens()[0]=="INC/DEC"):
        i=i+1
        return
    elif(TS[i].getTokens()[1]=="static" or TS[i].getTokens()[1]=="public" or TS[i].getTokens()[1]=="private" or TS[i].getTokens()[1]=="protected" or TS[i].getTokens()[0]=="ID" or TS[i].getTokens()[0]=="DT" or  TS[i].getTokens()[1]=="floop" or TS[i].getTokens()[1]=="wloop" or  TS[i].getTokens()[1]=="if" or TS[i].getTokens()[1]=="++" or TS[i].getTokens()[1]=="--" or TS[i].getTokens()[1]=="," or  TS[i].getTokens()[1]=="[" or TS[i].getTokens()[1]=="]" or  TS[i].getTokens()[1]==";" or TS[i].getTokens()[1]==")"   ):
        i=i+1
        return True
    return False

def F1():
    global i
    if(TS[i].getTokens()[0]=="PM"):
        if(X()):
            if(F2()):
                return True
    elif(TS[i].getTokens()[0]=="("):
        i=i+1
        if(ARGS2()):
            if(TS[i].getTokens()[0]==")"):
                i=i+1
                if(X()):
                    return True
    elif(TS[i].getTokens()[0]=="["):
        i=i+1
        if(OE()):
            if(TS[i].getTokens()[0]=="]"):
                if(F3()):
                    return True
    return False



def F():
    global i
    if(TS[i].getTokens()[0]=="ID" ):
        i=i+1
        if(F1()):
            return True
    elif(regex.integerConstant(TS[i].getTokens()[1])=="integer_const" ):
        i=i+1
        if(X()):
            return True
    elif(TS[i].getTokens()[0]=="INC/DEC" ):
        i=i+1
        if(TS[i].getTokens()[0]=="ID"):
            if(X()):
                return True
    elif (TS[i].getTokens()[0] == "NOT" ):
        i = i + 1
        if (F()):
            return True
    elif(TS[i].getTokens()[0]=="("):
        i=i+1
        if (OE()):
            if (TS[i].getTokens()[0]==")"):
                i=i+1
                return True
    elif (TS[i].getTokens()[0] == "this"):
        i = i + 1
        if (TS[i].getTokens()[0] == "."):
            i=i+1
            if(this1()):
                return True
    elif (TS[i].getTokens()[0] == "super"):
        i = i + 1
        if (TS[i].getTokens()[0] == "."):
            i=i+1
            if(super1()):
                return True

    return False
def T1():
    global i
    if(TS[i].getTokens()[0]=="MDM"):
        i=i+1
        if(F()):
            if(T1()):
                return True
    elif(TS[i].getTokens()[1]=="static" or TS[i].getTokens()[1]=="public" or TS[i].getTokens()[1]=="private" or TS[i].getTokens()[1]=="protected" or TS[i].getTokens()[0]=="ID" or TS[i].getTokens()[0]=="DT" or  TS[i].getTokens()[1]=="floop" or TS[i].getTokens()[1]=="wloop" or  TS[i].getTokens()[1]=="if" or TS[i].getTokens()[1]=="++" or TS[i].getTokens()[1]=="--" or TS[i].getTokens()[1]=="," or  TS[i].getTokens()[1]=="[" or TS[i].getTokens()[1]=="]" or  TS[i].getTokens()[1]==";" or TS[i].getTokens()[1]==")"   ):
        i=i+1
        return True
    return False



def T():
    global i
    if(TS[i].getTokens()[0]=="ID" or regex.integerConstant(TS[i].getTokens()[1])=="integer_const" or TS[i].getTokens()[0]=="INC/DEC" or TS[i].getTokens()[0]=="NOT" or TS[i].getTokens()[0]=="this" or TS[i].getTokens()[0]=="super" ):

        if(F()):
            if(T1()):
                return True
    return False
def X():
    global i
    print(TS[i].getTokens()[0])
    if(TS[i].getTokens()[0]=="PM" ):
        i=i+1
        if(T()):
            if(X()):
                return True
    elif(TS[i].getTokens()[1]=="static" or TS[i].getTokens()[1]=="public" or TS[i].getTokens()[1]=="private" or TS[i].getTokens()[1]=="protected" or TS[i].getTokens()[0]=="ID" or TS[i].getTokens()[0]=="DT" or  TS[i].getTokens()[1]=="floop" or TS[i].getTokens()[1]=="wloop" or  TS[i].getTokens()[1]=="if" or TS[i].getTokens()[1]=="++" or TS[i].getTokens()[1]=="--" or TS[i].getTokens()[1]=="," or  TS[i].getTokens()[1]=="[" or TS[i].getTokens()[1]=="]" or  TS[i].getTokens()[1]==";" or TS[i].getTokens()[1]==")"   ):
        i=i+1
        return True
    return False


def E():
    global i
    if(TS[i].getTokens()[0]=="ID" or regex.integerConstant(TS[i].getTokens()[1])=="integer_const" or TS[i].getTokens()[0]=="INC/DEC" or TS[i].getTokens()[0]=="NOT" or TS[i].getTokens()[0]=="this" or TS[i].getTokens()[0]=="super" ):

        if(T()):
            if(X()):
                return True
    return False

def RE1():
    global i
    if(TS[i].getTokens()[0]=="ROP" ):
        i=i+1
        if(E()):
            if(RE1()):
                return True
    elif(TS[i].getTokens()[1]=="static" or TS[i].getTokens()[1]=="public" or TS[i].getTokens()[1]=="private" or TS[i].getTokens()[1]=="protected" or TS[i].getTokens()[0]=="ID" or TS[i].getTokens()[0]=="DT" or  TS[i].getTokens()[1]=="floop" or TS[i].getTokens()[1]=="wloop" or  TS[i].getTokens()[1]=="if" or TS[i].getTokens()[1]=="++" or TS[i].getTokens()[1]=="--" or TS[i].getTokens()[1]=="," or  TS[i].getTokens()[1]=="[" or TS[i].getTokens()[1]=="]" or  TS[i].getTokens()[1]==";" or TS[i].getTokens()[1]==")"   ):
        i=i+1
        return True
    return False


def RE():
    global i
    if(TS[i].getTokens()[0]=="ID" or regex.integerConstant(TS[i].getTokens()[1])=="integer_const" or TS[i].getTokens()[0]=="INC/DEC" or TS[i].getTokens()[0]=="NOT" or TS[i].getTokens()[0]=="this" or TS[i].getTokens()[0]=="super" ):

        if(E()):

            if(RE1()):
                return True
    return False

def AE1():
    global i
    if(TS[i].getTokens()[0]=="LOP" ):
        if(TS[i].getTokens()[1]=="and" ):
            i=i+1
            if(RE()):
                if(AE1()):
                    return True
    elif(TS[i].getTokens()[1]=="static" or TS[i].getTokens()[1]=="public" or TS[i].getTokens()[1]=="private" or TS[i].getTokens()[1]=="protected" or TS[i].getTokens()[0]=="ID" or TS[i].getTokens()[0]=="DT" or  TS[i].getTokens()[1]=="floop" or TS[i].getTokens()[1]=="wloop" or  TS[i].getTokens()[1]=="if" or TS[i].getTokens()[1]=="++" or TS[i].getTokens()[1]=="--" or TS[i].getTokens()[1]=="," or  TS[i].getTokens()[1]=="[" or TS[i].getTokens()[1]=="]" or  TS[i].getTokens()[1]==";" or TS[i].getTokens()[1]==")"   ):
        i=i+1
        return True
    return False


def AE():
    global i
    if(TS[i].getTokens()[0]=="ID" or regex.integerConstant(TS[i].getTokens()[1])=="integer_const" or TS[i].getTokens()[0]=="INC/DEC" or TS[i].getTokens()[0]=="NOT" or TS[i].getTokens()[0]=="this" or TS[i].getTokens()[0]=="super" ):

        if(RE()):
            if(AE1()):
                return True
    return False
def OE1():
    global i
    if(TS[i].getTokens()[0]=="LOP" ):
        if(TS[i].getTokens()[1]=="or" ):
            i=i+1
            if(AE()):
                if(OE1()):
                    return True
    elif(TS[i].getTokens()[1]=="static" or TS[i].getTokens()[1]=="public" or TS[i].getTokens()[1]=="private" or TS[i].getTokens()[1]=="protected" or TS[i].getTokens()[0]=="ID" or TS[i].getTokens()[0]=="DT" or  TS[i].getTokens()[1]=="floop" or TS[i].getTokens()[1]=="wloop" or  TS[i].getTokens()[1]=="if" or TS[i].getTokens()[1]=="++" or TS[i].getTokens()[1]=="--" or TS[i].getTokens()[1]=="," or  TS[i].getTokens()[1]=="[" or TS[i].getTokens()[1]=="]" or  TS[i].getTokens()[1]==";" or TS[i].getTokens()[1]==")"   ):
        i=i+1
        return True
    return False


def OE():
    global i

    if(TS[i].getTokens()[0]=="ID" or regex.integerConstant(TS[i].getTokens()[1])=="integer_const" or TS[i].getTokens()[0]=="INC/DEC" or TS[i].getTokens()[0]=="NOT" or TS[i].getTokens()[0]=="this" or TS[i].getTokens()[0]=="super" ):


        if(AE()):

            if(OE1()):
                return True
        elif(TS[i].getTokens()[0]==';'):
            i=i+1



            return True

    return False
def M1():
    global i

    if(TS[i].getTokens()[1]==','):
        i=i+1
        if(TS[i].getTokens()[0]=='ID'):
            i=i+1
            if(M()):
                return True
    elif(TS[i].getTokens()[1]=='public' or TS[i].getTokens()[1]=='private' or TS[i].getTokens()[1]=='protected'):
        i=i+1
        return True
    return False
def M():
    global i
    if(TS[i].getTokens()[1]=='=' or TS[i].getTokens()[1]=='public' or TS[i].getTokens()[1]=='private' or TS[i].getTokens()[1]=='protected'):
        i=i+1
        if(OE()):
            if(M1()):
                return True
    elif(TS[i].getTokens()[1]==',' or TS[i].getTokens()[1]=='public' or TS[i].getTokens()[1]=='private' or TS[i].getTokens()[1]=='protected'):
        i=i+1
        return True
    return False


def NEXT2():
    global i


    if(TS[i].getTokens()[0]=="," ):
        i=i+1

        if(OE()):

            if(TS[i].getTokens()[0]==';'):
                i=i+1
                return True
            elif(NEXT2()):

                return True
            elif(MST()):


                return True
    elif(TS[i].getTokens()[0]==")" ):
        i=i+1
        return True
    return False
def NEXT():
    global i

    if(TS[i].getTokens()[0]==","):
        i=i+1
        if(DT()):

            if(X1()):
                if(NEXT()):
                    return True
    elif(TS[i].getTokens()[0]==")"):
        return True
    return False

def ARGS2():
    global i

    if(TS[i].getTokens()[0]=="ID" or regex.integerConstant(TS[i].getTokens()[1])=="integer_const" or TS[i].getTokens()[0]=="INC/DEC" or TS[i].getTokens()[0]=="NOT" or TS[i].getTokens()[0]=="this" or TS[i].getTokens()[0]=="super" ):
        if(OE()):
            if(NEXT2()):
                return True
    else:
        return False


def CLASS_BODY3():
    global i

    if(TS[i].getTokens()[0]=="ID"):
        i=i+1
        if(CLASS_BODY1()):
            return True
    elif(TS[i].getTokens()[0]=="("):
        i=i+1
        if(ARGS()):


            if(TS[i].getTokens()[0]==")"):
                i=i+1

                if(TS[i].getTokens()[0]=="{"):
                    i=i+1

                    if(CONSTRUCTOR_CALLING()):

                        if(MST()):
                            if(TS[i].getTokens()[0]=="}"):
                                i=i+1
                                if(CLASS_BODY()):
                                    return True
    return False


def CLASS_BODY2():
    global i

    if(TS[i].getTokens()[0]=="DT"):
        i=i+1

        if(TS[i].getTokens()[0]=="ID"):
            i=i+1

            if(CLASS_BODY1()):

                return True
            elif(NEXT2()):

                return True
    elif(TS[i].getTokens()[0]=="ID"):
        i=i+1

        if(CLASS_BODY3()):

            return True
    return False

def CLASS_BODY1():
    global i

    if(TS[i].getTokens()[0]=="AOP"):
        if(TS[i].getTokens()[1]=="="):
            i=i+1
            if(TS[i].getTokens()[1]==";"):
                i=i+1
                if(CLASS_BODY()):
                    return True
    elif(TS[i].getTokens()[0]=="("):
        i=i+1
        if(ARGS()):
            if(TS[i].getTokens()[1]==")"):
                i=i+1
                if(TS[i].getTokens()[1]=="{"):
                    i=i+1
                    if(MST()):
                        if(TS[i].getTokens()[1]=="}"):
                            if(CLASS_BODY()):
                                return True

    return False
def defs():
    global i

    if(TS[i].getTokens()[0]=="AM" or TS[i].getTokens()[0]=='class'  ):

        if(CLASSDEF()):



            if(defs()):

                return True

        elif(TS[i].getTokens()[1]=='public'):
            return True
    elif( TS[i].getTokens()[0]=='$'):
        return True

    return False

def INH():
    global i

    if(TS[i].getTokens()[0]==':'):

        i=i+1

        if(TS[i].getTokens()[0]=='ID' ):
            i=i+1
            return True
    elif(TS[i].getTokens()[0]=='{' ):
        return  True


    return False
def DEC():
    global i
    if(TS[i].getTokens()[0]=="AM" or  TS[i].getTokens()[0]=='o_static'):
        if(O_STATIC()):
            if(AM()):
                if(DT()):
                    if(TS[i].getTokens()[0]=='ID'):
                        i=i+1
                        if(M()):
                            if(TS[i].getTokens()[0]==";"):
                                i=i+1
                                return True
    return False
def O_STATIC():
    global i

    if(TS[i].getTokens()[0]=="AM" or  TS[i].getTokens()[0]=='o_static'):
        if(TS[i].getTokens()[1]=='static'):
            i=i+1
            return True
        return True
    return True

def FUNC_DEF():
    global i

    if(TS[i].getTokens()[0]=="AM" or  TS[i].getTokens()[0]=='o_static' or TS[i].getTokens()[0]=="DT"  or TS[i].getTokens()[0]=="ID" ):

        if(O_STATIC()):


            if(AM()):
               pass

            if(DT()):

                    if(TS[i].getTokens()[0]=="ID"):
                        i=i+1
                        if(TS[i].getTokens()[0]=="("):

                            i=i+1

                            if(ARGS()):


                                if(TS[i].getTokens()[0]==")"):

                                    i=i+1

                                if(TS[i].getTokens()[0]=="{"):

                                        i=i+1

                                        if(MST()):


                                            if(TS[i].getTokens()[0]=="}"):
                                                i=i+1

                                                return True

    return False


def CLASS_BODY():
    global i

    if( TS[i].getTokens()[0]=='o_static'):
        if(TS[i].getTokens()[1]=='static'):

            i=i+1

            if(AM()):

                if(DT()):

                    if(CLASS_BODY1()):

                        return True
                    else:
                        i=i-3
    elif(TS[i].getTokens()[0]=="AM"):
            i=i+1
            if(CLASS_BODY2()):

                return True
            elif(TS[i].getTokens()[1]=='public'):
                return True

    elif(TS[i].getTokens()[0]=="DT"  or TS[i].getTokens()[0]=="ID" ):

        if(DT()):

            if(OBJ()):

                if(CLASS_BODY()):
                    return True
            elif(CLASS_BODY2()):

                return True


    elif(TS[i].getTokens()[0]=="}"):
                return True

    return False



def INCDEC():
    global i
    if(TS[i].getTokens()[0] == "INC/DEC"):
        i=i+1


def FORLOOP1():
    global i
    if(TS[i].getTokens()[1] == "static" or TS[i].getTokens()[1] == "public" or TS[i].getTokens()[1] == "private" or TS[i].getTokens()[1] == "protected"):
        if(DEC()):
            return True
    elif(TS[i].getTokens()[0] == "ID"):
        if(P()):
            return True
    return False

def FORLOOP():
    global i
    if (TS[i].getTokens()[0] == "floop"):
        i=i+1
        if (TS[i].getTokens()[0] == "("):
            i=i+1
            if(FORLOOP1()):
                if(TS[i].getTokens()[0] == ";"):
                    i=i+1
                    if(OE()):
                        if (TS[i].getTokens()[0] == ";"):
                            i = i + 1
                            if(INCDEC()):
                                if (TS[i].getTokens()[0] == "ID"):
                                    i=i+1
                                    if(X()):
                                        if (TS[i].getTokens()[0] == ")"):
                                            i=i+1
                                            if (TS[i].getTokens()[0] == "{"):
                                                i=i+1
                                                if(MST()):
                                                    if (TS[i].getTokens()[0] == "}"):
                                                        return True
    return False


def WHILELOOP():
    global i
    if(TS[i].getTokens()[0] == "wloop"):
        i=i+1
        if(TS[i].getTokens()[0] == "("):
            i=i+1
            if(COND()):
                if(TS[i].getTokens()[0] == ")"):
                    i=i+1
                    if(TS[i].getTokens()[0] == "{"):
                        i=i+1
                        if(MST()):
                            if(TS[i].getTokens()[0] == "}"):
                                i=i+1
                            return True
    return False
def S():

    global i

    if(TS[i].getTokens()[0]=="AM" or  TS[i].getTokens()[0]=='class'):

        if(defs() or TS[i].getTokens()[0]=='AM'):

            if(TS[i].getTokens()[1]=='public'):
                i=i+1
                if(TS[i].getTokens()[0]=='class'):
                    i=i+1
                    if(TS[i].getTokens()[1]=='Main'):

                        i=i+1
                        if(TS[i].getTokens()[0]=='('):
                            i=i+1
                            if(TS[i].getTokens()[0]==')'):
                                i=i+1

                                if(INH() or TS[i].getTokens()[0]=='{'):

                                    if(TS[i].getTokens()[0]=='{'):
                                        i=i+1
                                        if(CLASS_BODY() or TS[i].getTokens()[1]=='static'):

                                            if(TS[i].getTokens()[1]=='static'):
                                                i=i+1

                                                if(TS[i].getTokens()[1]=='public'):
                                                    i=i+1
                                                    if(TS[i].getTokens()[1]=='void'):
                                                        i=i+1
                                                        if(TS[i].getTokens()[1]=='main'):
                                                            i=i+1

                                                            if(TS[i].getTokens()[1]=='('):
                                                                i=i+1
                                                                if(TS[i].getTokens()[1]==')'):
                                                                    i=i+1
                                                                    if(TS[i].getTokens()[1]=='{'):
                                                                        i=i+1

                                                                        if(MST()):


                                                                            if(TS[i].getTokens()[1]=='}'):
                                                                                i=i+1


                                                                                if(CLASS_BODY()):

                                                                                    if(TS[i].getTokens()[1]=='}'):

                                                                                        i=i+1


                                                                                        if(defs()):


                                                                                           return True



    return False




def SA(TS=[]):
    global i
    if(S()):

        if(TS[i].getTokens()[1]=='$'):
            return True


    print("Invalid Syntax at line number", TS[i].getTokens()[2])

def main():
    global TS
    TS=CC1.main()
    if((TS[-1].getTokens()[1])=='$'):
        print("Successfully Parsed")
    S=SA(TS)
    if(S):
        print("Syntax Analyzer Completed Successfully")
main()


