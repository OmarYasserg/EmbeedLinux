#include<iostream>

int main()
{
    char letter;
    std::cout << "Enter the letter"<<std::endl;
    std::cin >> letter ;
    if(letter == 'a' or letter == 'e' or letter == 'o' or letter == 'u' or letter == 'i' )
    {
        std::cout <<"Is vowel";
    }
    else
    {
        std::cout <<"Isn't vowel";
    }
}