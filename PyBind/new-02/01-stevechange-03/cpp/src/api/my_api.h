#ifndef _MY_API_H_
#define _MY_API_H_

#include <memory>

template <typename T>
class Container
{
public:
    Container(const size_t num_elements)
    {
        mData = std::make_unique<T[]>(num_elements);
    }

    T& operator [](const size_t index)
    {
        return mData[index];
    }

    const T& operator [](const size_t index) const
    {
        return mData[index];
    }

private:
    std::unique_ptr<T[]> mData;
};
#endif//_MY_API_H_