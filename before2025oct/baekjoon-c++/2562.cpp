#include <iostream>

using namespace std;

int main()
{
    int array[9];

    for (int i = 0; i < 9; i++)
    {
        cin >> array[i];
    };

    int maxValue = 0;
    int maxValueindex;

    for (int i = 0; i < 9; i++)
    {
        if (maxValue < array[i])
        {
            maxValue = array[i];
            maxValueindex = i + 1;
        }
    }

    cout << maxValue << endl;
    cout << maxValueindex << endl;

    return 0;
}