import pygame

# Initialize pygame
pygame.init()
pygame.joystick.init()

# Check for connected joysticks
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No joystick detected.")
    quit()

# Initialize the joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

print("Initialized joystick: {}".format(joystick.get_name()))

# Main loop to read joystick events
try:
    while True:
        pygame.event.get()  # Get the events
        for i in range(joystick.get_numaxes()):
            axis_value = joystick.get_axis(i)
            print("Axis {}: {:.2f}".format(i, axis_value))
        
        for i in range(joystick.get_numbuttons()):
            button_state = joystick.get_button(i)
            print("Button {}: {}".format(i, button_state))

        pygame.time.wait(100)  # Wait for 100 milliseconds to reduce CPU load

except KeyboardInterrupt:
    print("Program terminated by user.")
    pygame.quit()