using System;
using System.IO;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)

        {
            ulong[] numbers = Array.ConvertAll(Console.ReadLine().Split(), ulong.Parse);
            ulong num1 = numbers[0];
            ulong num2 = numbers[1];
            Console.WriteLine(num1*num2);

        }
    }
}