// my_api.cpp
#include "my_api.h"


template <typename T>
Container<T>::Container(const size_t num_elements)
{
    mData = std::make_unique<T[]>(num_elements);
}

template <typename T>
T& Container<T>::operator[](const size_t index)
{
    return mData[index];
}

template <typename T>
const T& Container<T>::operator[](const size_t index) const
{
    return mData[index];
}
