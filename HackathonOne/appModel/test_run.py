#!/usr/bin/python3.5
'''
Created on 12-Nov-2018

@author: tsuser
'''
from Order import *
order_obj = order()
digit1, choice1 = order_obj.take_user_input(0)
digit2, choice2 = order_obj.take_user_input(1)
print ('You said digit '+str(digit2)+' and '+str(digit1)+' to confirm you order of '+str(choice2)+' quantity of '+str(choice1))
#print('You Said :{} and confirming order as {}'.format(digit, choice))
