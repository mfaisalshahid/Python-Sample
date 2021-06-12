def rotate(matrix):
    n = len(matrix[0]);
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i] , matrix[i][j];    
    for i in range(n):
        matrix[i].reverse();

O(M)
O(1)
