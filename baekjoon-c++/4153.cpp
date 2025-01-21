#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int array[3];

    while (1)
    {
        for (int i = 0; i < 3; i++)
        {
            cin >> array[i];
        }

        if (array[0] == 0 || array[1] == 0 || array[2] == 0)
        {
            break;
        }

        sort(array, array + 3);

        if (array[0] * array[0] + array[1] * array[1] == array[2] * array[2])
        {
            cout << "right" << endl;
        }
        else
        {
            cout << "wrong" << endl;
        }
    }

    return 0;
}