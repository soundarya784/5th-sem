#include<stdio.h> //for I/O to console
#include<stdlib.h> // To include Standard Library functions such as printf
#include<fcntl.h> //To close and open files(file control)
#include<errno.h> //To read error numbers returned from system calls to Stdlib functions
#include<sys/types.h> //didnt understand what this is , i think it translates os specific env variables? no clue
#include<unistd.h> //gives access to POSIX APIs v1 , such as read(),write()

#define BUF_SIZE 8192

int main(int argc ,char* argv[])
{
	int input_fd,output_fd;
	ssize_t ret_in , ret_out; //number of bytes returned by read() and write()  (number of bytes of an object in memory)
	char buffer[BUF_SIZE];

	//to check if wrong usage of program:
	if(argc < 3 || argc > 3)
	{
		printf("Usage: pgm file1 file2");
		return 1;
	}

	//creating input FD
	input_fd=open(argv[1],O_RDONLY);
	if (input_fd == -1)
	{
		perror("open"); //automatically prints the error according to errno ,that's why we used #include<errno.h>
		return 2;
	}

	output_fd=open(argv[2],O_WRONLY | O_CREAT ,0664);
	if (output_fd == -1)
	{
		perror("open");
		return 3;
	}

	//Copying

	while((ret_in = read(input_fd,&buffer,BUF_SIZE)) > 0)
	{
		ret_out = write(output_fd,&buffer , (ssize_t) ret_in);
		if(ret_out != ret_in)
			{//write error
				perror("Write");
				return 4;
			}
	}

	close(input_fd);
	close(output_fd);

	return(EXIT_SUCCESS);



}
