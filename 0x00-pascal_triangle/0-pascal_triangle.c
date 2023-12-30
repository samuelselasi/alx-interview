#include <stdio.h>
#include <stdlib.h>

/**
 * print_triangle - prints triangle
 * @triangle: binomial coefficients
 * @n: number to generate coefficients
 *
 * Return: None
 */
void print_triangle(int** triangle, int n) {
    for (int i = 0; i < n; i++) {
        printf("[");
        for (int j = 0; j <= i; j++) {
            printf("%d", triangle[i][j]);
            if (j < i) {
                printf(",");
            }
        }
        printf("]\n");
    }
}


/**
 * pascal_triangle - creates pascal's triangle
 * @n: number to generate coefficients
 *
 * Return: binomial coefficients
 */
int** pascal_triangle(int n) {
    if (n <= 0) {
        return NULL;
    }

    int** triangle = (int**)malloc(n * sizeof(int*));

    for (int i = 0; i < n; i++) {
        triangle[i] = (int*)malloc((i + 1) * sizeof(int));
        triangle[i][0] = 1;

        for (int j = 1; j < i; j++) {
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }

        triangle[i][i] = 1;
    }

    return triangle;
}


/**
 * main - entry point
 *
 * Return: 0
 */
int main() {
    int n = 6;
    int** triangle;

    triangle = pascal_triangle(n);

    print_triangle(triangle, n);

    for (int i = 0; i < n; i++) {
        free(triangle[i]);
    }
    free(triangle);

    return 0;
}
