#include <stdio.h>
int main(){
    int i = 1;

    do {
        printf("%d\n", i);
        i++;
    }
    while(i <= 0);
    printf("We are finished with the loop\n");
    return 0;
}