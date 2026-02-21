#include <iostream>
#include "api/my_api.h"

int main()
{
    std::cout << "Hello from my_app!" << std::endl;
	Guitar g = Guitar( "Ibanez", 2400.0f, 6 );
    std::string result = g.mManufacturerName;
    std::cout << "What is the manufacturer? " << result << "!" << std::endl;
    return 0;
}
