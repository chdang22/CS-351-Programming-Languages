/*
* Concurrency lab
* We will use C++ for this lab practice.
* Below program has multiple threads that changes the same memory nodes.
* You can see the program gives unstable output.
* 
* Please use the WriteLock.cpp as example to add in the read-write lock and fix this program.
* Program output should be similar to WriteLock.cpp with a few rounds of simulation
* showing output without lock and a few rounds showing output with lock.
* 
* Submit .cpp file and a file with your program output (in a text, word document, or screenshots).
* 
* Grading: 4pt HW
* Submit working code with read-write lock 2pt
* Code output format 1pt
* Output file submission 1pt
*/

/*IMPORTANT: the lock library and coding format we used in WriteLock.cpp example needs
* C++ 17 (Visual Studio 2015) or later. You can try online compilers or install visual studio
* communnity on your computer. The school account gives you free log in to the VS. 
* 
* If you use VS, you need to create a new c++ project 
*	-> right click Source Files on the Solution Explorer 
*	-> add the example code file or create a new c++ file 
*	-> right click the .cpp file name on top of your script tab 
*	-> Open containing folder to find your .cpp file to submit
*	-> ONLY submit the .cpp, not the emtire VS project.
*/

#include <iostream>
#include <string>
#include <thread>
#include <map> // gives you access to the map data structure that is similar to dictionary
#include <shared_mutex> //need C++ 17 (Visual Studio 2015 or after)
using namespace std;

//shared memory between different threads.
map<string, int> INVENTORY;

bool debugMsg = true; //print middle steps or not

std::shared_timed_mutex inventory_mutex; //mutex for inventory


void print_map(const map<string, int>& inventory)
{
	std::cout <<endl<< "...Inventory: ";
	for (const auto& elem : inventory)
		std::cout << '[' << elem.first<< "  " << elem.second << "]; ";
	std::cout << endl;
}
void BuyItem(string customerName, string itemName, int amount, bool enableWriteLock) {
    if (enableWriteLock)
        //lock
        inventory_mutex.lock();

    //read the inventory information
    if (debugMsg) {
        std::cout << endl << customerName << " Buy... " << amount << "	" << itemName << "  read inventory" << endl;
        print_map(INVENTORY);
    }
    this_thread::sleep_for(chrono::milliseconds(10)); //simulating any system or network delays

    //perform calculation that will modify the shared data
    int newAmount = INVENTORY[itemName] - amount;

    //save the calculated result back and print info
    this_thread::sleep_for(chrono::milliseconds(10)); //simulating any system or network delays
    //if itemName is not exist in the map, it will be inserted automatically with value set to 0
    if (newAmount >= 0)
        INVENTORY[itemName] = newAmount;
    else {
        std::cout << customerName << "	SOLD OUT! Cannot buy." << endl;
        if (enableWriteLock)
            //lock
            inventory_mutex.unlock();
        return;

    }


    if (debugMsg) {
        std::cout << endl << customerName << " Finished buy... " << amount << "	" << itemName << endl;
        print_map(INVENTORY);
    }
    if (enableWriteLock)
        inventory_mutex.unlock();
}
void ReturnItem(string customerName, string itemName, int amount, bool enableWriteLock)
{
    if (enableWriteLock)
        //lock
        inventory_mutex.lock();
    //read the inventory information
	if (debugMsg)
	{
		std::cout << endl << customerName << " Return... " << amount << "	" << itemName << "  read inventory" << endl;
		print_map(INVENTORY);
	}
	this_thread::sleep_for(chrono::milliseconds(10)); //simulating any system or network delays

	//perform calculation that will modify the shared data
	int newAmount = INVENTORY[itemName] + amount;

	//save the calculated result back and print info
	this_thread::sleep_for(chrono::milliseconds(10)); //simulating any system or network delays
	//if itemName is not exist in the map, it will be inserted automatically with value set to 0
	INVENTORY[itemName] = newAmount;

	if (debugMsg)
	{
		std::cout << endl << customerName << " Finished return... " << amount << "	" << itemName << endl;
		print_map(INVENTORY);
	}
    if (enableWriteLock)
        inventory_mutex.unlock();
}
/*1 round of simulation
* Set the the inventory to the default value at the beginning 
* Create a few threads that modifies the shared value
*/
void Sim_Inventory(int round, bool enableWriteLock)
{
    if (enableWriteLock)
        std::cout << endl << "####################" << endl << "With lock. ROUND " << round << endl << "####################" << endl;
    else
	    std::cout << endl <<endl << "####################" << endl << "No lock. ROUND " << round << endl << "####################" << endl;
	//set same starting inventory for each round
	INVENTORY = { {"book", 5} ,{"PC",7},{"card", 11} };

	//create 4 threads calling either deposite or withdraw functions that modifies the ACCOUNT_BALANCE
	thread customer1(BuyItem,"customer1", "PC", 2, enableWriteLock);
	thread customer2(ReturnItem, "customer2", "bottle", 9, enableWriteLock);
	thread customer3(ReturnItem, "customer3", "PC", 1, enableWriteLock);
	thread customer4(BuyItem, "customer4", "bottle", 2, enableWriteLock);

	//start the threads
	customer1.join();
	customer2.join();
	customer3.join();
	customer4.join();

	//atm5 and 6 started a little later than previous threads
	thread customer5(BuyItem, "customer5", "card", 7, enableWriteLock);
	thread customer6(ReturnItem, "customer6", "card", 1, enableWriteLock);
	customer5.join();
	customer6.join();

	//Please calculate the correct inventory here
    map<string, int> correctInventory;
    correctInventory = {{"book",5}, {"PC",6}, {"card", 5}, {"bottle", 7}};
	//Please output the correct inventory and the output from the simulation with clear output format
    cout << endl<<"***Correct/Expected  Inventory:";
    print_map(correctInventory);
    cout << " Actual Inventory:";
    print_map(INVENTORY);

}
int main() {
    //rounds of simulation
    int rounds = 10;
    bool enableWriteLock;

    //Run the simulation with multiple threads that do not have the read-write lock
    //You will see unstable output
    enableWriteLock = false;
    for (int r = 1; r <= rounds; r++)
        Sim_Inventory(r, enableWriteLock);

    //write lock on
    enableWriteLock = true;
    for (int r = 1; r <= rounds; r++)
        Sim_Inventory(r,enableWriteLock);

}