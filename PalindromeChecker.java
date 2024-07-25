import java.util.Scanner;

public class PalindromeChecker {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter a string
        System.out.println("Enter a string: ");
        String input = scanner.nextLine();

        // Check if the string is a palindrome
        if (isPalindrome(input)) {
            System.out.println("The string is a palindrome.");
        } else {
            System.out.println("The string is not a palindrome.");
        }

        scanner.close();
    }

    // Method to check if a given string is a palindrome
    public static boolean isPalindrome(String str) {
        // Remove non-alphanumeric characters and convert to lower case
        String cleanedStr = str.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

        // Get the length of the cleaned string
        int len = cleanedStr.length();

        // Compare characters from the beginning and the end
        for (int i = 0; i < len / 2; i++) {
            if (cleanedStr.charAt(i) != cleanedStr.charAt(len - i - 1)) {
                return false; // Not a palindrome
            }
        }

        return true; // Is a palindrome
    }
}
