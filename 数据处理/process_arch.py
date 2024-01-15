import pandas as pd
import os

a=['\r\n', '\r\n ', '\r\n', '职称：教授', '\r\n', '学位：博士']
str='\r\n'
for i in range(0,len(a)-1):
    if str in a[i] and str in a[i+1]:
        a[i]=''
print(a)