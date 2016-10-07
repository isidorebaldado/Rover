import time                                                                     
from itertools import cycle                                                     
from flask import Flask, render_template                                        
#from robot_brain.gpio_pin import GPIOPin
import RPi.GPIO as GPIO

app = Flask(__name__)                                                           
'''
on_pin = GPIOPout(18)                                                            
off_pin = GPIOPin(23)                                                           
'''

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


state_cycle = cycle(['on', 'off'])

@app.route("/")
@app.route("/<state>")
def update_lamp(state=None):
    '''
    if state == 'on':                                                           
        on_pin.set(1)                                                           
        time.sleep(.2)                                                          
        on_pin.set(0)                                                           
    if state == 'off':                                                          
        off_pin.set(1)                                                          
        time.sleep(.2)                                                          
        off_pin.set(0)                                                          
    if state == 'toggle':                                                       
        state = next(state_cycle)                                               
        update_lamp(state)        
    '''
    if state == 'on':                                                           
        GPIO.output(18, 1)
        GPIO.output(27, 1)
        GPIO.output(22, 1)
    if state == 'off':                                                          
        GPIO.output(18, 0)
        GPIO.output(27, 0)
        GPIO.output(22, 0)                                                            
    if state == 'toggle':                                                       
        state = next(state_cycle)                                               
        update_lamp(state) 
    template_data = {                                                           
        'title' : state,                                                        
    }                                                                           
    return render_template('main.html', **template_data)

if __name__ == "__main__":                                                      
    app.run(host='0.0.0.0', port=80)
