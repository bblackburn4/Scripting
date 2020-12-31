#include <iostream> 
#include <limits>

/*int csico = 5; // Example on calling a varable in C++ INTEGER(AKA NUMBERS)
double love; // user Defined vrarable 
int love = 0; // using love and giving it a INT
int width = 5; // Can do inline as well
int width(5); // same as above on line 6direct initil. NOTE NOT BEST OF ALL TYPES
int width{}; // Value initialized to 0
int width{5};// Dreict list 
int hight = {6}; // Coppy init to 6 ((DREICT FROM PERFERED ))
// int can only hold whole numbers
// Can use mulit but requred to use a comma (,)  "a" = 5 , "b" =6;
int a =5 ,c= 33; */

int main()
{
    std::cout << "Hello World, I am learning how to do this!!\n";
    std::cout << "\n";
    std::cout << "Thank you for being tolerent with me while leaning";
    // Steps below are for holding the screen untell press from user.
std::cin.clear(); // reset any error flags
std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // ignore any characters in the input buffer until we find an enter character
std::cin.get(); // get one more char from the user
/* so 
every note needs to be 
in like this one */
    return 0;
}

