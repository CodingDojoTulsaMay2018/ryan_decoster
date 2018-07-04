using System;
using System.Collections.Generic;

namespace phone {
    public class Nokia : Phone, IRingable 
    {
    public Nokia(string versionNumber, int batteryPercentage, string carrier, string ringTone) 
        :base(versionNumber, batteryPercentage, carrier, ringTone) {}
        public string Ring() 
        {   
            return "... "+RingT+" ...";
        }
        public string Unlock() 
        {
            return "Nokia " + Version + " unlocked with passcode.";
        }
        public override void DisplayInfo() 
        {
            System.Console.WriteLine("$$$$$$$$$$$$$$$$");
            System.Console.WriteLine("Nokia "+Version);     
            System.Console.WriteLine("Battery Percentage: "+Battery);
            System.Console.WriteLine("Carrier: "+Carrier);  
            System.Console.WriteLine("Ring Tone: "+RingT);
            System.Console.WriteLine("$$$$$$$$$$$$$$$$");
            System.Console.WriteLine("");
        }
    }
}   