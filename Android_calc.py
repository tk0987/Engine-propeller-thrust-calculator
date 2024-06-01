from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import numpy as np

class MainApp(App):
    
    def build(self):
        self.main1_layout= BoxLayout(orientation='vertical')
        self.main_layout = GridLayout(cols=2, spacing=[50, 50])
        
        # Create TextInput for mass and angle
        self.mass_input = TextInput(multiline=False, readonly=False, halign="center", font_size=55)
        self.angle_input = TextInput(multiline=False, readonly=False, halign="center", font_size=55)
        
        # Create Labels for mass and angle
        self.massLabel = Label(text='Mass [g]:')
        self.angleLabel = Label(text='Angle [deg]:' )
        
        # Add Labels and TextInputs to the layout
        self.main_layout.add_widget(self.massLabel)
        self.main_layout.add_widget(self.mass_input)
        self.main_layout.add_widget(self.angleLabel)
        self.main_layout.add_widget(self.angle_input)
        self.main1_layout.add_widget(self.main_layout)
        self.solution1= Label(text=" ")
        # Create a Compute button
        self.button = Button(text="Compute", size_hint=(1, .5))
        self.button.bind(on_press=self.on_button_press)
        self.main1_layout.add_widget(self.solution1)
        self.main1_layout.add_widget(self.button)
        
        # Create a Label to display the solution
        self.solution = Label(text=".")
        self.main1_layout.add_widget(self.solution)
        
        return self.main1_layout

    def on_button_press(self, instance):
        try:
            # Convert inputs to float
            deg = float(self.angle_input.text)
            mass_g = float(self.mass_input.text)
            
            # Perform calculations
            angle_rad = deg / 180 * np.pi
            force_g = mass_g * 9.81 / 1000.0  # Assuming g = 9.81 m/s^2
            thrust = np.tan(angle_rad) * force_g
            
            # Update the label's text to the string representation of thrust
            self.solution.text = f'Thrust: {thrust:.4f} [N]'  # Formatting for better readability
        except ValueError:
            self.solution.text = 'Invalid input!\nPlease enter numeric\nvalues.'

if __name__ == "__main__":
    app = MainApp()
    app.run()
