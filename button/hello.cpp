#include "hello.h"

extern "C" 
void hello::printMessage(void)
{
    cout << message << endl;
}