using System;
using System.Linq;

namespace SelectionSort
{
    class SelectionSort
    {
        static void Main()
        {
            Random random = new Random();

            var arr = Enumerable
                .Repeat(0, 10)
                .Select(x => random.Next(1,25))
                .ToArray();

            Console.WriteLine("Unsorted array: ");
            PrintArray(arr);
            SelectionSort(arr);
            Console.WriteLine("Sorted array: ");
            PrintArray(arr);
        }

        static void SelectionSort(int[] data)
        {
            for (int i = 0; i < data.Length - 1; i++)
            {
                int minIndex = i;
                for (int j = i + 1; j < data.Length; j++)
                {
                    if (data[j] < data[minIndex])
                    {
                        minIndex = j;
                    }
                }
                var temp = data[minIndex];
                data[minIndex] = data[i];
                data[i] = temp;
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
