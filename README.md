Game of Life - A Python program to implement Conway's Game of Life using a C library.

Description:
This project is an implementation of Conway's Game of Life in Python. The Game of Life is a cellular automaton developed by mathematician John Conway in 1970. The program uses a C library to determine the state of cells in the next generation, which speeds up calculations and improves performance.

Functionality:
- Read a matrix from a text file using the command line.
- Display the current state of the matrix using the characters "." and " ".
- Execute multiple generations (iterations) of the Game of Life using the C library.

Project Structure:
- read_file.py: Python script to read the matrix from a file and manage the Game of Life.
- count.c: C file containing functions for computing the next generation of the Game of Life.
- matrix.txt: A text file with an example matrix for testing the program.

How to Use:
1. Clone the repository to your computer using the git clone command.
2. Run read_file.py from the command line, passing the name of the matrix file and the number of changes you want to perform.
   Example: python read_file.py matrix.txt 5

I hope this project helps you understand the basics of the Game of Life and provides an opportunity to use different matrices for testing and enjoyment.
