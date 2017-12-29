#include <stdio.h>
#include <stdlib.h>

void print_string(const char *str) {
    printf(str);
    printf("\n");
}

int main(int argc, char **argv) {

    char *hello1 = "Hello 1";
    print_string(hello1);
    printf("First call.\n");
    char *hello2 = "Hello 2";
    print_string(hello2);
    printf("Secend call.\n");
    exit(0);

}