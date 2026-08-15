def student_result(name , hindi , math , science):
	     total= hindi + math + science
	     percentage=total/300 *100
	     if hindi>=33 and  math>=33 and science>=33 :
	       	    result ="pas"
	     else:
	       	   result ="fail"    
	     if percentage>=90:
	    		  Grade= "Grade A" 
	     elif  percentage>=60:
	    		  Grade= "Grade B"
	     elif percentage>=45:
	    		  Grade="Grade C"
	     elif percentage>=33:
	    		  Grade= "Grade D"   
	     else:
	    		 Grade= "Fail"
	     return name , total , percentage , result , Grade
students=[
           ("Sumit" , 56 , 78 , 75),
           ("Ranu" ,75 , 46 , 86)
]  
for  student in students:
	name , total , percentage , result , Grade=student_result(*student)
	print("Name: " , name)   	
	print("Total: ", total)
	print("percentage: " , percentage)
	print("result: " , result)
	print("Grade: " , Grade)
	print("                  ")  	      	     	      