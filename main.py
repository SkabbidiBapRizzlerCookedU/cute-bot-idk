basic.show_leds("""
    . . . # .
    # . # . #
    # . # . #
    # . # . #
    . # . . .
    """)
strip = neopixel.create(DigitalPin.P15, 24, NeoPixelMode.RGB)
strip.show_rainbow(1, 360)
basic.show_icon(IconNames.HAPPY)

def on_forever():
    strip.rotate(1)
    basic.pause(100)
    strip.show()
basic.forever(on_forever)

def on_forever2():
    cuteBot.motors(30, 90)
    basic.pause(1500)
    cuteBot.motors(90, 30)
    basic.pause(1500)
basic.forever(on_forever2)
