using System;
using System.Collections.Generic;

namespace wizardninjasamurai {
    public class Samurai : Human {

        public Samurai(string name) :base(name) {
            health = 200;
        }

        public void Death_Blow(Object target) {
            Human enemy = target as Human;
            if (enemy != null) {
                if (enemy.health < 50) {
                    enemy.health = 0;
                    System.Console.WriteLine($"ATTACK! {enemy.name} died from {name}'s death blow.");
                }
                else {
                    System.Console.WriteLine("Death blow missed!");
                }
            }
            else {
                Console.WriteLine("Failed Attack");
            }
        }

        public void Meditate() {
            health = 200;
            System.Console.WriteLine($"HEALED! {name} healed itself and is now restored back to full health.");
        }
    }
}