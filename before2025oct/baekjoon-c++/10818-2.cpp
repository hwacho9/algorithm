#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, const char *argv[])
{
    int N;
    cin >> N;

    int array[N + 1];

    for (int i = 0; i < N; i++)
    {
        cin >> array[i];
    }

    sort(array, array + N);

    cout << array[0] << " " << array[N - 1];

    return 0;
}