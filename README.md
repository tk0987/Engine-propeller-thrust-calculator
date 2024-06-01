# Engine-propeller-thrust-calculator

Thrust can be calculated using ballistic pendulum.

However, one needs to preserve the center of the pendulum mass (symmetry!).

the general formula is:
###
Thrust [N] = tan(∆)*Gravity_force [N]
###

gravity force: just get a scale, and take the mass in grams. 

∆ is the angle (smaller than 90 deg) of pendulum displacement. just like in optics.

for best accuracy, ∆ should be less than 40 deg. it is inside tan() function.

here i provide kivy app (crude), that uses this formula.

in future - pc pyqt app with uncertanties support.
