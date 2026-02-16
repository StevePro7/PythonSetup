#ifndef _MY_API_H_
#define _MY_API_H_

#include <memory>

template <typename T>
class Container
{
public:
    Container(const size_t num_elements);

    T& operator [](const size_t index);

    const T& operator [](const size_t index) const;

private:
    std::unique_ptr<T[]> mData;
};

#endif//_MY_API_H_