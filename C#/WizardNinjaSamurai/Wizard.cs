using System;
using System.Collections.Generic;

namespace wizardninjasamurai {
    public class Wizard : Human {

        public Wizard(string name) :base(name) {
            health = 50;
            intelligence = 25;
        }

        public void Heal() {
            health += 10 * intelligence;
            System.Console.WriteLine($"HEALED! {name} gained {10 * intelligence} pts to their health.");
        }

        public void Fireball(Object target) {
            Human enemy = target as Human;
            if (enemy != null) {
                Random rand = new Random();
                var damage = rand.Next(20, 51);
                enemy.health -= damage;
                System.Console.WriteLine($"ATTACK! {enemy.name} loses {damage} pts from their health.");
            }
            else {
                Console.WriteLine("Failed Attack");
            }
        }
    }
}