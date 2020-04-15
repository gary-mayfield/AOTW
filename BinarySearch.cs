using System;

namespace BinarySearch
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] arr = {2, 3, 4, 15, 20, 50,60,99,101};
            int n = arr.Length;
            int x = 15;

            int result = BinarySearch(arr, 0, n - 1, x);

            if (result == -1)
            {
                Console.WriteLine("Found");
            }
            else
            {
                Console.WriteLine("Found");
            }

        }

        private static int BinarySearch(int[] arr, int start, int end, int x)
        
        {
            if (end >= start)
            {
                int mid = (start + end) / 2;

                if (arr[mid] == x)
                    return mid;

                if (arr[mid] > x)
                    return BinarySearch(arr, start, mid - 1, x);

                return BinarySearch(arr, mid + 1, end, x);
            }

            return -1;
        }
    }
}
