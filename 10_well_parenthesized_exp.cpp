// In any language program mostly syntax error occurs due to unbalancing
// delimiter such as (),{},[]. Write C++ program using stack to check whether given 
// expression is well parenthesized or not.

#include<iostream>
#include<stack>
using namespace std;

bool well_parenthesized(const string& str){
    stack<char>s;
    for(char ch: str){
        if(ch == '(' || ch == '[' || ch == '{')
            s.push(ch);
            
        else if(ch == ')' || ch == ']' || ch == '}'){
            if(s.empty())
                return false;
            char top = s.top();
            if((ch == ')' && top != '(') || 
                (ch == ']' && top != '[') ||
                (ch == '}' && top != '{')){
                    return false;
                }
            s.pop();
        }
    }
    return s.empty();
}

int main(){
    
    string expression;
    cout<<"\nEnter an Expression: ";
    getline(cin, expression);
    
    if(well_parenthesized(expression))
        cout<<"\nThe expression is well parethensized";
    else
        cout<<"\nThe expression is not well parenthezied";
    
    return 0;
    
}
