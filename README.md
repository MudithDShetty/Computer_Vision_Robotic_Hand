# Computer Vision Assisted Robotic Hand
This Computer Vision controlled mechanical arm was built as a project for a competition called 'Polarizer'. We used the library of OpenCV and Mediapipe to recognize the hand. Rest of the coding is done on python and Arduino.
Some of the photos are not origanally mine credit to the people for said photos.

# A MINI-PROJECT REPORT
Physics - IV 
“Computer  Vision Supported Robotic Hand”

# Robotic Hand
Introduction
 robotic arms are helping businesses boost their competitive advantage and keep costs low by enabling automation of key processes that contribute to enhanced safety for workers, accelerated production, and improved productivity. a robotic arm required teaching to perform narrowly defined tasks, such as picking a single type of object from a precise location with a specific orientation. Robots were not able to identify a particular type of object among many, determine an object location with some tolerance (area rather than exact position), or adjust the grasp based on object orientation.

1. Businesses can realize several benefits from industrial robotic arms:
2. Improved safety. Robotic arms help keep workers safe by operating in environments that are hazardous and executing tasks that present high risk of injury to humans.
3. Improved efficiency and productivity. Robotic arms can operate 24 hours a day, seven days a week without fatiguing, allowing businesses to keep production, inspections, or other tasks going continuously to increase output.
4. Enhanced precision. By their very nature, robotic arms perform more consistently and accurately than humans for tasks that require extreme precision or consistency.
5. Greater flexibility. As business priorities change, robotic arms can easily be repurposed for new activities or mounted onto different platforms, such as autonomous mobile robots (AMRs), a stationary assembly line platform, or wall or shelf, as needed.
6. One of the key advantages of industrial robotic arms is their versatility for supporting multiple applications—from the simplest to the most complex jobs in the safest or harshest environments. Automating these types of tasks not only removes human workers from possibly hazardous situations, but it enables those workers to take on high-value tasks such as interfacing with customers.


# Theory
Force of tension

Tension is defined as the force transmitted through a rope, string or wire when pulled by forces acting from opposite sides. The tension force is directed over the length of the wire and pulls energy equally on the bodies at the ends.

Tension is the opposite of compression force. All the objects that are present in contact with each other exert a force on each other. The best example of a tension force can be seen while pulling a rope. When a pull force is applied to the rope, a significant amount of tension gets built.

Ex. Force tension with a rope:
For instance, if a person pulls a massless rope with a force of 20 N, the block also experiences a force of 20 N. All massless ropes experience two opposite and equal tension forces. Here, the person pulling a block with a rope, rope experiences a net force.
![image](https://github.com/MudithDShetty/Computer_Vision_Robotic_Hand/assets/128790888/e25a78a2-45fa-4e6f-aa31-3bdecca5e770)

Formula:
T= mg + ma
We know that the force of tension is calculated using the formula T = mg + ma.
![image](https://github.com/MudithDShetty/Computer_Vision_Robotic_Hand/assets/128790888/a0aff258-d019-4874-9050-582c1e25ec87)


 # Semiconductor

Semiconductors are the materials which have a conductivity between conductors  and non-conductors or insulators. Semiconductors can be compounds such as gallium arsenide or pure elements, such as germanium or silicon.
semiconductor, any of a class of crystalline solids intermediate in electrical conductivity between a conductor and an insulator. Semiconductors are employed in the manufacture of various kinds of electronic devices, including diodes, transistors, and integrated circuits
![image](https://github.com/MudithDShetty/Computer_Vision_Robotic_Hand/assets/128790888/be392f87-c04d-4528-9747-c0fb67ffd629)


Property 1:The resistivity of a semiconductor is less than an insulator but higher than a conductor.
Property 2: Semiconductors show a negative temperature coefficient of resistance. 
Property 3: At zero kelvin, semiconductors behave as insulators.
Property 4: The conductivity of the semiconductors increases when impurities are added. The process of adding impurities to semiconductors is called doping.

# Components Used:
1.Arduino UNO

![image](https://github.com/MudithDShetty/Computer_Vision_Robotic_Hand/assets/128790888/658b92bf-abf1-4aea-8c2b-aae08f0b1d10)

Arduino UNO is a microcontroller board based on the ATmega328P. It has 14 digital input/output pins (of which 6 can be used as PWM outputs), 6 analog inputs, a 16 MHz ceramic resonator, a USB connection, a power jack, an ICSP header and a reset button.

2. Male to male jumper wires
   
![image](https://github.com/MudithDShetty/Computer_Vision_Robotic_Hand/assets/128790888/949321cb-437b-4ce0-8010-5587c7c01e6b)

This cable is an electrical wire or group of them in a cable with a connector or pins at each end, which is normally for interconnecting the components of a breadboard or other prototype or test circuit, internally or with other equipment or components, without soldering.

4. Cardboard
   
![image](https://github.com/MudithDShetty/Computer_Vision_Robotic_Hand/assets/128790888/5f4873d2-8df4-4a46-a295-d42f2899b1c3)

We have used the cardboard for covering the body of the hand and the wirings


4. SG90 9G Micro Servo Motor
   
![image](https://github.com/MudithDShetty/Computer_Vision_Robotic_Hand/assets/128790888/a481c0bc-c568-4ac7-955f-9212c4af3135)

Micro Servo Motor SG90 is a tiny and lightweight server motor with high output power. Servo can rotate approximately 180 degrees (90 in each direction), and works just like the standard kinds but smaller. You can use any servo code, hardware or library to control these servos.

5. 1 Feet USB A to USB B Cable
   
![image](https://github.com/MudithDShetty/Computer_Vision_Robotic_Hand/assets/128790888/19a356c9-b0ae-4a1a-a396-9ee8e0cea43f)

We have used this cable to directly connect the robotic hand to the laptop

7.  Tie tags
   
![image](https://github.com/MudithDShetty/Computer_Vision_Robotic_Hand/assets/128790888/25cf4bdc-0288-4149-bd9d-ab3ee6b4a010)

We have used this to make the movements of the fingers to go up and down. It works like flex muscles.

# Construction and Working:

![image](https://github.com/MudithDShetty/Computer_Vision_Robotic_Hand/assets/128790888/c1fffaf2-68ff-4dce-b768-93b9e7243b56)

The Robotic hand is made out of cardboard cut outs , of three divisions, the palm, the wrist and the fingers. The Servo Motors are embedded in the palm cutout, which leads to the back that connects the wires in the breadboard that is stuck to the wrist cutout, which is then connected to an Arduino UNO.
The wiring is as follows:

![image](https://github.com/MudithDShetty/Computer_Vision_Robotic_Hand/assets/128790888/c41bfc72-1b1d-4663-a56f-c2093047d75e)

This wiring with the help of the arduino code instructs the motors to turn in a angle of 135 degrees . 
The servo motor is used here as we can have more control over the angle in which the motor rotates
The rotator of the servo motor is attached to the tie tags and cutouts of the fingers when the rotator rotates it puls on the tie tags which forces the cuts in the finger to fold and the fingers are able to grab it.
The model of the fingers is as follows , we used tie tags for elasticity instead of the springs we decided for the prototype:
![image](https://github.com/MudithDShetty/Computer_Vision_Robotic_Hand/assets/128790888/cf9d181f-c15f-4f19-97b6-4a0346181ac4)

The final part of the model is the hand tracking program itself ,It was mostly made in Python 3.10, we used the opencv and mediapipe libaries for the hand tracking , mediapipe allowed us to use preassigned landmarks for the hand which made it easier and also we used opencv for the camera facility.
With some extra code in python and if else statements the program could recognize which fingers were up and which fingers were down .

![image](https://github.com/MudithDShetty/Computer_Vision_Robotic_Hand/assets/128790888/2a6e30e1-a82d-4fb2-9013-245d9a787b82)

It then encode it and send it to the arduino code using the Serial Library which processed it and gave the instructions to the servo motors to move.

![image](https://github.com/MudithDShetty/Computer_Vision_Robotic_Hand/assets/128790888/ff840a98-3f22-4f4d-b771-2585735ac7c3)

# Images of the model
1.Front Face Model

![image](https://github.com/MudithDShetty/Computer_Vision_Robotic_Hand/assets/128790888/80e33484-6268-49c3-ae70-53225c0d1b7d)

2. Internal wiring of  hand image
   
![image](https://github.com/MudithDShetty/Computer_Vision_Robotic_Hand/assets/128790888/cdfced07-55dc-4515-ae7e-93287615e01a)


# Reference links: 
https://www.nature.com/articles/s41467-021-27261-0
https://www.tertiaryrobotics.com/micro-servo-motor-sg90.html
https://www.datapro.net/products/usb-2-0-a-to-b-device-cable.html
https://byjus.com/physics/tension-force/
https://www.techtarget.com/whatis/definition/semiconductor
https://google.github.io/mediapipe/#:~:text=MediaPipe%20offers%20cross%2Dplatform%2C%20customizable,desktop%2Fcloud%2C%20web%20and%20IoT
https://opencv.org/
https://miro.medium.com/max/1200/1*WhYiJkSaqJAMEloRIiWHTQ.png




