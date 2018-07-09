using System;
using System.Collections.Generic;

namespace dojodachi {
    public class Dachi {
        public int Happiness {get; set;} = 20;
        public int Fullness {get; set;} = 20;
        public int Energy {get; set;} = 50;
        public int Meals {get; set;} = 3;
        public string Status {get; set;} = "Welcome to Dojodachi, use buttons below to interact with your Dachi.";
        Random rand = new Random();

        public void feed() {
            int full_chance = rand.Next(1, 5);
            if (Meals > 0) {
                Meals -= 1;
                Status = "You used one meal.";
                if (full_chance == 1) {
                    int full = rand.Next(5, 11);
                    Fullness += full;
                    Status += ".. it gained " + full + " fullness!";
                }
                else {
                    Status = "Your Dachi did not like the meal!";
                }
            }
            else {
                Status = "Not enough meals to feed.";
            }
        }
        public void play() {
            int play_chance = rand.Next(1, 5);
            if(Energy >= 5) {
                Energy -= 5;
                Status = "Your Dachi used five energy.";
                if (play_chance == 1) {
                    int play = rand.Next(5, 11);
                    Happiness += play;
                    Status += ".. it gained " + play + " happiness!";
                }
                else {
                    Status = "Your Dachi does not feel like playing.";
                }
            }
            else {
                Status = "Your Dachi is too tired to play.";
            } 
        }
        public void work() {
            if (Energy >= 5) {
                Energy -= 5;
                int meal = rand.Next(1, 4);
                Meals += meal;
                Status = "Your Dachi lost five energy points, and gained " + meal + " meal(s)!";
            }
            else {
                Status = "Your Dachi is too tired to work.";
            }
        }
        public void sleep() {
            if (Fullness >= 5 && Happiness >= 5) {
                Energy += 15;
                Fullness -= 5;
                Happiness -= 5;
                Status = "Your Dachi lost five points to fullness and happiness, but gained fifteen points to energy!";
            }
            else if (Fullness < 5 && Happiness > 5) {
                Status = "Your Dachi needs to be fed before sleep!";
            }
            else if (Happiness < 5 && Fullness > 5) {
                Status = "Your Dachi is too sad to sleep!";
            }
            else {
                Status = "Your Dachi is too hungry and sad to sleep.";
            }
        }
    }
}