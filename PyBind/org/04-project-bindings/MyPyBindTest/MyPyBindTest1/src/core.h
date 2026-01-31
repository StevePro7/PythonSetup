#ifndef MYPYBINDTEST_CORE_H
#define MYPYBINDTEST_CORE_H

class Processor
{
public:
    Processor(int scale);
    int process(int x) const;

private:
    int scale_;
};

#endif //MYPYBINDTEST_CORE_H
