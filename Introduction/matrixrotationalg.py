
"""
inputMat, represents the matrix of N*M, where N is inputMat_row and M is inputMat_col.
"""
def funcRotate(inputMat):
    N = len(inputMat)
    M = len(inputMat[0])
    
    rotatedMat = [[0] * N for _ in range(M)]
    
    for i in range(N):
        for j in range(M):
            rotatedMat[j][N - 1 - i] = inputMat[i][j]
    
    return rotatedMat

def main():
    inputMat = []
    inputMat_rows, inputMat_cols = map(int, input().split())
    for idx in range(inputMat_rows):
        inputMat.append(list(map(int, input().split())))
    
    result = funcRotate(inputMat)
    
    for row in result:
        print(*row)

if __name__ == "__main__":
    main()

