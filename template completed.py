"""
RECORD CHECK  -  my version
===========================

Name  : Veer Nanwani
Lane  : AI 
Date  : 26/09/2026
"""

label = input("Enter the label: ")
first = int(input("Enter the first value: ")) 
second =int(input("Enter the second value: "))    
difference = second-first   
percent = (first/second)*100     
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"First      : {first:>10.2f}")
print(f"Second     : {second:>10.2f}")
print(f"Difference : {difference:>+10.2f}")
print(f"Percent    :{percent:>10.2f}%")
print("=" * 34)
