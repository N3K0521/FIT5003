import java.util.UUID;

public class APIConnection {

	private String token;

	public APIConnection() {

		// Assume the token is obtained via a secure service
		token =  UUID.randomUUID().toString();

	}

	/**
	 * A public method that requires authentication first.
	 * @param tokenGuess
	 */
	public void doSomething(String tokenGuess) {
		if (token.equals(tokenGuess)) {
			doSomethingSecret();
		} else {
			System.out.println("Invalid Token");
		}
	}

	/**
	 * This method is supposed to be protected, but using reflection, it can be directly invoked.
	 */
	private void doSomethingSecret() {
		System.out.println("You are authenticated! Now let's do some sensitive stuff.");
	}
}