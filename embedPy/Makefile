# Makefile for building embedded application.
# by Brian Fraser

# Edit this file to compile extra C files into their own programs.
TARGETS= captureDriver


PUBDIR = .
OUTDIR = $(PUBDIR)
CROSS_TOOL = arm-linux-gnueabihf-
CC_CPP = $(CROSS_TOOL)g++
CC_C = $(CROSS_TOOL)gcc

CFLAGS = -I/usr/include/python3.9 -I/usr/include/python3.9  -Wno-unused-result -Wsign-compare -g -ffile-prefix-map=/python3.9-3.9.2=. -specs=/usr/share/dpkg/no-pie-compile.specs -fstack-protector -Wformat -Werror=format-security  -DNDEBUG -g -fwrapv -O3 -Wall
LDFLAGS = -L/usr/lib/python3.9/config-3.9-arm-linux-gnueabihf -L/usr/lib  -lcrypt -lpthread -ldl  -lutil -lm -lpython3.9

# Convert the targets to full-path executables to delete.
OUTPUTS= $(addprefix $(OUTDIR)/, $(TARGETS))

all: $(TARGETS)

$(TARGETS):
	$(CC_C) $(CFLAGS) $@.c -o $(OUTDIR)/$@ $(LDFLAGS)


clean:
	rm -f $(OUTPUTS)