# a=["a","b","c","d","e"]
# b=["f","g","h","i","j"]
# i=0
# while i<len(a):
#     n=a[i]+b[-i]
#     print(n)
#     i=i+1
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist") 