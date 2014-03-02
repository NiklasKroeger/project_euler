#!/usr/bin/python3
def readTriangle(path):
    triangle = []
    with open(path, "r") as input:
        for line in input:
            triangle.append(list(map(int, line.rstrip().split(" "))))
    return triangle

def calcMaxPath(triangle):
    levels = len(triangle)
    if levels == 1:
        return triangle[0][0]
    else:
        for i, val in enumerate(triangle[levels-2]):
            triangle[-2][i] += max(triangle[-1][i], triangle[-1][i+1])
#        for line in triangle:
#            print(line)
        return calcMaxPath(triangle[:-1])

def main():
    triangle = readTriangle("../files/problem067_file.txt")
    maxPathSum = calcMaxPath(triangle)
    print(maxPathSum)

if __name__=="__main__":
    main()
