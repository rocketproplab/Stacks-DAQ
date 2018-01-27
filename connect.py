import subinitial.stacks as stacks

core = stacks.Core(host="192.168.1.49")

analogdeck = stacks.AnalogDeck(core, bus_address=2)

# Change leds for no reason
while:




# Set the RGBs to green when done "initializing"
core.rgbled.set(core.rgbled.COLOR_GREEN)
analogdeck.rgbled.set(analogdeck.rgbled.COLOR_GREEN)


while 1:

    # Read input from user
    input = readline()

    switch(input[1]):
        case 0:
            analogdeck.solenoiddrivers.engage(input)

        case 1:

        case 2:

        case 3:
