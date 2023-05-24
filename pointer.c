#include <stdio.h>

int main() {
    int num = 10;   // num = 10
    int* ptr = &num;  // id(num)

    printf("The value of the pointer is: %p\n", ptr);

    return 0;
}
