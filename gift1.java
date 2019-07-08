/*
ID: graceti1
LANG: JAVA
TASK: gift1
*/

import java.io.*;
import java.util.*;
public class gift1 {

	public static void main(String[] args) throws IOException {
		//read file
		File file = new File("gift1.in");
		Scanner in = new Scanner(file);
		
		//first line 
		int np = in.nextInt();
		
		//lines 2 to np+1 - get Names and create lists/arrays 
		ArrayList<String> names = new ArrayList<String>();
			//use type arraylist because it can find the index of an element
		int[] money = new int[np];
		getNames(in, names, np); //works 

		//lines np+2 to end 
		getMoney(in, money, names);

		//print output to gift1.out
		PrintWriter out = new PrintWriter("gift1.out");
		for (int i = 0; i<money.length; i++) {
			out.println(names.get(i)+ " "+money[i]);
		}
		out.close();
	}
	
	// gets the names from lines 2 to np+1 and stores them in the array names
	// @param in 		Scanner object that reads file ride.in
	// @param names		arraylist of names of all friends
	// @param np		number of friends 
	public static void getNames(Scanner in, ArrayList<String> names, int np) {
		for (int i = 0; i<np; i++) {
			names.add(in.next());
		}
	}
	
	/* parses through the money amounts in lines np+2 to the end in gift1.in
	 * and passes this info into distributeMoney function which calculates 
	 * the money distributed accordingly and saves the values into an array
	 * 
	 * @param in		Scanner object that reads through the lines
	 * @param money 	array that stores the amount of money each person has
	 * @param names 	arraylist of names of all the friends 
	*/
	public static void getMoney(Scanner in, int[] money, ArrayList<String> names) {
		for (int i = 0; i<money.length; i++) {
			//takes giver name and finds corresponding index in names array
			int giverInd = names.indexOf(in.next()); 
			
			int giveAmt = in.nextInt();
			int numOfRecipients = in.nextInt();
			
			ArrayList<Integer> recipInd = new ArrayList<Integer>();
			for (int j = 0; j<numOfRecipients; j++) {
				recipInd.add(names.indexOf(in.next()));
			}
			distributeMoney(money, giverInd, giveAmt, recipInd);
			/*for (int k = 0; k<money.length; k++) { //error checking 
				System.out.print(money[k]+ " ");
			}
			System.out.println();*/
		}

	}

	
	/*	given the amt of money, the index of the Giver, and indices of recipient names
		distributes money accordingly among everyone in the money array
		
	* @param money 		array that stores the amount of money each person has
	* @param giverInd	index of the giver's name in the names arraylist
	* @param total 		amount of money to be divided into gifts by the giver
	* @param recipInd	arraylist of all the indices of the recipients names in the names arraylist
	* @return			void - updates the money array
	*/ 
	private static void distributeMoney(int[] money, int giverInd, int total, ArrayList<Integer> recipInd) {

		if (recipInd.size()!=0) { //to avoid divide by zero
			int perGift = total/recipInd.size();	
			int left = total%recipInd.size();
			money[giverInd] = money[giverInd]-total+left;
			//distribute gifts to recipients 
			for (int i = 0; i<recipInd.size(); i++) {
				money[recipInd.get(i)] += perGift; 
			}

		}
		
	}
}
