# Motor-propeller-thrust-calculator

# screenshot added describes the setup, and what to measure

Thrust can be calculated using ballistic pendulum.

However, one needs to preserve the center of the mass of the pendulum (symmetry!).

the general formula is:

# Thrust [N] = tan(∆)*Gravity_force [N]


gravity force: just get a scale, and take the mass in grams. Scale division is the smallest mass you can measure.

∆ is the angle (smaller than 90 deg) of pendulum displacement. just like in optics - the angle between steady state and displaced state of wire holding pendulum (like between normal vector & reflected light).

for best accuracy, ∆ should be less than 40 deg. it is inside tan() function.

here i provide kivy app (crude), that uses this formula with uncertainties.

also, theres pc pyqt app with uncertanties support.

the uncertainties can be systematic only, but if you obtain experimentally statistical uncertainty/ies, then join them with the formula (provided here for noobs in experimental physics):

# Joined_U = np.sqrt(U_systematic^2 + U_statistical^2)

if you wanna perform experiments in series to obtain an average thrust, then join the results using weighted average (where weight = 1/(total_uncertainty^2)).

![Screenshot_20240602-211129](https://github.com/tk0987/Engine-propeller-thrust-calculator/assets/109526789/a81ee7b7-0253-4076-b862-0830c1a61d5e)
