import math 
import time 

start = time.time() 
math.factorial(100000) 
end = time.time() 
print(f"{end - start:.5f} sec")