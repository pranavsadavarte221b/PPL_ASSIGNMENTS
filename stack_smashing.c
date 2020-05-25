#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int outer(void) {
        return 1;
}
int overflow(void) {
        int array[3];
        array[0] = 12;
        array[1] = 10;
        array[2] = 18;
        array[3] = 5;
        array[4] = 0x00005555;
        array[5] = 0x55555125;

        return 1;
}

int main() {
        int i;
        i = 14;
        overflow();
        
        return 0;
}
