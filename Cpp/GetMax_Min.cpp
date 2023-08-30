#include <iostream>

int main()
{
    int x , y , z;
    std::cout << "Enter three numbers" <<std::endl;
    std::cin >> x >> y >> z;
    if (x > y && x > z)
    {
        std::cout <<"1st is the largest"<<std::endl;
    }
    else if (y > x && y > z)
    {
        std::cout <<"2nd is the largest"<<std::endl;
    }
    else if (z > x && z > y)
    {
        std::cout <<"3rd is the largest"<<std::endl;
    }

}