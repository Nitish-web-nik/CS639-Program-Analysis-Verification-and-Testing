## Assignment 1 Program Analysis Verification and Testing

The location of my 5 good examples is at \Chiron-Framework\KachuaCore\example in '.tl' format.

To run the program in Windows x64 based system,

We have to do the following steps:-

Run the following command in cmd (directory for cmd should be inside KachuaCore): 

python ./kachua.py -r -t 60 -d {':x':30,':y':3,':z':7} --fuzz tests/<example name>.tl

For bash:
./kachua.py -r -t 60 -d {':x':0,':y':89,':z':69} --fuzz tests/<example name>.tl

The input value totally depends on the user that he/she wants to enter in order to run the examples.

