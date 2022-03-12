from time import sleep
import pibrella
import random

time = random.uniform(5,10)
sleep(time)
pibrella.light.green.on()

while True:
    p1 = pibrella.input.a.read()
    p2 = pibrella.button.read()
    if p1 == 1:
        pibrella.light.yellow.blink(0.5,0.5)
        sleep(5)
        break
    if p2 == 1:
        pibrella.light.red.blink(0.5,0.5)
        sleep(5)
        break
pibrella.buzzer.success()
sleep(2)
pibrella.lights.off()

