/*
ID: graceti1
LANG: JAVA
TASK: friday
*/

import java.io.*;
import java.util.*;
public class friday {
	
	//returns whether the given year is a leap year or not
	private static boolean isLeap(int year) {
		boolean leap = false;
		if (year%4 == 0) {
			leap = true;
			if (year%100 == 0 && year%400!=0) {
				leap = false;
			}
		}
		return leap;
	}
	
	//given the date month+1/13/year, finds the number of days till the next month 
	//at the date month+2/13/year
	//month is indexed starting at 0 
	public static int numOfDays(int month, int year) {
		int[] daysPerMonth = new int[] {31,28,31,30,31,30,31,31,30,31,30,31};
		if (month==1 && isLeap(year)) { //February on a leap year 
			daysPerMonth[1] = 29;
		}
		return daysPerMonth[month];
	}
	
	

	public static void main(String[] args) throws IOException {
		//read file
		File file = new File("friday.in");
		Scanner in = new Scanner(file);
		int N = in.nextInt(); //first line of the file 
		in.close();
		
		//define variables 
		int[] count13 = new int[7];
		int y = 1900, m;
		int dayOfWeek = 0; //Saturday on 1/13/1900
		
		//loop through every year 
		while (y <= 1900+N-1) {
			//loop through each month
			for (m = 0; m<12; m++) { //i counts the month, indexed starting at 0
				//increase counter for the day that the date m+1/13/y appears in 
				count13[dayOfWeek]++;
				//calculate day of week for next month (m+2/13/y)
				dayOfWeek = (dayOfWeek + numOfDays(m, y))%7; 
			}
			y++;
		}
		
		//output result into the file 
		PrintWriter out = new PrintWriter("friday.out");
		String str = "";
		for (int j = 0; j<count13.length; j++) {
			str += count13[j]+" "; 
		}
		out.println(str.trim());
		out.close();
	}

}
