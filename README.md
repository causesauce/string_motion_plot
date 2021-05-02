# string_motion_plot
The following code is written in Python using Matplotlib and native python. It shows a plot of the string motion and a plot of Potential, Kinetic and Total energies of a string with the given length using following formulas:

![image](https://user-images.githubusercontent.com/67865361/116825510-f0967f80-ab8f-11eb-8515-f3d780ad95e2.png)


![image](https://user-images.githubusercontent.com/67865361/116825535-0b68f400-ab90-11eb-8134-364601c5f1a1.png)

For better approximation we solve differential equations using Mid Point method aka 'improved Euler method'



-----------

For input values like:
# length
L = m.pi

# number of points
n = 17

# delta x
dx = L / n

# delta t (time difference)
dt = 0.2

# simple string oscillation function
sin = m.sin


the output looks like that:


String motion plot:


![image](https://user-images.githubusercontent.com/67865361/116827769-107f7080-ab9b-11eb-9343-017f80f5a1fb.png)

Potential, Kinetic, Total energies:

![image](https://user-images.githubusercontent.com/67865361/116827777-1c6b3280-ab9b-11eb-9f30-b365100c36c7.png)

