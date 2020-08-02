COMPILER=g++
FLAGS=-Wall -g -std=c++11

all: main

main: main.o random.o
	${COMPILER} ${FLAGS} $^ -o $@

main.o: main.cc random.h
	${COMPILER} ${FLAGS} -c $< -o $@

random.o: random.cc random.h
	${COMPILER} ${FLAGS} -c $< -o $@

clean:
	rm -rf *.o