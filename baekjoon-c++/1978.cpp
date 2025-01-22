#include <iostream>

using namespace std;

// Function to check if a number is prime
bool prime(int n)
{
    if (n < 2)
        return false;
    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main()
{
    int N;
    int M;
    int ans = 0;

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> M;

        if (M >= 2 && prime(M))
        {
            ans++;
        }
    }

    cout << ans;

    return 0;
}
