#include <stdio.h>

extern char* digest(char* str);

extern void pre_digest() {
    printf("pre_digest called\n");
}

int main() {
    char* result = digest("Hello World");
    printf("SHA digest of \'Hello World\': %s\n", result);
    return 0;
}