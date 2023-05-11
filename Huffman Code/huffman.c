#include <stdio.h>

#define ASCII 128

void init(int count[], int *total) {
    int ascii;

    while ((ascii = getchar()) != EOF) {
        if (ascii < ASCII){
            count[ascii]++;
            (*total)++;
        }
    }
}

void bubbleSort(int count[]) {
    for (int i = 0; i < ASCII; i++) {
        for (int j = 0; j < ASCII-i-1; j++) {
            if (count[j] < count[j+1]) {
                int temp = count[j];
                count[j] = count[j+1];
                count[j+1] = temp;
            }
        }
    }
}

void huffman(int count[], int total){
    int sum = 0;
    int huff_arr[ASCII] = {0};
    int count_r, huff_l = 0, huff_r = 1;

    for (count_r = 0; count[count_r]; count_r++) {}
    huff_arr[0] = count[count_r-1] + count[count_r-2];
    count_r = count_r - 3;
    for (; count_r > -1;) {
        int temp;
        if (count[count_r] <= huff_arr[huff_l]){
            temp = count[count_r--];
            if (count_r > -1 && count[count_r] <= huff_arr[huff_l]) {
                huff_arr[huff_r++] = temp + count[count_r--];
                sum += huff_arr[huff_r-1];
            } else {
                huff_arr[huff_r++] = temp + huff_arr[huff_l++];
                sum += huff_arr[huff_r-1];
            }
        }
        else {
            temp = huff_arr[huff_l++];
            if (count[count_r] <= huff_arr[huff_l] || !(huff_r - huff_l)) {
                huff_arr[huff_r++] = temp + count[count_r--];
                sum += huff_arr[huff_r-1];
            } else {
                huff_arr[huff_r++] = temp + huff_arr[huff_l++];
                sum += huff_arr[huff_r-1];
            }
        }
    }

    for (; (huff_r - huff_l) > 1;) {
        huff_arr[huff_r++] = huff_arr[huff_l] + huff_arr[huff_l + 1];
        sum+= huff_arr[huff_r-1];
        huff_l = huff_l + 2;
    }

    printf("answer : %f\n", (float) 2 * sum/(8 * total));
    printf("sum : %d", sum / 8);
}

int main() {
    int count[ASCII] = {0};
    int total = 0;

    init(count, &total);
    bubbleSort(count);
    huffman(count, total);

    return 0;
}