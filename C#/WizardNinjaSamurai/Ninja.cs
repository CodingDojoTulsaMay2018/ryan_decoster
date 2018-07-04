using System;
using System.Collections.Generic;

namespace wizardninjasamurai {
    public class Ninja : Human {

        public Ninja(string name) :base(name) {
            dexterity = 175;
        }

        public void Steal(Object target) {
            Human enemy = target as Human;
            if (enemy != null) {
                enemy.health -= 10;
            }
            else {
                Console.WriteLine("Failed Attack");
            }
            health += 10;
            System.Console.WriteLine($"ATTACK! {name} gained {10} pts to their health and {enemy.name} lost {10} pts to their health.");
        }

        public void Get_Away() {
            health -= 15;
            System.Console.WriteLine($"RUN! {name} ran away and lost {15} pts to their health.");
        }
    }
}