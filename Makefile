CXX=clang++
RM=rm -f
CPPFLAGS=-Wall -Wextra -pedantic -std=c++17

timestamp: timestamp.o
	$(CXX) -o timestamp timestamp.o

timestamp.o: timestamp.cpp
	$(CXX) $(CPPFLAGS) -c timestamp.cpp

clean:
	$(RM) timestamp.o timestamp

