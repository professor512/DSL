// Queues are frequently used in computer programming, and a typical example is 
// the creation of a job queue by an operating system. If the operating system does 
// not use priorities, thenthe jobs are processed in the order they enter the system. 
// Write C++ program for simulating job queue. Write functions to add job and 
// delete job from queue.


#include<iostream>
#include<string>
using namespace std;

class JobQueue{
    private:
        static const int MAX_SIZE = 10;
        string jobQueue[MAX_SIZE];
        int front, rear, count;
        
    public:
        JobQueue(){
            front = 0;
            rear = -1;
            count = 0;
        }
        
        void addJob(const string& job){
            if(count == MAX_SIZE){
                cout<<"\nQueue is Full";
                return;
            }
            rear = (rear + 1) % MAX_SIZE;
            jobQueue[rear] = job;
            count++;
            cout<<"\nNew job added";
            
        }
        
        void deleteJob(){
            if(count == 0){
                cout<<"\nNo jobs to delete";
                return;
            }
            cout<<"\nJob Deleted: "<<jobQueue[front];
            front = (front + 1) % MAX_SIZE;
            count--;
        }
        
        void displayJob(){
            if(count == 0){
                cout<<"\nNo jobs to display";
                return;
            }
            for(int i = 0; i < count; i++){
                cout<<jobQueue[(front + i) % MAX_SIZE]<<" ";
            }
        }
};

int main(){
    JobQueue j;
    string job;
    int choice;
    
    do{
        cout<<"\nJob Queue Menu: ";
        cout<<"\n1 - Add Job";
        cout<<"\n2 - Delete Job";
        cout<<"\n3 - Display Jobs";
        cout<<"\n4 - EXIT\n";
        cin>>choice;
        cin.ignore();
        
        switch(choice){
            case 1:
                cout<<"\nEnter Job name: ";
                getline(cin, job);
                j.addJob(job);
                break;
            case 2:
                j.deleteJob();
                break;
            case 3: 
                j.displayJob();
                break;
            case 4:
                cout<<"\nExiting Program...";
                break;
            default:
                cout<<"\nEnter Correct Option: ";
        }
    }while(choice != 4);
    return 0;
}
