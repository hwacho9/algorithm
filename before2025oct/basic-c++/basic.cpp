#include <iostream>

using namespace std;

int main()
{
    string a = "abcd";
    string b = a.substr(4);

    // 0 -> abcd
    // 1 -> bcd
    // 2 -> cd
    // 3 -> d
    // 4 ->

    cout << b << endl;

    return 0;
}