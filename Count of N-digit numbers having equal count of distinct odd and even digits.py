# Python program for the above approach:

## Stores the dp-states
dp = []

# Function to count set bits in an integer
# in Python
def __builtin_popcount(num):
	
	# convert given number into binary
	# output will be like bin(11)=0b1101
	binary = bin(num)

	# now separate out all 1's from binary string
	# we need to skip starting two characters
	# of binary string i.e; 0b
	setBits = [ones for ones in binary[2:] if ones=='1']
	return len(setBits)

## Recursive Function to find number
## of N-digit numbers which has equal
## count of distinct odd & even digits
def countOfNumbers(index, evenMask, oddMask, N):

	## If index is N + 1
	if (index == N + 1):

		## Find the count of set bits
		## in the evenMask
		countOfEvenDigits = __builtin_popcount(evenMask);

		## Find the count of set bits
		## in the oddMask
		countOfOddDigits = __builtin_popcount(oddMask);

		## If the count of set bits in both
		## masks are equal then return 1
		## as they have equal number of
		## distinct odd and even digits
		if (countOfOddDigits == countOfEvenDigits):
			return 1
		return 0

	val = dp[index][evenMask][oddMask]

	## If the state has already
	## been computed
	if (val != -1):
		return val

	val = 0

	## If current position is 1, then
	## any digit from [1-9] can be
	## placed

	## If N = 1, 0 can be also placed
	if (index == 1):

		st = 1
		if(N == 1):
			st = 0

		for digit in range(st, 10):

			## If digit is odd
			if (digit & 1) == 1:

				## Set the (digit/2)th bit
				## of the oddMask
				val += countOfNumbers(index + 1, evenMask, oddMask | (1 << (digit // 2)), N)

			## Set the (digit/2)th bit
			## of the number evenMask
			else:
				val += countOfNumbers(index + 1, evenMask | (1 << (digit // 2)), oddMask, N)

	## For remaining positions, any
	## digit from [0-9] can be placed
	else:
		for digit in range(10):

			## If digit is odd
			if (digit & 1) == 1:

				## Set the (digit/2)th
				## bit of oddMask
				val += countOfNumbers(index + 1, evenMask, oddMask | (1 << (digit // 2)), N)
			else:

				## Set the (digit/2)th
				## bit of evenMask
				val += countOfNumbers(index + 1, evenMask | (1 << (digit // 2)), oddMask, N)

	dp[index][evenMask][oddMask] = val

	## Return the answer
	return val

## Function to find number of N-digit
## numbers which has equal count of
## distinct odd and even digits
def countNDigitNumber(N):

	## Initialize dp array with -1
	for i in range(0, 100):
		dp.append([])
		for j in range(0, 1 << 5):
			dp[i].append([])
			for k in range(0, 1 << 5):
				dp[i][j].append(-1)

	## Function Call
	print(countOfNumbers(1, 0, 0, N))

## Driver code
if __name__=='__main__':

	N = 3
	countNDigitNumber(N)
