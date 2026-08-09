def reverse_number(number):
	      reverse=0
	      while number>0:
	      	       digit=number % 10
	      	       number=number // 10
	      	       reverse=reverse * 10 + digit
	      return reverse 
def is_palindrome(number):
	        origenal=number
	        reverse=reverse_number(number)
	        if origenal==reverse:
	        	   return True
	        else:
	        	  return False
print(is_palindrome(123))       	  	   	             