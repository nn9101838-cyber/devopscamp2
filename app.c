#include <stdio.h>

int main() {
    char name[100];
    int num1, num2;
    printf("Welcome to DevOps C App\n");
    printf("Enter your name: ");
    scanf("%99s", name);
    printf("Hello, %s!\n", name);

    printf("Enter two integers to add: ");
    scanf("%d %d", &num1, &num2);
    printf("Sum: %d\n", num1 + num2);

    return 0;
}
