int main(int argc, char *argv[])
{
	char user_input[100];
	int *secret;
	int int_input;

	/* The secret value is stored on the heap */
	secret = (int *) malloc(7*sizeof(int));

	/* getting the secret */
	secret[0] = 0x46; secret[1] = 0x49; secret[2] = 0x54; secret[3] = 0x35; secret[4] = 0x30; secret[5] = 0x30; secret[6] = 0x33;
	

	printf("Please enter a string:\n");
	scanf("%s", user_input); /* getting a string from user */
	
	/* Vulnerable place */
	printf(user_input);
	printf("\n");

	printf("Please enter a decimal integer:\n");
	scanf("%d", &int_input); /* getting a decimal input from user */


	printf("Please enter another string:\n");
	scanf("%s", user_input); /* getting another string from user */
	
	/* Vulnerable place */
	printf(user_input);
	printf("\n");

	/* Verify whether your attack is successful */
	printf("The secret is: %s%s%s%s%s%s%s\n", &secret[0],&secret[1],&secret[2],&secret[3],&secret[4],&secret[5],&secret[6]);

	free(secret);	
	
	return 0;

}
