#ifndef _MY_API_H_
#define _MY_API_H_

#include <string>

struct Guitar
{
    Guitar(const std::string& manufacturer_name,
           const float price,
           const int num_strings);

    Guitar(const std::string& manufacturer_name,
           const float price);

    Guitar();

    void SetManufacturer(const std::string& manufacturer_name);
    void SetPrice(const float price);

    std::string mManufacturerName {""};
    float mPrice {0.f};
    int mNumStrings {0};
};

#endif//_MY_API_H_