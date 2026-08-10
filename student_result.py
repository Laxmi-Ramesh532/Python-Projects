def student_result(name , mark1 , mark2 , mark3):
	        if mark1>=33 and mark2>=33 and mark3>=33:
	        	       result= "pass"
	        else: 
	                  result= "fail" 	       
	        total=mark1 + mark2 + mark3
	        total_observation=300
	        percentage=total / 300 * 100
	        return name , total , percentage , result
def grade(percentage):	            
	        if percentage>=90:
	           	   return "grade A"
	        elif  percentage>=75:	   
	                  return"grade B"
	        elif percentage>=60:
	            	  return "grade C"      
	        elif percentage>=45:
	            	  return "grade D" 	  
	        elif percentage>=33:
	            	  return "grade E"
	        else:
	            	  return "fail"
name , total , percentage , result=student_result("Ravi" , 78 , 67 , 23)
print("Name: " , name)
print("Total marks: " , total)
print("percentage: " , percentage)
print("Grade: " , grade(percentage))
print(result)	            	         	  	  	  