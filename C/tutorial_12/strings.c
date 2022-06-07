#include <stdio.h>
#include <string.h>
int main(){
    char greeting[] = "Hello";
    //char greeting[6] = {'H', 'e','l','l','o'};
    int num_words = 2;
    int num_char = 6;
    char sentance[num_words][num_char];
    strlcpy(sentance[0],"Hello",num_char);
    strlcpy(sentance[1],"World",num_char);
    for(int i = 0; i < num_words; i++){
        for(int j = 0; j < num_char; j++){
            printf("%c",sentance[i][j]);
        }
        printf("\n");
    }
    char world[50] = "World";
    char hello_world[50] = "Hello ";
    strcat(hello_world,world);
    printf("The result is %s\n",hello_world);
    printf("The length of the string is: %lu\n",strlen(hello_world));
    return 0;
}