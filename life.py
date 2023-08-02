import ctypes
import sys


if len(sys.argv) < 3:
    print("Usage: python_file matrix.txt num_of_chages")
    sys.exit(1)

input_matrix = sys.argv[1]
num_of_changes = int(sys.argv[2])

try:
    with open (input_matrix, 'r') as file:
        map = file.read()
except File_not_found_error:
    print("File '{input_matrix}'not found")        
        

# sys.argv

c_count = ctypes.CDLL('./count.so')


'''def exam (map, y, x):
    if x < 0 or y < 0 or x >= cols or y >= rows:
        return 0
    return map[y*WIDTH+x]
        
    
def count (map, y, x):
    
    sum = 0
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if i >= 0 and j >= 0 and i < rows and j < cols:
                sum += exam(map, i, j)   
    return sum - map[y][x]
'''            

def print_matrix(map): 

    for i  in range(rows):
        for j in range(cols):
            if map[i * cols + j] == 0:
                print(".", end = '')
            else:
                print("0", end = '')    
        print() 

def point_life(map, y, x):
    num = c_count.count(map, y, x, cols, rows)
    if (num == 3 and map[y*cols+x] == 1) or (num == 2 and map[y*cols+x]):
        return 1
    elif map[y*cols+x] == 0 and num == 3 :
        return 1
    return 0;
    
            

def new_generation(map):
    #new_map = []
    #for i in range(rows):
        #subarray = []
        #for j in range(cols):
            #subarray.append(0)
            
        #new_map.append(subarray)
    new_map = (ctypes.c_int * (rows * cols))()
    
        
    for y in range (rows):
        for x in range (cols):            
            new_map[y*cols+x] = (point_life(map, y, x))  
              
    return new_map  


    
    
def converting(num_of_changes, map):
    for i in range(num_of_changes):
        map = new_generation(map) 
        print_matrix(map)   

      
def transform(map):
    c_array = (ctypes.c_int * (rows * cols))()
    for i in range(rows):
        for j in range(cols):
            c_array[i*cols+j] = map[i][j] 
    return c_array        


def read_matrix(file_matrix):        
    matrix_py = []
    with open(file_matrix, 'r') as file:
        lines = file.readlines()
        line_length = len(lines[0].strip())
        valid_char = {'0', '1'}
        for line in lines:
            #print(repr(line))
            after_line = line.strip()
            if len(after_line) != line_length:
                print("Matrix rows have different lengths") 
                exit()
            if not all(char in valid_char for char in after_line):  
                print("Other symbols")
                exit() 
            row = [int(x) for x in after_line]
            matrix_py.append(row)
    return matrix_py                       

file_path = "matrix.txt"
matrix_py = read_matrix(file_path)
rows = len(matrix_py)
cols = len(matrix_py[0])
converting(num_of_changes, transform(matrix_py))




   
            
                
