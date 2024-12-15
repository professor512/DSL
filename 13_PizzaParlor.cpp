// Pizza parlor accepting maximum M orders. Orders are served in first come first 
// served basis. Order once placed cannot be cancelled. Write C++ program to
// simulate the system using circular queue using array.



#include <iostream>
#include<string>
using namespace std;

class PizzaParlor{
    private:
        static const int MAX_ORDERS = 10;
        string orders[MAX_ORDERS];
        int front, rear, count;
        
    public:
        PizzaParlor(){
            front = 0;
            rear = -1;
            count = 0;
        }
        
        void placeOrder(const string& order){
            if(count == MAX_ORDERS){
                cout<<"\nOrder queue is Full";
                return;
            }
            rear = (rear + 1) % MAX_ORDERS;
            orders[rear] = order;
            cout<<"\nOrder Placed ";
            count++;
        }
        
        void serveOrder(){
            if(count == 0){
                cout<<"\nNo orders to Serve";
                return;
            }
            cout<<"\nOrder Served : "<<orders[front];
            front = (front + 1) % MAX_ORDERS;
            count--;
        }
        
        void displayOrders(){
            if(count == 0){
                cout<<"\nNo orders to Display";
                return;
            }
            for(int i = 0; i < count; i++){
                cout<<orders[(front + i) % MAX_ORDERS]<<" ";
            }
        }
};


int main()
{
   PizzaParlor p;
   string order;
   int choice;
   
   do{
    cout<<"\nPizza Parlor Menu";
    cout<<"\n1 - Place Order: ";
    cout<<"\n2 - Serve Order: ";
    cout<<"\n3 - Display Orders: ";
    cout<<"\n4 - EXIT: ";
    cin>>choice;
    cin.ignore();
    
    switch(choice){
        case 1:
            cout<<"\nEnter Order Name: ";
            getline(cin, order);
            p.placeOrder(order);
            break;
        case 2: 
            p.serveOrder();
            break;
        case 3: 
            p.displayOrders();
            break;
        case 4:
            cout<<"\nExiting Program...";
            break;
        default:
            cout<<"\nINVALID CHOICE";
    }
   }while(choice != 4);
    return 0;
}
