eq = '2*x+4=5*x-2'
j = complex(0,1)
eq1 = eval('2*j+4')
eq2 = eval('5*j-2')
#print(eq1-eq2)
import re
def equa_sol(eq):
    val_lst = re.findall(r'[a-zA-Z]',eq)
    #print(val)
    val = val_lst[0]
    loc_equal = eq.find('=')
    eq_left = eq[:loc_equal]
    eq_right = eq[loc_equal+1:]
    j = complex(0,1)
    eq_left = eq_left.replace(val,'j')
    eq_right = eq_right.replace(val,'j')
    #print(eq_left,eq_right)
    eq2 = eval(eq_left)-eval(eq_right)
    print(-eq2.real/eq2.imag)
equa_sol(eq)
