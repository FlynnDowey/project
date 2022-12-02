SOURCES = main.c
TARGET = main


PUBDIR = $(HOME)/cmpt433/public/project
OUTDIR = $(PUBDIR)

CC_C_HOST = arm-linux-gnueabihf-gcc
CFLAGS = -g -std=c99 -Werror 


all: 
	$(CC_C_HOST) $(CFLAGS) $(SOURCES) -o $(OUTDIR)/$(TARGET) 
clean:
	rm -f $(OUTDIR)/$(TARGET)
