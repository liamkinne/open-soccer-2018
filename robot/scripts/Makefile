SOURCES := ${wildcard ../src/*.cpp}
OBJECTS := ${SOURCES:.cpp=.o}
ORANJE_FLAGS := -L../oranje/ -loranje -I../oranje/src/
PHANTOM_FLAGS := -L../phantom-avr/ -lphantom -I../phantom-avr/

# Chip specific
F_CPU := 16000000
MMCU := atmega328p

all: $(SOURCES)
	make -fAVR.mk --directory=../oranje MMCU=$(MMCU) F_CPU=$(F_CPU)
	avr-g++ $^ -o ../build/main.out $(ORANJE_FLAGS) $(PHANTOM_FLAGS) -Wall -Wextra -std=c++14 -O3 -mmcu=atmega328p -DF_CPU=16000000

