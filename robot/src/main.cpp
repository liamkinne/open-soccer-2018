#include <PWMOutput.h>
#include <DigitalOutput.h>
#include <L298.h>
#include <Boards/ArduinoUno.h>
#include <util/delay.h>

using namespace Phantom;

Oranje::L298 motor(new PWMOutput(new Pin(3)), new DigitalOutput(new Pin(2)), new DigitalOutput(new Pin(4)));

int main(void)
{
	while (true) {
		motor.set(0.75);
		_delay_ms(1000);
		motor.set(-0.75);
		_delay_ms(1000);
	}	
}
