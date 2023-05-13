#include <stdio.h>

#define INT_MAX 99999999
#define FLOAT_MAX 9999999.99

// 3-(a) 소스 코드
void chainedMatrixMultipulication(int arr[], int length){
    int matrix[length][length];
    int p[length][length];
    int min;
    for (int i = 1; i < length; i++) {
        matrix[i][i] = 0; // 대각선 0으로 초기화
        p[i][i] = 0;
    }
    for (int L = 2; L < length; L++) {
        for (int i = 1; i < length-L+1; i++) {
            int j = i + L - 1;
            matrix[i][j] = INT_MAX; // 임의의 큰 값으로 구하고자 하는 값 초기화
            
            for (int k = i; k < j; k++) {
                min = matrix[i][k] + matrix[k+1][j] + arr[i - 1] * arr[k] * arr[j]; //  opt(i, j) 계산
                if (min < matrix[i][j]){ 
                    matrix[i][j] = min;
                    p[i][j] = k;
                }
            }
        }
    }

    for (int i = 1; i < length; i++) {
        for (int j = 1; j < i; j++) {
            printf("  ");
        }
        for (int j = i; j < length; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }

    printf("\n");
    for (int i = 1; i < length; i++) {
        for (int j = 1; j < i; j++) {
            printf("  ");
        }
        for (int j = i; j < length; j++) {
            printf("%d ", p[i][j]);
        }
        printf("\n");
    }
}


// 5-(a) 소스코드
float sum(float arr[], int i, int j) {
    float sum = 0;
    for (int k = i; k < j + 1; k++) {
        sum += arr[k];
    }
    return sum;
}
void optimalBinarySearchTree(float arr[], int length) {
    float opt[length][length];
    int p[length][length];
    for (int i = 1; i < length; i++) {
        opt[i][i] = 1.00; // 대각선 1.00으로 초기화
        p[i][i] = i;
        for (int j = i + 1; j < length; j++) {
            opt[i][j] = 0;
            p[i][j] = -1;
        }
    }
    
    for (int L = 2; L < length; L++) {
        for (int i = 1; i < length-L+1; i++) {
            int j = i + L - 1;
            opt[i][j] = FLOAT_MAX;

            for (int k = i; k < j + 1; k++) {
                float cost = 1 + (sum(arr, i, k - 1) / sum(arr, i, j)) 
                        * opt[i][k - 1] + (sum(arr, k + 1, j) / sum(arr, i, j)) * opt[k + 1][j];
                if (cost < opt[i][j]) {
                    opt[i][j] = cost;
                    p[i][j] = k;
                }
            }
        }
    }

    for (int i = 1; i < length; i++) {
        for (int j = 1; j < i; j++) {
            printf("     ");
        }
        for (int j = i; j < length; j++) {
            printf("%.2f ", opt[i][j]);
        }
        printf("\n");
    }

    printf("\n");
    for (int i = 1; i < length; i++) {
        for (int j = 1; j < i; j++) {
            printf("  ");
        }
        for (int j = i; j < length; j++) {
            printf("%d ", p[i][j]);
        }
        printf("\n");
    }
}

// 실행
int main() {
    // int arr[] = {4,9,3,7,3,5};
    float arr[] = {0.0,0.08,0.12,0.05,0.15,0.2,0.05,0.05,0.1,0.1,0.1};
    int length = sizeof(arr) / sizeof(float);
    // chainedMatrixMultipulication(arr, length);
    optimalBinarySearchTree(arr, length);
}