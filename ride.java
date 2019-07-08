
/*
ID: graceti1
LANG: JAVA
TASK: ride
*/
import java.io.*;
import java.util.*;

public class ride {
	public static void main (String [] args) throws IOException {
		 BufferedReader f = new BufferedReader(new FileReader("ride.in"));
		 PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("ride.out")));
		 StringTokenizer st = new StringTokenizer(f.readLine()); //reads 1st line of text
		 
		 String s1 = st.nextToken(); //first string		
		 st = new StringTokenizer(f.readLine());
		 String s2 = st.nextToken(); //second string 
		 
		 //String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

		 int num1 = 1, num2 = 1;
		 for (int i = 0; i<s1.length(); i++) {
			 //int index = alphabet.indexOf(s1.charAt(i))+1;
			 int index = (int) (s1.charAt(i))-'A'+1; //ascii
			 num1 = num1 * index;
		 }
		 for (int j = 0; j<s2.length(); j++) {
			 //int index1 = alphabet.indexOf(s2.charAt(j))+1;
			 int index = (int) s2.charAt(j) - 'A' +1; //ascii
			 num2 = num2 * index;
		 }
		 if (num1%47 == num2%47) {
			 out.println("GO");
		 }
		 else {
			 out.println("STAY");
		 }
		 out.close();                                  // close the output file
	}
}