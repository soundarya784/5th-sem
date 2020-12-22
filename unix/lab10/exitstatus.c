#include<stdio.h>
#include<sys/wait.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>


int main(void)
{

	int exitstatus;
	int exitval = 10;
	pid_t pid;
	
	pid = fork();
	if(pid == 0)
	{
		printf("in child process ....\n");
		printf("CHILD : trminating with exit status with exit value %d\n",exitval);
		exit(exitval);
	}
		
	else
	{
		wait(&exitstatus);
		printf("In parent proces.....");
		printf("Parent child terminated with exit value %d\n",WEXITSTATUS(exitstatus));
		exit(20);
	}
	printf("Both processes continue from here\n\n");
	exit(0);
}














