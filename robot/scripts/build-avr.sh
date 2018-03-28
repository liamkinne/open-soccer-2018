# Seup build directory
mkdir ../build

make -f ../phantom-avr/Makefile --directory=../phantom-avr

make -f ../scripts/Makefile --directory=../oranje/ P_LIB=../phantom-avr/
