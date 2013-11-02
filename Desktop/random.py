##Copyright (c) <2013> <Taehoon Lee, Elizabeth Zeng>
##
##Permission is hereby granted, free of charge, to any person obtaining a copy
##of this software and associated documentation files (the "Software"), to deal
##in the Software without restriction, including without limitation the rights
##to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##copies of the Software, and to permit persons to whom the Software is
##furnished to do so, subject to the following conditions:
##
##The above copyright notice and this permission notice shall be included in
##all copies or substantial portions of the Software.
##
##THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
##THE SOFTWARE.
##Version 3

import time

# This is a pseudo-random number generator that takes in a positive integer n,
# and returns a pseudo-random integer in the range of [0, n)

def random(n):

	# Checks that n is a positive integer, and raises an exception otherwise
	if not (type(n) == int) or n <= 0:
    		raise Exception
	
	# Gets a nice positive integer seed
	x = time.clock()
	while x < 1:
                x = x * 10
	x = (x * 12289) % 1000
	
	# Div will make sure we won’t get an integer too large in the for loop
	div = 6151
	while div < n:
    		div = div * div - 1

	# Makes sure we don't return 0 when n is 12289
	if n == 12289:
    		mult = 17497
	else:
    		mult = 12289

	for i in range(5):
   		x = (x * mult) % div

	return int(x % n)
