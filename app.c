#include <stdio.h>

int main() {
    char name[100];
    int choice;
    printf("Welcome to DevOps C App\n");
    printf("Enter your name: ");
    scanf("%99s", name);
    printf("Hello, %s!\n", name);

    printf("Menu:\n1. Greet User\n2. Add Two Numbers\nChoice: ");
    scanf("%d", &choice);
    if (choice == 1) {
        printf("You chose to be greeted again. Hello!\n");
    } else if (choice == 2) {
        printf("Addition feature coming soon!\n");
    } else {
        printf("Invalid choice.\n");
    }

    return 0;
}
