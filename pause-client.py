from microbit import *
import radio

radio.on()
radio_on = True

while True:
    if button_a.was_pressed():
        radio.on()
        radio.send("A")
        display.scroll("vvv", delay=40, wait=False)
        radio.off()
        radio_on = False
 
    if button_b.was_pressed():
        radio.on()
        radio.send("B")
        display.scroll("vvv", delay=40, wait=False)
        radio.off()
        radio_on = False
        
    if radio_on:
        received = radio.receive()
        if received:
            print(received)
            display.scroll(received, delay=40, wait=False)
