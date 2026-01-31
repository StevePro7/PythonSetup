#include "core.h"

Processor::Processor(int scale) : scale_(scale)
{
}

int Processor::process(int x) const
{
    return x * scale_ * 2;
}
