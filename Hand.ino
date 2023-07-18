#include <Servo.h>
   Servo Pinky; 
   Servo Ring;
   Servo Middle;
   Servo Index;
   Servo Thumb;
   char val;
void setup() {
  Serial.begin(9600);
  Pinky.attach(9,600,2300);
  Ring.attach(8,600,2300);
  Middle.attach(7,600,2300);
  Index.attach(6,600,2300);
  Thumb.attach(5,600,2300);
  Pinky.write(0); 
}

void loop() {
  while(Serial.available()>0){
    val= Serial.read();
    Serial.print(val);
    if(val=='a'){
      Pinky.write(150); 
      Ring.write(150);
      Middle.write(150);
      Index.write(150);
      Thumb.write(150); 
    }
    if(val=='b'){
      Pinky.write(135); 
      Ring.write(135);
      Middle.write(135);
      Index.write(135);
      Thumb.write(0); 
    }
    else if(val=='c'){
      Pinky.write(135); 
      Ring.write(135);
      Middle.write(135);
      Index.write(0);
      Thumb.write(180); 
    }
    else if(val=='d'){
      Pinky.write(135); 
      Ring.write(135);
      Middle.write(135);
      Index.write(0);
      Thumb.write(0); 
    }
    else if(val=='e'){
      Pinky.write(135); 
      Ring.write(135);
      Middle.write(0);
      Index.write(135);
      Thumb.write(180); 
    }  
    else if(val=='f'){
      Pinky.write(135); 
      Ring.write(135);
      Middle.write(0);
      Index.write(135);
      Thumb.write(0); 
    }   
    else if(val=='g'){
      Pinky.write(135); 
      Ring.write(135);
      Middle.write(0);
      Index.write(0);
      Thumb.write(180); 
    }   
    else if(val=='h'){
      Pinky.write(135); 
      Ring.write(135);
      Middle.write(0);
      Index.write(0);
      Thumb.write(0); 
    }   
    else if(val=='i'){
      Pinky.write(135); 
      Ring.write(0);
      Middle.write(135);
      Index.write(135);
      Thumb.write(180); 
    }     
    else if(val=='j'){
      Pinky.write(135); 
      Ring.write(0);
      Middle.write(135);
      Index.write(135);
      Thumb.write(180);
    }
    else if(val=='k'){
      Pinky.write(135); 
      Ring.write(0);
      Middle.write(135);
      Index.write(0);
      Thumb.write(180); 
    }
    else if(val=='l'){
      Pinky.write(135); 
      Ring.write(0);
      Middle.write(135);
      Index.write(0);
      Thumb.write(0);
    } 
    else if(val=='m'){
      Pinky.write(135); 
      Ring.write(0);
      Middle.write(0);
      Index.write(135);
      Thumb.write(180); 
    }
    else if(val=='n'){
      Pinky.write(135); 
      Ring.write(0);
      Middle.write(0);
      Index.write(135);
      Thumb.write(0); 
    }
    else if(val=='o'){
      Pinky.write(135); 
      Ring.write(0);
      Middle.write(0);
      Index.write(0);
      Thumb.write(180); 
    }
    else if(val=='p'){
      Pinky.write(135); 
      Ring.write(0);
      Middle.write(0);
      Index.write(0);
      Thumb.write(0);
    } 
    else if(val=='q'){
      Pinky.write(0); 
      Ring.write(135);
      Middle.write(135);
      Index.write(135);
      Thumb.write(180); 
    } 
    else if(val=='r'){
      Pinky.write(0); 
      Ring.write(135);
      Middle.write(135);
      Index.write(135);
      Thumb.write(0); 
    }
    else if(val=='s'){
      Pinky.write(0); 
      Ring.write(135);
      Middle.write(135);
      Index.write(0);
      Thumb.write(180); 
    }
    else if(val=='t'){
      Pinky.write(0); 
      Ring.write(135);
      Middle.write(135);
      Index.write(0);
      Thumb.write(0); 
    }
    else if(val=='u'){
      Pinky.write(0); 
      Ring.write(135);
      Middle.write(0);
      Index.write(135);
      Thumb.write(180); 
    } 
    else if(val=='v'){
      Pinky.write(0); 
      Ring.write(135);
      Middle.write(0);
      Index.write(135);
      Thumb.write(0); 
    } 
    else if(val=='w'){
      Pinky.write(0); 
      Ring.write(135);
      Middle.write(0);
      Index.write(0);
      Thumb.write(180); 
    } 
    else if(val=='x'){
      Pinky.write(0); 
      Ring.write(135);
      Middle.write(0);
      Index.write(0);
      Thumb.write(0); 
    } 
    else if(val=='y'){
      Pinky.write(0); 
      Ring.write(0);
      Middle.write(135);
      Index.write(135);
      Thumb.write(180); 
    } 
    else if(val=='z'){
      Pinky.write(0); 
      Ring.write(0);
      Middle.write(135);
      Index.write(135);
      Thumb.write(0); 
    } 
    else if(val=='&'){
      Pinky.write(0); 
      Ring.write(0);
      Middle.write(135);
      Index.write(0);
      Thumb.write(180); 
    } 
    else if(val=='$'){
      Pinky.write(0); 
      Ring.write(0);
      Middle.write(135);
      Index.write(0);
      Thumb.write(0); 
    } 
    else if(val=='%'){
      Pinky.write(0); 
      Ring.write(0);
      Middle.write(0);
      Index.write(135);
      Thumb.write(180); 
    } 
     else if(val=='*'){
      Pinky.write(0); 
      Ring.write(0);
      Middle.write(0);
      Index.write(135);
      Thumb.write(0); 
    } 
     else if(val=='#'){
      Pinky.write(0); 
      Ring.write(0);
      Middle.write(0);
      Index.write(0);
      Thumb.write(180); 
    } 
    
    else if(val=='!'){
      Pinky.write(0); 
      Ring.write(0);
      Middle.write(0);
      Index.write(0);
      Thumb.write(0); 
    }
  }
}