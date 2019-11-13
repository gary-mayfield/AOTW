using System;
using System.Linq;

namespace MergeSort
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
            int[] sortedArr = MergeSort(arr);
            Console.WriteLine("Sorted array: ");
            PrintArray(sortedArr);
        }

        static int[] MergeSort(int[] arr)
        {
            if (arr.Length < 2)
            {
                return arr;
            }

            var middle = arr.Length / 2;
            var merged = new int[arr.Length];
            var left = new int[middle];
            var right = arr.Length % 2 == 0 ? new int[middle] 
                                            : new int[middle + 1];

            for (int i = 0; i < middle; i++)
            {
                left[i] = arr[i];
            }
            int index = 0;
            for (int j = middle; j < arr.Length; j++)
            {
                right[index] = arr[j];
                index++;
            }
            var l = MergeSort(left);
            var r = MergeSort(right);

            merged = Merge(l, r);
            return merged;
        }

        static int[] Merge(int[] left,int[] right)
        {

            var totalLength = left.Length + right.Length;
            var result = new int[totalLength];
            var leftIndex = 0;
            var rightIndex = 0;
            var resultIndex = 0;

            while (leftIndex < left.Length || rightIndex < right.Length)
            {
                if (leftIndex < left.Length && rightIndex < right.Length)
                {
                    if (left[leftIndex] <= right[rightIndex])
                    {
                        result[resultIndex] = left[leftIndex];
                        leftIndex++;
                        resultIndex++;
                    }
                    else
                    {
                        result[resultIndex] = right[rightIndex];
                        rightIndex++;
                        resultIndex++;
                    }                  
                }
                else if (leftIndex < left.Length)
                {
                    result[resultIndex] = left[leftIndex];
                    leftIndex++;
                    resultIndex++;
                }
                else if (rightIndex < right.Length)
                {
                    result[resultIndex] = right[rightIndex];
                    rightIndex++;
                    resultIndex++;
                }
            }
            return result;
        }

        static void PrintArray(int[] data)
        {
            for (int i = 0; i < data.Count(); i++)
            {
                Console.WriteLine(data[i]);
            }
        }
    }
}