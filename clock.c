#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <unistd.h>
#include <time.h>


pthread_t arr[3]; 
pthread_mutex_t lock; 
int counter = 1;


void* clockthread(void* arg) {
        pthread_mutex_lock(&lock); 
        
        time_t s, val = 1; 
	struct tm* current_time; 

	s = time(NULL); 

	// to get current time 
	current_time = localtime(&s); 
        if(counter == 1) {
                printf("%02d:",current_time->tm_hour);
		counter++;
	}
	else if(counter == 2) {
	        printf("%02d:",current_time->tm_min);
		counter++;
	}
	else if(counter == 3) {
	        printf("%02d \n",current_time->tm_sec);
	}
	
	pthread_mutex_unlock(&lock); 
	
	return NULL; 
}

int main() {
        int i = 0;
        int error;
        
        printf("Implementing clock using threads: \n");
        
        if (pthread_mutex_init(&lock, NULL) != 0) { 
		printf("\n mutex init has failed\n"); 
		return 1; 
	} 
	
	while (i < 3) { 
		error = pthread_create(&(arr[i]), NULL, &clockthread, NULL); 
		if (error != 0) 
			printf("\nThread can't be created :[%s]", 
				strerror(error)); 
		i++; 
	} 

    pthread_join(arr[0], NULL); 
	pthread_join(arr[1], NULL); 
	pthread_join(arr[2], NULL); 
	
	pthread_mutex_destroy(&lock); 

	return 0; 
	
}
