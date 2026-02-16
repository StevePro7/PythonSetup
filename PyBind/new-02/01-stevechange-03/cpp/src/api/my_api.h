#ifndef _MY_API_H_
#define _MY_API_H_

#include <memory>
#include <sstream>

template <typename T>
class Container
{
public:
    Container(const size_t num_elements) :
            mData( std::make_unique<T[]>(num_elements)),
            mSize(num_elements)
    {
    }

    T& operator [](const size_t index)
    {
        check_bounds(index);
        return mData[index];
    }

    const T& operator [](const size_t index) const
    {
        check_bounds(index);
        return mData[index];
    }

    size_t size() const { return mSize; }

private:
    void check_bounds(size_t index) const
    {
        if (index >= mSize)
        {
            std::ostringstream oss;
            oss << "Index " << index
                << " out of range (size=" << mSize << ")";
            throw std::out_of_range(oss.str());
        }
    }

    std::unique_ptr<T[]> mData;
    size_t mSize;
};
#endif//_MY_API_H_