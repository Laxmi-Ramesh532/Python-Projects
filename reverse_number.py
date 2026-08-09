def reverse_number(number):
	     reverse=0
	     while number > 0:
	     	       digit=number % 10
	     	       number=number // 10
	     	       reverse=reverse * 10 + digit
	     return reverse
print(reverse_number(12345))	     	       	     	    