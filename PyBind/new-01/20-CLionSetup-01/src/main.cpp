#include <iostream>
#include "api/my_api.h"

int main()
{
    std::cout << "Hello from my_app!" << std::endl;
    int result = add(5, 4);
    std::cout << "what is " << "5 + 4 = " << result << std::endl;
    return 0;
}
