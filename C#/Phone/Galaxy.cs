using System;
using System.Collections.Generic;

namespace phone {
    public class Galaxy : Phone, IRingable 
    {
        public Galaxy(string versionNumber, int batteryPercentage, string carrier, string ringTone) 
            : base(versionNumber, batteryPercentage, carrier, ringTone) {}
        public string Ring() 
        {
            return "... "+RingT+" ...";
        }
        
        public string Unlock() 
        {
            return "Galaxy " + Version + " unlocked with fingerprint scanner.";
        }
        public override void DisplayInfo() 
        {
            System.Console.WriteLine("###############");
            System.Console.WriteLine("Galaxy "+Version);     
            System.Console.WriteLine("Battery Percentage: "+Battery);
            System.Console.WriteLine("Carrier: "+Carrier);  
            System.Console.WriteLine("Ring Tone: "+RingT);
            System.Console.WriteLine("###############");
            System.Console.WriteLine("");     
        }
    }
}