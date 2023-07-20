#include <iostream>
using namespace std;

int main() {
    int A,B,C,D,E,F = 0;
    int x = 0;
    int y = 0; 

    cin >> A >> B >> C >> D >> E >> F;

    for (x=-10000; x<10001; x++){
        for (y=-10000; y<10001; y++){
            if(A*x + B*y == C){
                if (D*x + E*y == F){
                    cout << x << " " << y << endl;
                    return 0; 
                }
            }
        }
    }
}