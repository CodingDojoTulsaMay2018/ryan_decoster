using System;

namespace phone
{
    class Program
    {
        static void Main(string[] args)
        {
            Galaxy S8 = new Galaxy ("s8", 100, "Verizon", "Dooo doo doo do");
            Nokia elevenHundred = new Nokia ("1100", 60, "T-Mobile", "Ringgg ring ringgg");

            S8.DisplayInfo();
            System.Console.WriteLine(S8.Ring());
            System.Console.WriteLine(S8.Unlock());
            System.Console.WriteLine("");

            elevenHundred.DisplayInfo();
            System.Console.WriteLine(elevenHundred.Ring());
            System.Console.WriteLine(elevenHundred.Unlock());
            System.Console.WriteLine("");

        }
    }
}
