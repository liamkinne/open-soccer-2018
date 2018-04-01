SOURCES := ${wildcard ../src/*.cpp}
OBJECTS := ${SOURCES:.cpp=.o}
ORANJE_FLAGS := -loranje -L../oranje/ -I../oranje/src/
PHANTOM_FLAGS := -lphantom -L../phantom-avr/ -I../phantom-avr/

# Chip specific
F_CPU := 16000000
MMCU := atmega328p

all: $(SOURCES)
	rm -rf ../build/*
	mkdir -p ../build
	make -fAVR.mk --directory=../oranje MMCU=$(MMCU) F_CPU=$(F_CPU)
	avr-g++ $^ -o ../build/main.out $(ORANJE_FLAGS) $(PHANTOM_FLAGS) -Wall -Wextra -std=c++14 -O3 -mmcu=$(MMCU) -DF_CPU=$(F_CPU)
	avr-objcopy -j .text -j .data -O ihex ../build/main.out ../build/main.hex
	avrdude -c arduino -b 57600 -P /dev/ttyUSB0 -p $(MMCU) -vv -U flash:w:../build/main.hex
