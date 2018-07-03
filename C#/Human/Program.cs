using System;

namespace Human
{
    class Program
    {
        static void Main(string[] args)
        {
            var player1 = new Human("Ryan");
            var player2 = new Human("Satan", 10, 50, 5, 20);
            player2.Attack(player1);
        }
    }
}
