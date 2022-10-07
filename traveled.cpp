// The distance a vehicle travels can be calculated as follows:

//distance = speed * time
//For example, if a train travels 40 miles per hour for 3 hours, the distance traveled is 120 miles.

//write a program that asks the user for the speed of a vehicle (in miles per hour) 
//and how many hours it has traveled. 
//It should then use a loop to display the total distance traveled at the end of each hour of that time period. 
//Here is an example of the output:

//What is the speed of the vehicle in mph? 40
//How many hours has it traveled? 3

#include <iostream> 
#include <iomanip>
using namespace std; 
int main()
{
    int speed,hours_traveled, distance = 0; 
    // ask for the speed 
    cout << "What is the speed"; 
    while(!(cin >> speed )|| (speed < 0))
    {
        cout << "Error: the number for the speed must be greater than zero \n"; 
        cin.clear();
        cin.ignore(1200,'\n');
    } 
    cout << "What are the hours traveled";
    while(!(cin >> hours_traveled )|| (hours_traveled < 0))
    {
        cout << "Error: the number for the speed must be greater than one \n"; 
        cin.clear();
        cin.ignore(1200,'\n');
    } 

    cout << "hours distane tracled" << endl; 
    for(int i = 0; i < hours_traveled; i++)
    {
    distance += speed; 
    cout << "  " << (i + 1) << " " << distance << endl;     
    }
    return(0);
}