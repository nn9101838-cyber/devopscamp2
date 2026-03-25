#include <stdio.h>

int main() {
    char name[100];
    printf("Welcome to DevOps C App\n");
    printf("Enter your name: ");
    scanf("%99s", name);
    printf("Hello, %s!\n", name);
    return 0;
}
