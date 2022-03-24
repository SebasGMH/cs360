# Giuliani Martinez
# HW#1
# find all the function names, function return type (void or int), variable names, variable values and variable types (only integer or array element).

import pandas as pd

#read in txt file and copy source code into a string
source_txt = open("testfile.txt",'r')
source_string = source_txt.read()

#make df's for functions,LH vars, RH vars
func_ = {'name':[],'return_type':[]}
function_df = pd.DataFrame(func_)
# print(function_df)

Lh_var = {'name':[],'value':[],'type':[]}
Lh_var_df = pd.DataFrame(Lh_var)

rh_var = []
print (type(rh_var))

