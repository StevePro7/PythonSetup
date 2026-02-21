#include <iostream>
#include "api/my_api.h"

int main()
{
    std::cout << "Hello from my_app!" << std::endl;

    // Create a Container of 5 integers
    Container<int> numbers(5);

    // Fill the container
    for (size_t i = 0; i < numbers.size(); ++i)
    {
        numbers[i] = static_cast<int>(i * 10);
    }

    // Print the contents
    std::cout << "Container contents\n";
    for (size_t i = 0; i < numbers.size(); ++i)
    {
        std::cout << "numbers[" << i << "] = "
                  << numbers[i] << std::endl;
    }

    return 0;
}
