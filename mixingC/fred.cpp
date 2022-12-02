#include "fred.h"
#include <iostream>

extern "C" void print(void)
{
    std::cout << "Hello World!" << std::endl;
}
