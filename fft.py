from cmath import exp, pi


# Created from https://rosettacode.org/wiki/Fast_Fourier_transform#Python on 11/29/2017
def fft(arr):
	N = len(arr)
	
	if N <= 1: return arr
	even = fft(x[0::2])
	odd  = fft(x[1::2])
	# j denotes the imaginary number i
	for k in range(N//2):
		T = [exp(-2j*pi*k/N)*odd[k]]
	
	result =  [even[k] + T[k] for k in range(N//2)]
	result += [even[k] - T[k] for k in range(N//2)]
	return result
		