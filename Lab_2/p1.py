def print_list(lst):
	for val in lst:
		print(val, end=" ")
	print("")

def print_matrix(M):
	for row in M:
		for val in row:
			print(val, end=" ")
		print("")

def flatten_list(A):
	rows = len(A)
	cols = len(A[0])
	ans = []

	for i in range(rows):
		for j in range(cols):
				ans.append(A[i][j])
	return ans

def multiply(A,B):
	rows_A = len(A)
	rows_B = len(B)
	cols_A = len(A[0])
	cols_B = len(B[0])
	if(cols_A!=rows_B):
		print("Can't multiply!")
		return None
	else:
		ans = []
		for i in range(rows_A):
			new_row = []
			for j in range(cols_B):
				sum = 0
				for k in range(cols_A):
					sum+=A[i][k]*B[k][j]
				new_row.append(sum)
			ans.append(new_row)
		return ans

def is_symmetric(M):
	rows = len(M)
	cols = len(M[0])
	if(rows!=cols):
		return False
	else:
		T = transpose(M)
		flag = True
		for i in range(rows):
			for j in range(cols):
				if(M[i][j]!=T[i][j]):
					flag = False
					break
		if(flag): 
			return True
		else: 
			return False
			
def transpose(M):
	rows = len(M)
	cols = len(M[0])

	T = []
	for j in range(cols):
		new_row = []
		for i in range(rows):
			new_row.append(M[i][j])
		T.append(new_row)
	return T
		
def dimension(M):
	rows = len(M)
	cols = len(M[0])
	print(f"rows = {rows} , cols = {cols}")

A = [[1,2,3],[4,5,6],[7,8,9]]
dimension(A)
A_transpose = transpose(A)
print_matrix(A_transpose)
if(is_symmetric(A)):
	print("A is Symmetric")
else:
	print("A is not Symmetric")
prod = multiply(A,A_transpose)
print_matrix(prod)
if(is_symmetric(prod)):
	print("A.A^t is Symmetric")
else:
	print("A.A^t is not Symmetric")

flat_list = flatten_list(A)
print_list(flat_list)