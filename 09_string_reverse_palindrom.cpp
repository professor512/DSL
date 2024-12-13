#include <iostream>
#include <stack>
using namespace std;

// Function to reverse the string using a stack
string reverseUsingStack(const string& str) {
    stack<char> s;
    for (char ch : str) {
        s.push(ch);
    }

    string reversed;
    while (!s.empty()) {
        reversed += s.top();
        s.pop();
    }
    return reversed;
}

// Function to check if a string is a palindrome
bool isPalindrome(const string& str) {
    string reversed = reverseUsingStack(str);
    return str == reversed;
}

int main() {
    string input;
    cout << "Enter a string: ";
    getline(cin, input);

    string reversed = reverseUsingStack(input);

    cout << "Original string: " << input << endl;
    cout << "Reversed string: " << reversed << endl;

    if (isPalindrome(input)) {
        cout << "The given string is a palindrome." << endl;
    } else {
        cout << "The given string is not a palindrome." << endl;
    }

    return 0;
}
