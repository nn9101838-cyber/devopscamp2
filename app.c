#include <stdio.h>

int main() {
    char name[100];
    int num1, num2;
    int choice;
    printf("Welcome to DevOps C App\n");
    printf("Enter your name: ");
    scanf("%99s", name);

    printf("Menu:\n1. Greet User\n2. Add Two Numbers\nChoice: ");
    scanf("%d", &choice);
    if (choice == 1) {
        printf("Hello, %s!\n", name);
    } else if (choice == 2) {
        printf("Enter two integers to add: ");
        scanf("%d %d", &num1, &num2);
        printf("Sum: %d\n", num1 + num2);
    } else {
        printf("Invalid choice.\n");
    }

    return 0;
}
