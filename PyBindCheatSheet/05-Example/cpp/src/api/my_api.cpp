// my_api.cpp
#include "my_api.h"
#include <stdexcept>


Guitar::Guitar(const std::string& manufacturer_name,
           const float price,
           const int num_strings) :
           mManufacturerName(manufacturer_name),
           mPrice(price),
           mNumStrings(num_strings)
{
}

Guitar::Guitar(const std::string& manufacturer_name,
               const float price) :
        mManufacturerName(manufacturer_name),
        mPrice(price)
{
}

Guitar::Guitar() {}

void Guitar::SetManufacturer(const std::string& manufacturer_name)
{
    mManufacturerName = manufacturer_name;
}

void Guitar::SetPrice(const float price)
{
    if (price < 0.0f)
    {
        throw std::invalid_argument("Price cannot be negative");
    }

    mPrice = price;
}
