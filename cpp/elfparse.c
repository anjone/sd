/* */
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <elf.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <stdint.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char **argv) {
    int fd, i;
    uint8_t *mem;
    struct stat st;
    char *StringTable, *interp;
    
    Elf32_Ehdr *ehdr;
    Elf32_Phdr *phdr;
    Elf32_Shdr *shdr;

    if(argc < 2) {
        printf('Usage: %s <executable>\n', argv[0]);
        exit(0);
    }

    if( (fd = open(argv[1], O_RDONLY)) < 0 ) {
        perror('open');
        exit(-1);
    }
}