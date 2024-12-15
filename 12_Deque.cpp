#include <iostream>
#include <string>
using namespace std;

class Deque {
private:
    static const int MAX_SIZE = 10; // Maximum size of the deque
    string deque[MAX_SIZE];        // Array to store deque elements
    int front, rear, count;        // Front, rear indices and element count

public:
    Deque() : front(0), rear(-1), count(0) {}

    void addRear(const string& job) {
        if (count == MAX_SIZE) {
            cout << "\nDeque is Full";
            return;
        }
        rear = (rear + 1) % MAX_SIZE;
        deque[rear] = job;
        count++;
        cout << "\nNew Job Added At REAR";
    }

    void addFront(const string& job) {
        if (count == MAX_SIZE) {
            cout << "\nDeque is Full";
            return;
        }
        front = (front - 1 + MAX_SIZE) % MAX_SIZE;
        deque[front] = job;
        count++;
        cout << "\nNew Job Added At FRONT";
    }

    void deleteRear() {
        if (count == 0) {
            cout << "\nDeque is Empty";
            return;
        }
        cout << "\nElement Deleted At REAR: " << deque[rear];
        rear = (rear - 1 + MAX_SIZE) % MAX_SIZE;
        count--;
    }

    void deleteFront() {
        if (count == 0) {
            cout << "\nDeque is Empty";
            return;
        }
        cout << "\nElement Deleted At FRONT: " << deque[front];
        front = (front + 1) % MAX_SIZE;
        count--;
    }

    void display() const {
        if (count == 0) {
            cout << "Nothing to Display";
            return;
        }
        cout << "\nElements in Deque: ";
        for (int i = 0; i < count; i++) {
            cout << deque[(front + i) % MAX_SIZE] << " ";
        }
        cout << endl;
    }
};

int main() {
    Deque d;
    string job;
    int choice;

    do {
        cout << "\nDeque Menu";
        cout << "\n1 - Add at Front";
        cout << "\n2 - Add at Rear";
        cout << "\n3 - Delete at Front";
        cout << "\n4 - Delete at Rear";
        cout << "\n5 - Display Deque";
        cout << "\n6 - EXIT\n";
        cin >> choice;
        cin.ignore();

        switch (choice) {
        case 1:
            cout << "\nEnter job name at Front: ";
            getline(cin, job);
            d.addFront(job);
            break;

        case 2:
            cout << "\nEnter job name at Rear: ";
            getline(cin, job);
            d.addRear(job);
            break;

        case 3:
            d.deleteFront();
            break;

        case 4:
            d.deleteRear();
            break;

        case 5:
            d.display();
            break;

        case 6:
            cout << "\nExiting Program...";
            break;

        default:
            cout << "\nInvalid Choice. Try Again.";
        }

    } while (choice != 6);

    return 0;
}
