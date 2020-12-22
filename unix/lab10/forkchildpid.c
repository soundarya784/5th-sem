#include<stdio.h>
#include<sys/types.h>
#include<stdlib.h>
#include<unistd.h>

int main(void)
{

	int pid;
	printf("before fork");
	pid = fork();
	
	if(pid>0){
	
		sleep(3);
		printf("Parent --PID: %d \nPPID :%d,\n CHILD PID:%d",getpid(),getppid(),pid);
		}

	else if(pid == 0)
	{
		printf("child --PID: %d \nPPID :%d",getpid(),getppid());
	}
		
	else
	{
		printf("Fork error");
		exit(1);
	}
	printf("Both processes continue from here");
	exit(0);
}














