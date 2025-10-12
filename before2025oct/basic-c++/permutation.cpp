#include <iostream>

using namespace std;

int main()
{
    vector<int> a = {1, 2, 3};

    int b[] = {1, 2, 3};

    sort(a.begin(), a.end());
    do
    {
        // for (int i = 0; i < 2; i++)
        // {
        //     cout << a[i] << " ";
        // }
        for (int i : a)
            cout << i << " ";
        cout << endl;
    } while (next_permutation(a.begin(), a.end()));

    do
    {
        for (int i : b)
            cout << i << "";
        cout << '\n';
    } while (next_permutation(&b[0], &b[0] + 3));
}
