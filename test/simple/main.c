#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#include <pthread.h>

void* show_date(void* data) {
    time_t rawtime;
    struct tm * timeinfo;
    time(&rawtime);
    timeinfo = localtime(&rawtime);
    printf("Current local time and date: %s", asctime(timeinfo));
    return 0;
}

int main(void) {
    int result;
    pthread_t worker;

    result = pthread_create(&worker, NULL, show_date, NULL);
    if (result) {
        perror("Could not create thread");
        return EXIT_FAILURE;
    }
    pthread_join(worker, NULL);
    return EXIT_SUCCESS;
}
