#include <stdio.h>
#include "foo.h"
int main() {
    int x = bar();
    //int x = 8;
    printf("Hello, World = '%d'\n", x);
    return 0;
}
