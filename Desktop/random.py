import time

#This function takes an integer from the client, n, and returns a pseudorandom number from 0 to n-1 inclusive
def random(n):
	#The function uses the current time in seconds to create a random number
	x=time.clock()
	while x<1:
    		x=x*10
	x=(x*12289)%1000
	div=6151
	while div<n:
    		div=div*div-1
	for i in range(5):
   		x=(x*12289)%div
	return int(x % n)
