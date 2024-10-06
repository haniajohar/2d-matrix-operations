import time
#main 
if __name__ == "__main__":
    print("Hello everyone")
    #timer to delay printing
    time.sleep(1)
    print("today we are going to perform different operation on matrices")
    print("a matrix is basically a rectangular array of rows and columns")
    time.sleep(1)
    print("Now")
    
    #loop to perform different functions
    while True:
      
      print("which function do you want to perform")
     
      value=int(input("press 1 for addition\npress 2 for subtraction\npress 3 for multiplication\npress 4 for transpose\n press 5 for scaler multiplication\n" ))
        #match case to perform any 1 function from the list
      match value:
          case 1:
              #addition of matrices
              print("Addition")
              a=int(input("enter the number of rows for matrix1 ",))
              b=int(input("enter the number of column for matrix1 ",))
              matrix1=[]
              print("input numbers for the matrix1")
              for i in range(a):
                 row=[]
                 for j in range(b):
                   c=int(input(f"enter number for row {i+1} and column {j+1}"))
                   row.append(c)
                 matrix1.append(row)   
               
              print("The matrix1 is:")
              for row in matrix1:
                   for elem in row:
                       print(elem, end=" ")
                   print()        
                    
           
              a1=int(input("enter the number of rows for matrix2 ",))
              b1=int(input("enter the number of column for matrix2 ",))
              matrix2=[]
              print("input numbers for the matrix2")
              for i in range(a1):
                 row2=[]
                 for j in range(b1):
                   c1=int(input(f"enter number for row {i+1} and column {j+1}"))
                   row2.append(c1)
                 matrix2.append(row2)   
               
              print("The matrix2 is:")
              for row2 in matrix2:
                   for elem in row2:
                       print(elem, end=" ")
                   print()  
           
  
              
              if((a==a1)and(b==b1)):
                      
                      result=[]
                      for k in range(a):  
                       row3 = []
                       for l in range(b):  
                            #logic for addition
                            row3.append(matrix1[k][l] + matrix2[k][l])  
                       result.append(row3)
                      print("sum of the matrix1 and matrix2 :")
                      for row3 in result:
                          for elements in row3:
                              print(elements,end=" ")
                          print()
              else:
                  print("sorry this case is not possible ") 
                  continue
             
                                   
                              
          case 2:
              #subraction of two matrices
              print("Subtraction")
              a=int(input("enter the number of rows for matrix1 ",))
              b=int(input("enter the number of column for matrix1 ",))
              matrix1=[]
              print("input numbers for the matrix1")
              for i in range(a):
                 row=[]
                 for j in range(b):
                   c=int(input(f"enter number for row {i+1} and column {j+1}"))
                   row.append(c)
                 matrix1.append(row)   
               
              print("The matrix1 is:")
              for row in matrix1:
                   for elem in row:
                       print(elem, end=" ")
                   print()        
                    
           
              a1=int(input("enter the number of rows for matrix2 ",))
              b1=int(input("enter the number of column for matrix2 ",))
              matrix2=[]
              print("input numbers for the matrix2")
              for i in range(a1):
                 row2=[]
                 for j in range(b1):
                   c1=int(input(f"enter number for row {i+1} and column {j+1}"))
                   row2.append(c1)
                 matrix2.append(row2)   
               
              print("The matrix2 is:")
              for row2 in matrix2:
                   for elem in row2:
                       print(elem, end=" ")
                   print()  
           
  
              
              if((a==a1)and(b==b1)):
                      
                      result=[]
                      for k in range(a):  
                       row3 = []
                       for l in range(b): 
                            #logic for subtraction 
                            row3.append(matrix1[k][l] - matrix2[k][l])  
                       result.append(row3)
                      print("difference of the matrix1 and matrix2 :")
                      for row3 in result:
                          for elements in row3:
                              print(elements,end=" ")
                          print()
              else:
                  print("sorry this case is not possible") 
                  continue
                 
          case 3:
              print("Multiplication")
              #mutiplication of two matrices
              a=int(input("enter the number of rows for matrix1 ",))
              b=int(input("enter the number of column for matrix1 ",))
              matrix1=[]
              print("input numbers for the matrix1")
              for i in range(a):
                 row=[]
                 for j in range(b):
                   c=int(input(f"enter number for row {i+1} and column {j+1}"))
                   row.append(c)
                 matrix1.append(row)   
               
              print("The matrix1 is:")
              for row in matrix1:
                   for elem in row:
                       print(elem, end=" ")
                   print()        
                    
           
              a1=int(input("enter the number of rows for matrix2 ",))
              b1=int(input("enter the number of column for matrix2 ",))
              matrix2=[]
              print("input numbers for the matrix2")
              for i in range(a1):
                 row2=[]
                 for j in range(b1):
                   c1=int(input(f"enter number for row {i+1} and column {j+1}"))
                   row2.append(c1)
                 matrix2.append(row2)   
               
              print("The matrix2 is:")
              for row2 in matrix2:
                   for elem in row2:
                       print(elem, end=" ")
                   print()  
           
              if(a==b1):
                      c1=a
                      
                      result=[]
                      #logic to mutiply to matrices
                      for k in range(a):  
                       row3 = []
                       for l in range(b): 
                            c=0
                            for n in range(c1):
                                c+=(matrix1[n][l]*matrix2[k][n])
                            row3.append(c)  
                       result.append(row3)
                      print("product of the matrix1 and matrix2 :") 
                      for row3 in result:
                          for elements in row3:
                              print(elements,end=" ")
                          print()
              else:
                  print("sorry this case is not possible") 
                  continue
               
                  
  
  
              
          case 4:
              print("transpose")
              #transpose (conversion of rows into columns) of a matrix
              a=int(input("enter the number of rows for matrix ",))
              b=int(input("enter the number of column for matrix ",))
              matrix=[]
              print("input numbers for the matrix1")
              for i in range(a):
                 row=[]
                 for j in range(b):
                   c=int(input(f"enter number for row {i+1} and column {j+1}"))
                   row.append(c)
                 matrix.append(row)   
               
              print("The matrix is:")
              for row in matrix:
                   for elem in row:
                       print(elem, end=" ")
                   print()          
              if(a==b):
                         result=[]
                         #logic to take transpose of a matrix
                         for i in range(a):
                           row=[]
                           for j in range(b):
                             c=matrix[j][i]
                             row.append(c)
                           result.append(row)   
      
                         print("The transpose of matrix is:")
                         for row in result:
                              for elem in row:
                                  print(elem, end=" ")
                              print() 
              else:
                     print("error*** wrong input found")
                     print("try again")
                     continue
              
                     
                 
          
          case 5:
              print("Scalar Multiplication")
              print("- Scalar Multiplication is a multiplication that allows user to multiply a matrix by a scalar (a single number).\n Each element of the matrix is multiplied by this scalar.")
              a=int(input("enter the number of rows for matrix "))
              b=int(input("enter the number of column for matrix "))
              matrix=[]
              print("input numbers for the matrix")
              for i in range(a):
                 row=[]
                 for j in range(b):
                   c=int(input(f"enter number for row {i+1} and column {j+1}"))
                   row.append(c)
                 matrix.append(row)   
               
              print("The matrix is:")
              for row in matrix:
                   for elem in row:
                       print(elem, end=" ")
                   print()
              scalar=int(input("enter the scaler you want to multiple with the matrix"))
              result=[]
              #logic to do scalar multiplication of a matrix
              for i in range(a):
                row=[]
                for j in range(b):
                  c=(scalar*matrix[i][j])
                  row.append(c)
                result.append(row)     
              print("The scalar multiplication result of this matrix is:")
              for row in result:
                   for elem in row:
                       print(elem, end=" ")
                   print("")  
      print("Do you want to perform functions again")
      choice=input("press y/Y for yes ")
      if(choice=='y' or choice=='Y'):
          continue
      else:
          break
  
                 
  