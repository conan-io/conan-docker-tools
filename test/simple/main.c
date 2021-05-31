#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(void) {
    time_t rawtime;
    struct tm * timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);
    printf("Current local time and date: %s", asctime(timeinfo));

    return EXIT_SUCCESS;
}
