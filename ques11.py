# Python script to find the greater between the real and imaginary parts of a Complex Number.

def findRealAndImag(s) :
	l = len(s)
	i = 0
	if (s.find('+') != -1):
		i = s.find('+')
	else:
		i = s.find('-');
	real = s[:i]
	imaginary = s[i + 1:l - 1]
	print("Real part:", real)
	print("Imaginary part:", imaginary)
s = "3+4i";
findRealAndImag(s);
