using System;

namespace wizardninjasamurai
{
    class Program
    {
        static void Main(string[] args)
        {
            var player1 = new Samurai ("Ryan");
            var player2 = new Human ("Satan");
            // player1.Fireball(player2);
            // player1.Heal();
            // player1.Steal(player2);
            // player1.Get_Away();
            player1.Death_Blow(player2);
            player1.Meditate();
        }
    }
}
