# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 20:01:22 2022

@author: tonyl
Name = Anthony Lomeli
22, August 2022


"""
def payment(pv, rAPR, nMonths):
    """ 
    pv: TYPE; floating point number 
        DESCRIPION: how much money I borrow
    
    rAPR: TYPE: Float 
        Description: annual % interest rate
        
    nMonths: TYPE; Integer 
        DESCRIPTION: Term of loan, or length of the loan. 
        
    ---

    Payment: TYPE: Float, 
        DESCRIPTION: Monthly payment. 
    --- 
    """
    pmt= rAPR/1200*pv/(1-(1+(rAPR/1200))**(-nMonths))
    
    return pmt 
"""
write a loop! 
input pv, n , rAPR
print out the input variables 
print out the payment 
and loop back to get a new case 


if pv is put in a '0' exit the loop 
"""
while(1):
   pv = input('input pv')
   if pv is == '0':
      break
     print(pv)
print("out of the loop")

#pv = 39000
#nMonths = 48
#rAPR = 7

#carPayment = payment(pv, rAPR, nMonths)
#carPayment = payment (41232, 3.5, 36)
""" 
we input values instead of the locations, and it runs it in orders that we
listed above. 

""" 
#paymentDollars = payment(float.(input('input.pv'), 6, 30)
#pv = input("enter amount to borrow" )
#print("Payment = {:.2f}".format(paymentDollars))
#print('my payment for my loan is ${:.2f} '.format(round(carPayment,2)))
    
    
    






