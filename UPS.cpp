/*
Purpose: Track which lights are on during time of delivery
Authors: Adonte Mays   
Date: 2023-01-31
Updated:
*/

//Header Files

#include <iostream>
using namespace std;

// This program outputs which lights are on during the time of delivery

bool UPS(int t1_on, int t1_off, int t2_on, int t2_off, int t_ups);
int main()
{
    int t1_on, t1_off, t2_on, t2_off, t_ups; //Declaring vars
    int light1, light2; //Declaring vars
    cout << "Enter on time for t1_on." << endl; //t1_on time
    cin >> t1_on; // give t1_on value
    cout << "Enter off time for t1_off."<< endl; //t1_off time
    cin >> t1_off; // give t1_off value
    t1_on = t1_on + t1_off; //Calculate the total on time for t1
    cout << "Enter on time for t2_on." << endl; //t2_on time
    cin >> t2_on; //give t2_on value
    cout << "Enter off time for t2_off." << endl; //t2_off time
    cin >> t2_off; //give t2_off value
    t2_on = t2_on + t2_off; //Calculate the total on time for t2
    
    cout << "Enter on time for t_ups." << endl; //t_ups time
    cin >> t_ups; // give t_ups value
   
  //End of code due to school reasons (if you'd like to see the full code please let me know!)
