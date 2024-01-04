#!/usr/bin/env python
from collections import defaultdict
from functools import partial
f = open("7/in.raw", "r")
# f = open("7/sample.raw", "r")
lines = f.read().splitlines()

missing_entries={}
values={}

def get_value(x):
    if x.isdigit():
        return(int(x))
    else:
        return(values[x])

def op_not(x):
    return(~get_value(x))

def op_and(x,y):
    return(get_value(x) & get_value(y))

def op_or(x,y):
    return(get_value(x) | get_value(y))

def op_lshift(v,x):
    return(get_value(x)<<v)

def op_rshift(v,x):
    return(get_value(x)>>v)

def op_id(x):
    return(get_value(x))

for line in lines:
    input, output = line.split(' -> ')
    inputs = input.split(' ')
    match len(inputs):
        case 1:
            if inputs[0].isdigit():
              values[output] = int(inputs[0])
            else:
              missing_entries[output] = ((inputs[0],), op_id)
        case 2:
            assert(inputs[0]=="NOT")
            missing_entries[output] = ((inputs[1],), op_not)
        case 3:
            match inputs[1]:
                case 'AND':
                    missing_entries[output] = ((inputs[0], inputs[2],), op_and)
                case 'OR':
                    missing_entries[output] = ((inputs[0], inputs[2],), op_or)
                case 'LSHIFT':
                    missing_entries[output] = ((inputs[0],), partial(op_lshift,int(inputs[2])))
                case 'RSHIFT':
                    missing_entries[output] = ((inputs[0],), partial(op_rshift,int(inputs[2])))
                case _ :
                    raise Exception(f'Invalid operation "{inputs}" on "{line}"')
        case _ :
            raise Exception(f'Invalid inputs "{inputs}" on "{line}"')

missing = list(missing_entries.keys())
while missing:
    for m in missing:
        if all((input in values) or input.isdigit() for input in missing_entries[m][0]):
            values[m] = missing_entries[m][1](*missing_entries[m][0])
            del missing_entries[m]
    missing=list(missing_entries.keys())
print(values['a'])

# PART 2

missing_entries={}
values={}

for line in lines:
    input, output = line.split(' -> ')
    inputs = input.split(' ')
    match len(inputs):
        case 1:
            if inputs[0].isdigit():
              values[output] = int(inputs[0])
            else:
              missing_entries[output] = ((inputs[0],), op_id)
        case 2:
            assert(inputs[0]=="NOT")
            missing_entries[output] = ((inputs[1],), op_not)
        case 3:
            match inputs[1]:
                case 'AND':
                    missing_entries[output] = ((inputs[0], inputs[2],), op_and)
                case 'OR':
                    missing_entries[output] = ((inputs[0], inputs[2],), op_or)
                case 'LSHIFT':
                    missing_entries[output] = ((inputs[0],), partial(op_lshift,int(inputs[2])))
                case 'RSHIFT':
                    missing_entries[output] = ((inputs[0],), partial(op_rshift,int(inputs[2])))
                case _ :
                    raise Exception(f'Invalid operation "{inputs}" on "{line}"')
        case _ :
            raise Exception(f'Invalid inputs "{inputs}" on "{line}"')

values['b'] = 956

missing = list(missing_entries.keys())
while missing:
    for m in missing:
        if all((input in values) or input.isdigit() for input in missing_entries[m][0]):
            values[m] = missing_entries[m][1](*missing_entries[m][0])
            del missing_entries[m]
    missing=list(missing_entries.keys())
print(values['a'])
