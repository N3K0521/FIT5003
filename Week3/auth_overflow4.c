#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int check_authentication(char *password, unsigned int bytes) {

	unsigned char password_buffer[96];
	int auth_flag[1];
	auth_flag[0] = 0;	

	memcpy(password_buffer, password, bytes);
	
	if(strcmp(password_buffer, "brillig") == 0)
		auth_flag[0] = 1;
	if(strcmp(password_buffer, "outgrabe") == 0)
		auth_flag[0] = 1;

	return auth_flag[0];
}

int main(int argc, unsigned char *argv[]) {
	if(argc < 3) {
		printf("Usage: %s <bytes> <password>\n", argv[0]);
		exit(0);
	}
	printf("Usage: %s\n",argv[2]);
	if(check_authentication( argv[2], atoi(argv[1]))) {
		printf("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-\n");
		printf("      Access Granted.\n");
		printf("-=-=-=-=-=-=-=-=-=-=-=-=-=-\n");
	} else {
		printf("\nAccess Denied.\n");
   }
}
	