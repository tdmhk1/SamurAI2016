CPPFLAGS= -std=c++11 -g
CPP= c++

COMMONOBJECTS= players.o
PLANNINGOBJECTS= planning.o
GREEDYOBJECTS= ${COMMONOBJECTS} ${PLANNINGOBJECTS} greedyPlayer.o
TARGET= greedyPlayer

all: ${TARGET}

greedyPlayer: ${GREEDYOBJECTS}
	${CPP} ${CPPFLAGS} -o $@ $^

-include ${OBJECTS:.o=.d}

%.o: %.cpp
	${CPP} -c ${CPPFLAGS} $*.cpp -o $*.o
	${CPP} -MM ${CPPFLAGS} $*.cpp > $*.d

clean:
	rm -f ${TARGET}
	rm -f *.o *.d
	rm -rf *~ */*~ \#*\#
