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
            QuickSort(arr, 0, arr.Length - 1);
            Console.WriteLine("Sorted array: ");
            PrintArray(arr);
        }

        static int Partition(int[] arr, int left, int right)
        {
            int pivot = arr[right];
            int i = left - 1;
            for (int j = left; j < right; j++)
            {
                if(arr[j] <= pivot)
                {
                    i += 1;
                    var a = arr[j];
                    arr[j] = arr[i];
                    arr[i] = a;
                }
            }
        
        var b = arr[right];
        arr[right] = arr[i + 1];
        arr[i + 1] = b;
        return (i + 1);
        }


        static void QuickSort(int[] arr, int low, int high)
        {
            if (low < high)
            {
                var pi = Partition(arr, low, high);
                QuickSort(arr, low, pi - 1);

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