#Arthematic Operation On Two Series
import pandas as pd
series1 = pd.Series([4,8,16,32,64])
series2 = pd.Series([3,6,12,24,48])
print(f"First Series : {series1}")
print(f"second series: {series2}")
print(f"Add both series : {series1 + series2}")
print(f"Subtract both series : {series1 - series2}")
print(f"Multiply both series : {series1 * series2}") 
print(f"Divide both series : {series1 / series2}")
print(f"Floor division of both series : {series1 // series2}")
