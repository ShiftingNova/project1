#Jordan_Walker
#CSC110
#The program prints hollow triangles and squares of different sizes
def hollow_row(char, N):
    #will make the hollow lines in the square. Char is the specific character
    # N is the size of the sqaure
    if N > 1:
        return_value = char + " " * (N - 2) + char

    else:
        return_value = char
    return return_value


def hollow_square(char, N):
    #Will create the hollow sqaure. Char is the specific charater
    #N is the size of the sqaure
    for i in range(N):
        if i > 0 and i < N - 1:
            print(hollow_row(char, N))
        else:
            print(char * N)


def hollow_triangle(char, N):
    #will create the hollow triangle. Char is the specfic character it will be using
    #N is the size of the triangle
    for i in range(N + 1):
        if i > 2 and i < N:
            print(char + " " * (i - 2) + char)
        elif i>0:
            print(char * i)
hollow_square("@", 1)
hollow_square("#", 2)
hollow_square("*", 5)
hollow_triangle("@", 1)
hollow_triangle("#", 2)
hollow_triangle("*", 5)
