// A palindrome is a string of character that‘s the same forward and backward. 
// Typically, punctuation, capitalization, and spaces are ignored. For example, 
// “Poor Dan is in a droop” is a palindrome, as can be seen by examining the 
// characters “poor danisina droop” and observing that they are the same forward 
// and backward. One way to check for a palindromeis to reverse the characters in 
// the string and then compare with them the original-in a palindrome, the sequence 
// will be identical. Write C++ program with functions a) To print original string followed by reversed string using stack
// b) To check whether given string is palindrome or not

#include <iostream>
#include<stack>
using namespace std;

string reverse_str(const string& str){
    stack<char>s;
    for(char ch: str){
        s.push(ch);
    }
    
    string reversed;
    while(!s.empty()){
        reversed += s.top();
        s.pop();
    }
    return reversed;
}

int main()
{
    string str;
    
    cout<<"\nEnter a String: ";
    getline(cin, str);
    
    string reversed = reverse_str(str);
    cout<<"\nOriginal String: "<<str;
    cout<<"\nReversed String: "<<reversed;
    
    if(str == reversed)
        cout<<"\nThe String is Palindrom";
    else
        cout<<"\nString is not palindrom";
    
    
    return 0;
}
