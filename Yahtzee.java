import javax.swing.JOptionPane;

/**
 * 
 */

/**
 * @author Amit Singh Mehmi
 * Date: March 12th, 2022
 * Description: This program will execute the game of Yahtzee 
 *
 */
public class Yahtzee {

	/**
	 * @param args
	 */
	public static void main(String[] args) {


		// Declaring variables
		int userMoney, continuation, intialMoney;
		
		// Declaring and intializing lists
		int dieCount[]; 
		dieCount = new int [6];
		int dieValues[];
		dieValues = new int [5];

		// Welcome message
		JOptionPane.showMessageDialog(null, "Welcome to the game of Yahtzee!", "YAHTZEE!", JOptionPane.INFORMATION_MESSAGE);

		// Asking for user's betting amount
		userMoney = Integer.parseInt(JOptionPane.showInputDialog(null, "Please enter betting amount to start (>=$10): ", "BETTING AMOUNT", JOptionPane.INFORMATION_MESSAGE));

		// Loop until user enters a bet greater than or equal to $10
		while (userMoney < 10) {
			userMoney = Integer.parseInt(JOptionPane.showInputDialog(null, "Betting amount must be >= $10 to start: ", "BETTING AMOUNT", JOptionPane.INFORMATION_MESSAGE));
		}
		
		// Storing user's initial money amount and taking away 10 for starting the game
		intialMoney = userMoney;
		userMoney = userMoney - 10;
		

		// Looping until user runs out of money or does not want to continue
		while (userMoney >= 0) {

			// Declaring variables 
			int numOnes=0, numTwos=0, numThrees=0, numFours=0, numFives=0, numSixes=0;
			String result = null;

			// Random dice roll
			for (int i = 0 ; i < 5 ; i++) {
				dieValues[i] = (int) (Math.random() * 6 + 1);
			}

			// Counting number of occurrances  
			for (int i = 0 ; i < 5 ; i++) {
				if (dieValues[i] == 1) {
					numOnes++;
				}
				else if (dieValues[i] == 2) {
					numTwos++;
				}
				else if (dieValues[i] == 3) {
					numThrees++;
				}
				else if (dieValues[i] == 4) {
					numFours++;
				}
				else if (dieValues[i] == 5) {
					numFives++;
				}
				else {
					numSixes++;
				}
			}

			// Putting Occurances into an array 
			dieCount[0] = numOnes;
			dieCount[1] = numTwos;
			dieCount[2] = numThrees;
			dieCount[3] = numFours;
			dieCount[4] = numFives;
			dieCount[5] = numSixes;

			// Deciding if user won Yahtzee, three straight, full house etc. 

			// Yahtzee
			for (int x = 0 ; x < 6 ; x++) {
				if (dieCount[x] == 5) {
					result = "YAHTZEE!";
					userMoney = userMoney + 1000;
				}
			}

			// Large straight 
			if (dieCount[0] == 1 && dieCount[1] == 1 && dieCount[2] == 1 && dieCount[3] == 1 && dieCount[4] == 1 && dieCount[5] == 0 || 
					dieCount[0] == 0 && dieCount[1] == 1 && dieCount[2] == 1 && dieCount[3] == 1 && dieCount[4] == 1 && dieCount[5] == 1) {
				result = "LARGE STRAIGHT";
				userMoney = userMoney + 500;
			}

			// Small straight 
			else if (dieCount[0] == 2 && dieCount[1] == 1 && dieCount[2] == 1 && dieCount[3] == 1 && dieCount[4] == 0 && dieCount[5] == 0||	// If number is 12341
					dieCount[0] == 1 && dieCount[1] == 2 && dieCount[2] == 1 && dieCount[3] == 1 && dieCount[4] == 0 && dieCount[5] == 0||	// 12342
					dieCount[0] == 1 && dieCount[1] == 1 && dieCount[2] == 2 && dieCount[3] == 1 && dieCount[4] == 0 && dieCount[5] == 0||	// 12343
					dieCount[0] == 1 && dieCount[1] == 1 && dieCount[2] == 1 && dieCount[3] == 2 && dieCount[4] == 0 && dieCount[5] == 0||	// 12344
					dieCount[0] == 1 && dieCount[1] == 1 && dieCount[2] == 1 && dieCount[3] == 1 && dieCount[4] == 0 && dieCount[5] == 1||	// 12346
					dieCount[0] == 0 && dieCount[1] == 2 && dieCount[2] == 1 && dieCount[3] == 1 && dieCount[4] == 1 && dieCount[5] == 0||	// 23452
					dieCount[0] == 0 && dieCount[1] == 1 && dieCount[2] == 2 && dieCount[3] == 1 && dieCount[4] == 1 && dieCount[5] == 0||	// 23453
					dieCount[0] == 0 && dieCount[1] == 1 && dieCount[2] == 1 && dieCount[3] == 2 && dieCount[4] == 1 && dieCount[5] == 0||	// 23454
					dieCount[0] == 0 && dieCount[1] == 1 && dieCount[2] == 1 && dieCount[3] == 1 && dieCount[4] == 2 && dieCount[5] == 0) {	// 23455
				result = "SMALL STRAIGHT";
				userMoney = userMoney + 200;
			}

			// Four of a kind
			else if (dieCount[0] == 4 || dieCount[1] == 4 || dieCount[2] == 4  || dieCount[3] == 4 || dieCount[4] == 4 || dieCount[5] == 4) {
				result = "FOUR OF A KIND";
				userMoney = userMoney + 100;
			}


			// Full house
			else if (dieCount[0] == 3 && dieCount[1] == 2|| //
					dieCount[0] == 3 && dieCount[2] == 2||
					dieCount[0] == 3 && dieCount[3] == 2||
					dieCount[0] == 3 && dieCount[4] == 2||
					dieCount[0] == 3 && dieCount[5] == 2||
					dieCount[1] == 3 && dieCount[0] == 2||
					dieCount[2] == 3 && dieCount[0] == 2||
					dieCount[3] == 3 && dieCount[0] == 2||
					dieCount[4] == 3 && dieCount[0] == 2||
					dieCount[5] == 3 && dieCount[0] == 2||
					dieCount[1] == 3 && dieCount[2] == 2||
					dieCount[2] == 3 && dieCount[3] == 2||
					dieCount[3] == 3 && dieCount[4] == 2||
					dieCount[4] == 3 && dieCount[5] == 2||
					dieCount[2] == 3 && dieCount[1] == 2||
					dieCount[3] == 3 && dieCount[2] == 2||
					dieCount[4] == 3 && dieCount[3] == 2||
					dieCount[5] == 3 && dieCount[4] == 2||
					dieCount[1] == 3 && dieCount[5] == 2||
					dieCount[1] == 3 && dieCount[4] == 2||
					dieCount[1] == 3 && dieCount[3] == 2||
					dieCount[2] == 3 && dieCount[5] == 2||
					dieCount[2] == 3 && dieCount[4] == 2||
					dieCount[3] == 3 && dieCount[5] == 2) {
				result = "FULL HOUSE";
				userMoney = userMoney + 20;
			}

			// Three of a kind
			else if (dieCount[0] == 3 || dieCount[1] == 3 || dieCount[2] == 3  || dieCount[3] == 3 || dieCount[4] == 3 || dieCount[5] == 3) {
				result = "THREE OF A KIND";
				userMoney = userMoney + 50;
			}

			// Output values of dice roll and result 
			JOptionPane.showMessageDialog(null, "| Dice # |  1  |  2  |  3  |  4  |  5  |\n"
					+ "| Value  |  " + dieValues[0] + "  |  " + dieValues[1] + "  |  " + dieValues[2] + "  |  " + dieValues[3] + "  |  " + dieValues[4] + "  | " + 
					"\n \nNumber of Ones: " + dieCount[0] +"\nNumber of Twos: " + dieCount[1] + "\nNumber of Threes: " + dieCount[2] + "\nNumber of Fours: " + dieCount[3] + "\nNumber of Fives: " + dieCount[4] + "\nNumber of Sixes: " + dieCount[5] +
					"\n \nResult: " + result + "\nMoney remaining: $" + userMoney + "\nMoney gained: $" + (userMoney - intialMoney),
					"RESULT", JOptionPane.INFORMATION_MESSAGE);

			// If enters $10 and loses it stops the game
			if (userMoney == 0) {
				break;
			}
			else {
				continuation = JOptionPane.showConfirmDialog(null, "Would you like to play again? (-$10)", "PLAY AGAIN?",
						JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);

				// End game if user says no
				if (continuation == JOptionPane.NO_OPTION) {
					break;
				}

				// Taking away $10 from user's money if they want to continue 
				userMoney = userMoney - 10;

			}
		}

		// Thank you message
		JOptionPane.showMessageDialog(null, "Thank you for playing Yahtzee!", "YAHTZEE!", JOptionPane.INFORMATION_MESSAGE);

	}


}
