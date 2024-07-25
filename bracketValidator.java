import java.util.Stack;

public class bracketValidator {

    public static void main(String[] args) {
        // Test cases
        String test1 = "()";
        String test2 = "([])";
        String test3 = "([)]";
        String test4 = "{[()]}";
        String test5 = "(((())))";
        String test6 = "{[(])}";

        System.out.println(test1 + ": " + isValid(test1));
        System.out.println(test2 + ": " + isValid(test2));
        System.out.println(test3 + ": " + isValid(test3));
        System.out.println(test4 + ": " + isValid(test4));
        System.out.println(test5 + ": " + isValid(test5));
        System.out.println(test6 + ": " + isValid(test6));
    }

    public static boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            // If opening bracket, push to stack
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } 
            // If closing bracket, check if stack is empty or top of stack is the matching opening bracket
            else if (c == ')' && !stack.isEmpty() && stack.peek() == '(') {
                stack.pop();
            } 
            else if (c == '}' && !stack.isEmpty() && stack.peek() == '{') {
                stack.pop();
            } 
            else if (c == ']' && !stack.isEmpty() && stack.peek() == '[') {
                stack.pop();
            } 
            // If closing bracket does not match opening bracket
            else {
                return false;
            }
        }

        // If stack is empty, all brackets matched correctly
        return stack.isEmpty();
    }
}