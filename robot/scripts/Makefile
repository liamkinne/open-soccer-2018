NAME = oranje
SOURCES := ${wildcard src/*.cpp} ${wildcard src/Drive/*.cpp}
OBJECTS := ${SOURCES:.cpp=.o}

%.o: %.cpp
	@avr-g++ -c -o $@ $< -Wall -Wextra -std=c++14 -O3 -I./src/ -mmcu=$(MMCU) -DF_CPU=$(F_CPU) -L$(P_LIB) -lphantom -I$(P_LIB) -L$(P_LIB)std/ -lstd -I$(P_LIB)std/

all: $(OBJECTS)
	@echo "Building library"
	avr-ar rcsv lib$(NAME).a $^
