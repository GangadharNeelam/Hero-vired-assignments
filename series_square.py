#Squares Of Each Element
import pandas as pd                                   
ran = int(input("Enter no.of iterarations : "))   
user=[]
sqr=[]       
for i in range(ran):
    n=int(input("Enter a number:"))                                                          
    user.append(n)                             
    sqr.append(n*n)    
res=pd.Series(sqr,index=[user])         
print(res)    