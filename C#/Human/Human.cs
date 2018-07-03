using System;

namespace Human {
    public class Human {
        public string Name { get; set; }
        public int Strength { get; set; } = 3;
        public int Intelligence { get; set; } = 3;
        public int Dexterity { get; set; } = 3;
        public int Health { get; set; } = 100;

        public Human(string name) {
            Name = name;
        }

        public Human(string name, int strength, int intelligence, int dexterity, int health) {
            Name = name;
            Strength = strength;
            Intelligence = intelligence;
            Dexterity = dexterity;
            Health = health;
        }

        public void Attack(Object prey) {
            var p = (Human) prey;
            if (p is Human) {
                p.Health -= 5 * Strength;
                System.Console.WriteLine($"ATTACK! {p.Name} loses {5*Strength} pts from their health.");
            }
            else {
                System.Console.WriteLine("Attack failed!");    
            }
            System.Console.WriteLine("Current Stats: " + p.LogStats() );
        }

        public string LogStats() {
            return $"Name: {Name}, Health: {Health}";
        }
    }
}