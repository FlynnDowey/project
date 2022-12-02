# Makefile for building embedded application.
# by Brian Fraser

# Edit this file to compile extra C files into their own programs.
TARGETS = main
SOURCES_C = main.c
SOURCES_CPP = fred.cpp

PUBDIR = $(HOME)/cmpt433/public/myApps

OUTDIR = $(PUBDIR)
CROSS_TOOL = 
CC_CPP = $(CROSS_TOOL)g++
CC_C = $(CROSS_TOOL)gcc

CFLAGS = -Wall -g -std=c99 -D _POSIX_C_SOURCE=200809L -Werror -Wshadow
CPPFLAGS = -Wall -g -std=c++11 -Werror -Wshadow
# -pg for supporting gprof profiling.
# CFLAGS += -pg

all: $(TARGETS)

$(TARGETS):
	$(CC_CPP) $(CPPFLAGS) $(SOURCES_CPP) $(SOURCES_C) -o $(OUTDIR)/$(TARGETS)
