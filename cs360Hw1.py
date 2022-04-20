# Giuliani Martinez
# HW#1
# find all the function names, function return type (void or int), variable names, variable values and variable types (only integer or array element).

import pandas as pd
import regex as re

#what i am doing first is extracting the data, since 
#read in txt file and copy source code into a string
source_txt = open("testfile.txt",'r')
source_string = source_txt.read()
source_regex = r'\s'
stripped_source_string= re.sub(source_regex, ' ', source_string)
#print(source_string)

#make df's for functions,LH vars, RH vars
func_ = {'name':[],'return_type':[],'param':[]}
function_df = pd.DataFrame(func_)
# print(function_df)

Lh_var = {'name':[],'value':[],'type':[]}
Lh_var_df = pd.DataFrame(Lh_var)

rh_var = []
operations = ['+','-','/','*']

#first check for functions
#make a regex for each col of the df
func_name_regex = r'\w+\s(\w+)\(.*\)\{'
func_return_regex= r'(\w+)\s\w+\(.*\)\{'
func_param_regex= r'\w+\s\w+\((.*)\)\{'
test_re = r'\w+\s\w+\([^)]*\)\{.*[^;][^\s][^\}]'
print(re.findall(test_re,stripped_source_string))
#print(re.findall(func_name_regex,source_string),re.findall(func_return_regex,source_string), re.findall(func_param_regex,source_string))

#fill in funcdf
function_df['name']= re.findall(func_name_regex,source_string)
function_df['return_type']= re.findall(func_return_regex,source_string)
function_df['param']= re.findall(func_param_regex,source_string)
#print(function_df)

#check for lh vars
#make a seprate df for declarations and finals values?
#dont need a seprate df, can accomplish with an extra regex
#if i go the case regex way, ill have to make one for ints, arrays, and multiple declarations.
#will likely have to do seperate dfs because there is declaration, and arithmetix statement 

#declarations
#do the searches corresponding to a specific function, custom function?
#after finding functions, use stripped string 

#might not need a function specific search as it would be diff memory anyways
def fun_var_srch(function,search):
    return

#ints-single declaration
lhscalar_name_regex = r'int (\w+)=[^,\s;]*;'
lhscalar_type_regex = r'(int) \w+=[^,\s;]*;'
lhscalar_intial_regex = r'int \w+=([^,\s;]*);'

#before continuing test oout .split to return the contents of a string
#first return with the [^\}]
#multiple declarations

#arrays

lhvar_name_regex = r'\w+\s\w+='
lhvar_intial_regex = r''
lhvar_type_regex = r''
lhvar_value_regex = r''
var_test_regex=r'\w+.*=.*;'

#print(re.findall(lhscalar_name_regex,source_string), re.findall(lhscalar_type_regex,source_string),re.findall(lhscalar_intial_regex,source_string))


