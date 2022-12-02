#ifndef HELLO_H_
#define HELLO_H_

#ifdef _cplusplus
extern "C" {
#endif

#include <iostream>
#include <string>
using namespace std;

class hello {
private:
    string message;

public:
    hello(string message);
    void printMessage(void);
    ~hello();
};

hello::hello(string message)
{
    this->message = message;
}

hello::~hello()
{
}

#ifdef _cplusplus
}
#endif
#endif