#include <iostream>

int main()
{
    std::cout << " ASCI Table"<<std::endl;
    std::cout << "--------------------------"<<std::endl;
    std::cout << "|char \t| ASCII |"<<std::endl;
    std::cout << "--------------------------"<<std::endl;
    int i = 0;
    for(; i<127; i++)
    {
        printf("|%d \t| %c |\n",i,i);
    }
}