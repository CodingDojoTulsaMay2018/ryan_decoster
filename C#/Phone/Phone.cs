using System;

namespace phone {
        public abstract class Phone {
        private string _versionNumber;
        private int _batteryPercentage;
        private string _carrier;
        private string _ringTone;
        public Phone(string versionNumber, int batteryPercentage, string carrier, string ringTone){
            _versionNumber = versionNumber;
            _batteryPercentage = batteryPercentage;
            _carrier = carrier;
            _ringTone = ringTone;
        }
        public abstract void DisplayInfo();
        public string Version {
            get {
                return _versionNumber;
            }
            set {
                _versionNumber = value;
            }  
        }
        public int Battery {
            get {
                return _batteryPercentage;
            }
            set {
                _batteryPercentage = value;
            }
        }
        public string Carrier {
            get {
                return _carrier;
            }
            set {
                _carrier = value;
            }
        }
        public string RingT {
            get {
                return _ringTone;
            }
            set {
                _ringTone = value;
            }
        }
    }  
}