# Interopera

This is the manual to run the interopera Project follow the steps bellow to install all the depencies and packages. 
Note that this project is only compatible with the linux environment.

## Software requirements

+ Run the command 'make install_python' in the terminal to install python and setting its path;
+ Run the command 'make install_java' in the terminal to install java and setting its path;
+ Run the command 'make install_programs'  in the terminal to install all the programs that this project will use;
+ Run the command 'make install_sigma'  in the terminal to install all the sigma dependencies;
+ Re-open the terminal to ensure that the paths have been set;
+ Run the command 'make configure_sigma'  in the terminal to make tha last configurations on sigma;
+ Run the command 'make install'  in the terminal to install all of this project dependencies;
+ If you want to run the interface or the example you will need to run the 'make install_node' as well to install node and its path;

## How to run the project
+ To run this project go to the interopera folder;
+ Run the command 'java -Xmx7g -cp $SIGMA_SRC/build/classes:$SIGMA_SRC/build/lib/* com.articulate.sigma.KBmanager -p';
+ Open another terminal and Run the command 'python controler -args';
+ The args to run this project can be found in the help file;

## How to run the interface
+ To run the interface go to the interface folder;
+ Run the command 'npm install' or 'yarn install';
+ Run the command 'npm dev' or 'yarn dev';

## How to run the example of the interface
+ To run the example go to the example folder;
+ Run the command 'npm install' or 'yarn install';
+ Run the command 'npm dev' or 'yarn dev';

# Common issues

+ If you have problems running the make command you need to install it with the command 'sudo apt-get install make';
+ If you are having problems running the Java command go to the root folder and run the command 'make install_vampire' and try again;