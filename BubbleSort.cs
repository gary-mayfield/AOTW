using System;
using System.Linq;

namespace Sort
{
    class Sort
    {
        static void Main()
        {
            Random random = new Random();

            var arr = Enumerable
                        .Repeat(0,10)
                        .Select(x => random.Next(1, 25))
                        .ToArray();

            Console.WriteLine("Unsorted array: ");
            PrintArray(arr);
            BubbleSort(arr);
            Console.WriteLine("Sorted array: ");
            PrintArray(arr);
        }

        static void BubbleSort(int[] arr)
        {
            var n = arr.Length;
            for (int i = 0; i < n - 1; i++)
            {
                for (int j = 0; j < n - i - 1; j++)
                {
                    if(arr[j] > arr[j + 1])
                    {
                        var temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                    }
                }
            }
        }

        static void PrintArray(int[] data)
        {
            for (int i = 0; i < data.Length; i++)
            {
                Console.WriteLine(data[i]);
            }
        }
    }
}