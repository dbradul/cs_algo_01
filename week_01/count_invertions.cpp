#include <iostream>
#include <fstream>
#include <vector>
#include <cassert>
#include <algorithm>
#include <iterator>

using namespace std;


long sort_and_count_invertions(vector<int>& v)
{
    long num_invertions = 0;

    if (v.size() > 1)
    {
        vector<int> left(v.begin(), v.begin()+v.size()/2);
        vector<int> right(v.begin()+v.size()/2, v.end());

        num_invertions += sort_and_count_invertions(left);
        num_invertions += sort_and_count_invertions(right);

        int k = 0, i = 0, j = 0;
        while (i < left.size() && j < right.size())
        {
            if (left[i] <= right[j])
            {
                v[k] = left[i];
                i++;
            }
            else
            {
                v[k] = right[j];
                j++;
                num_invertions += left.size() - i;
            }

            k++;
        }

        std::copy(left.begin()+i, left.end(), v.begin()+k);
        k += left.size() - i;
        std::copy(right.begin()+j, right.end(), v.begin()+k);
    }

    return num_invertions;
}


long count_invertions(const vector<int>& v)
{
    vector<int> v_sorted = v;
    return sort_and_count_invertions(v_sorted);
}


int brute_force(const vector<int>& v)
{
    long num_invertions = 0;

    for(int i=0; i<v.size(); ++i)
    {
        for (int j=i; j<v.size(); ++j)
        {
            if (v[j] < v[i])
            {
               num_invertions++;
            }
        }
    }

    return num_invertions;
}

void test_assert(const vector<int>& v)
{
    long num_invertions = count_invertions(v);
    assert(num_invertions == brute_force(v));
    cout << num_invertions << endl;
}

int main(int argc, char *argv[])
{
    test_assert({1,2,3,4,5,6});
    test_assert({1,1,1});
    test_assert({1,2,2,2});
    test_assert({1,2,2,3,3});

    test_assert({1,2,3,4,5,6,1});
    test_assert({1,2,3,4,5,6,1,2});
    test_assert({1,2,3,4,5,6,1,2,7,8});
    test_assert({1,2,3,4,5,6,1,2,7,8,1,2});
    test_assert({6,5,4,3,2,1});
    test_assert({6,5,4,3,2,1,1,2,3,4,5,6});
    test_assert({6,5,4,3,2,1,1,2,3,4,5,6,7,8});

    vector<int> v;
    ifstream inputFile("../week_01/integerArray.txt");
    if (inputFile)
    {
        std::istream_iterator<int> input(inputFile);
        std::copy(input, std::istream_iterator<int>(),
                  std::back_inserter(v));
        test_assert(v);
    }

    cout << "SUCCESS" << endl;

    return 0;
}
