#-------------------------------------------------------------------------------
# Name:        Euler_14
# Purpose:      Collatz Problem - Euler #14
#
# Author:      Stewart
#
# Created:     23/07/2012
# Copyright:   (c) Stewart 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

var = 1
chain = 1
test_chain = 0
biggest = 0
sub = 0
bank = [1]
temp_bank = [0]

while var < 10000:  #top limit
    sub = var
    test_chain = 0
    temp_bank = []
    while sub > 1:
        if sub in bank:
            test_chain += (len(bank) - bank.index(sub))
            if len(temp_bank) > chain or bank[0] == sub:
                bank =  temp_bank + bank[bank.index(sub) : len(bank)]
            break
        temp_bank.append(sub)
        if sub%2 == 0:
            sub = sub / 2
            test_chain = test_chain + 1
        else:
            sub = sub*3 +1
            test_chain = test_chain + 1

    if len(temp_bank) > len(bank):
        bank = temp_bank
    if test_chain > chain:
        chain = test_chain
        biggest = var
##    print 'VARIABLE: ' , var
##    print  'bank is ' , bank
##    print 'temp bank: ' , temp_bank
##    print 'test chain: ' , test_chain
##    print '-----------------'
    var += 1

print "The biggest number is ", biggest, ", with a chain of " , chain , '.'


