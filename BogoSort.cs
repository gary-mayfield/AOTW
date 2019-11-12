using System;
using System.Linq;
using System.Collections.Generic;

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
            BogoSort(arr);
            Console.WriteLine("Sorted array: ");
            PrintArray(arr);
        }

        static void BogoSort(int[] arr)
        {
            var counter = 0;
            while(!IsSorted(arr))
            {
                Console.WriteLine(counter);
                arr.Shuffle();
                counter++;
            }

        }

        static bool IsSorted(int[] data)
        {
            for (int i = 0; i < data.Length - 1; i++)
            {
                if (data[i] > data[i + 1])
                {
                    return false;
                }
            }
            return true;
        }

        static void PrintArray(int[] data)
        {
            for (int i = 0; i < data.Length; i++)
            {
                Console.WriteLine(data[i]);
            }
        }
    }

    static class Extensions
    {
        public static void Shuffle<T>(this IList<T> list)
        {
            int n = list.Count;
            Random rand = new Random();

            while(n > 1)
            {
                n--;
                int k = rand.Next(n + 1);
                T value = list[k];
                list[k] = list[n];
                list[n] = value;
            }
        }
    }
}