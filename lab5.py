import numpy as np

def matrix_addition(mat1, mat2):
    return np.add(mat1, mat2)
def matrix_subtraction(mat1, mat2):
    return np.subtract(mat1, mat2)
def scalar_matrix_multiplication(mat1, scalar):
    return np.multiply(mat1, scalar)
def elementwise_matrix_multiplication(mat1, mat2):
    return np.multiply(mat1, mat2)
def  matrix_multiplication(mat1, mat2):
    return np.dot(mat1, mat2)
def matrix_transpose(mat1):
    return np.transpose(mat1)
def trace_of_matrix(mat1):
    return np.trace(mat1)
def solve_system_of_linear_equations(mat1, mat2):
    return np.linalg.solve(mat1, mat2)
def determinant(mat1):
    return np.linalg.det(mat1)
def inverse(mat1):
    return np.linalg.inv(mat1)
def eigen_value(mat1):
    return np.linalg.eig(mat1)
def search(mat1,ele):
    b=np.where(mat1==ele,1,0)
    return b
def difference(mat1):
    return np.sum(np.triu(mat1))-np.sum(np.tril(mat1))

if __name__ == "__main__":
    
    
    rows1=int(input("Enter the number of rows: "))
    columns1=int(input("Enter the number of columns: "))
    mat1=np.empty((rows1,columns1))
    for i in range(rows1):
        for j in range(columns1):
            print("Enter the element at position ",i,j)
            mat1[i][j]=int(input())
            
            
    rows2=int(input("Enter the number of rows: "))
    columns2=int(input("Enter the number of columns: "))
    mat2=np.empty((rows2,columns2))
    
    for i in range(rows2):
        for j in range(columns2):
            print("Enter the element at position ",i,j)
            mat2[i][j]=int(input())
            
           
    mat1=np.array(mat1)
    mat2=np.array(mat2)
    c=True
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Scalar Matrix Multiplication")
    print("4. Elementwise Matrix Multiplication")
    print("5. Matrix Multiplication")
    print("6. Matrix Transpose")
    print("7. Trace of a Matrix")
    print("8. Solve System of Linear Equations")
    print("9. Determinant")
    print("10. Inverse")
    print("11.singular value decomposition")
    print("12. Eigen Value")
    print("13.search an element")
    print("14.difference of sum of upper and lower triangular matrices")
    print("15. Exit")
    
    while c:
        
        option=int(input("Enter your choice: "))
        if (option==1):
            if (rows1!=rows2 or columns1!=columns2):
                print("Matrix addition is not possible")
                continue
            else:
                mat3= matrix_addition(mat1,mat2)
                print(mat3)
        elif (option==2):
            if (rows1!=rows2 or columns1!=columns2):
                print("Matrix subtraction is not possible")
                continue
            else:
                mat3= matrix_subtraction(mat1,mat2)
                print(mat3)
        elif (option==3):
            value=int(input("Enter the scalar value for matrix1: "))
            mat3= scalar_matrix_multiplication(mat1,value)
            print(mat3)
            value=int(input("Enter the scalar value for matrix1: "))
            mat3= scalar_matrix_multiplication(mat2,value)
            print(mat3)
            
        elif (option==4):
            if (rows1!=rows2 or columns1!=columns2):
                print("Elementwise matrix multiplication is not possible")
                continue
            else:
                mat3= elementwise_matrix_multiplication(mat1,mat2)
                print(mat3)
        elif (option==5):
            if (columns1!=rows2):
                print("Matrix multiplication is not possible")
                continue
            else:
                mat3= matrix_multiplication(mat1,mat2)
                print(mat3)
        elif (option==6):
            print("transpose of matrix1=")
            mat3= matrix_transpose(mat1)
            print(mat3)
            print("transpose of matrix2=")
            mat3= matrix_transpose(mat2)
            print(mat3)
            
        elif (option==7):
            if(columns1!=rows1):
                print("trace not possible for matrix1")
            else:
                print("trace of matrx1=",trace_of_matrix(mat1))
            if(columns2!=rows2):
                print("trace not possible for matrix1")
            else:
                print("trace of matrx2=",trace_of_matrix(mat2))
                
                
        
        elif (option==8):
            rows_1=int(input("Enter the number of rows: "))
            columns_1=int(input("Enter the number of columns: "))
            mat_1=np.zeros((rows_1,columns_1))
            for i in range(rows_1):
                for j in range(columns_1):
                    print("Enter the element at position ",i,j)
                    mat_1[i][j]=int(input())
            
            
            rows_2=int(input("Enter the number of rows: "))
            columns_2=int(input("Enter the number of columns: "))
            mat_2=np.zeros((rows_2,columns_2))
            for i in range(rows_2):
                 for j in range(columns_2):
                    print("Enter the element at position ",i,j)
                    mat_2[i][j]=int(input())
            
            mat_1=np.array(mat_1)
            mat_2=np.array(mat_2)
            if(rows_2!=rows_1 or columns_2!=1):
                print("System of linear equations cannot be solved")
                continue
            else:
                mat3= solve_system_of_linear_equations(mat_1,mat_2)
                print(mat3)
        elif (option==9):
            if(rows1!=columns1):
                print("determinant cannot be calculated to matrix1")
            else:
                print("determinant of matrix1=",int(determinant(mat1)))
            if(rows2!=columns2):
                print("determinant cannot be calculated to matrix1")
            else:
                print("determinant of matrix2=",int(determinant(mat2)))
           
        elif (option==10):
            if(columns1!=rows1 or determinant(mat1)==0):
                print("Inverse of the matrix1 does not exist")
            else:
                mat3= inverse(mat1)
                print("inverse of matrix1")
                print(mat3)
                
            if(columns2!=rows2 or determinant(mat2)==0):
                print("Inverse of the matrix1 does not exist")
            else:
                print("inverse of matrix2")
                print(inverse(mat2))
            
        elif(option==11):
            if(columns1!=rows1 or determinant(mat1)==0):
                print("singular_value_decomposition does not exist for matrix1")
            else:
                print("matrix1=")
                u,s,v=np.linalg.svd(mat1)
                print("U:",u,sep="\n")
                print("S:",s,sep="\n")
                print("V:",v,sep="\n")
            if(columns2!=rows2 or determinant(mat2)==0):
                print("singular_value_decomposition does not exist for matrix2")
            else:    
                print("matrix2=")
                u,s,v=np.linalg.svd(mat1)
                print("U:",u,sep="\n")
                print("S:",s,sep="\n")
                print("V:",v,sep="\n")
                
                
        
        elif (option==12):
            if(rows1!=columns1):
                print("eigen matrix cannot be calculated to matrix1")
            else:
                print("eigen values of matrix1")
                mat3,mat4= eigen_value(mat1)
                print(mat3)
            if(rows2!=columns2):
                print("eigen matrix  cannot be calculated to matrix2")
            else:
                print("eigen values of matrix2")
                mat3,mat4= eigen_value(mat2)
                print(mat3)
            
           
            
        elif(option==13):
            b=int(input("enter the element to be searched in matrix1:"))
            if(np.count_nonzero(search(mat1,b))):
                print(" element {} found".format(b))
            else:
                print(" element {} not found".format(b))
            
            
            c=int(input("enter the element to be searched in matrix2:"))    
            if(np.count_nonzero(search(mat2,c))):
                print(" element {} found".format(c))
            else:
                print(" element {} not found".format(c))
                
                
        elif(option==14):
            if(rows1!=columns1):
                print("difference of sum of upper and lower triangular matrices cannot be calculated to matrix1")
            else:
                print("matrix1=")
                print(difference(mat1))
            if(rows2!=columns2):
                print("difference of sum of upper and lower triangular matrices cannot be calculated to matrix2")
            else:
                print("matrix2=")
                print(difference(mat2))
                
            
        elif (option==15):
            c=False
            exit()    
        else:
             print("Invalid option")