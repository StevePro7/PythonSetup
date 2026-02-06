#include <iostream>
#include "api/my_api.h"

int main() {
    std::cout << "Hello from my_app!" << std::endl;
    int result = add(5, 3);
    std::cout << "5 + 3 = " << result << std::endl;
    return 0;
}
