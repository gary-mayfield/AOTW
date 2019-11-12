using System;
using System.Linq;

namespace HeapSort
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
            HeapSort(arr);
            Console.WriteLine("Sorted array: ");
            PrintArray(arr);
        }

        static void Heapify(int[] arr, int n, int i)
        {
            int largest = i;
            int left = 2 * i + 1;
            int right = 2 * i + 2;

            if (left < n && arr[left] > arr[largest])
            {
                largest = left;
            }

            if (right < n && arr[right] > arr[largest])
            {
                largest = right;
            }

            if (largest != i)
            {
                var swap = arr[i];
                arr[i] = arr[largest];
                arr[largest] = swap;

                Heapify(arr, n, largest);
            }
        }


        static void HeapSort(int[] arr)
        {
            var n = arr.Length;

            for (int i = n / 2 - 1; i >= 0; i--)
            {
                Heapify(arr, n, i);
            }

            for (int i = n - 1; i >= 0; i--)
            {
                var temp = arr[i];
                arr[i] = arr[0];
                arr[0] = temp;
                Heapify(arr, i, 0);
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