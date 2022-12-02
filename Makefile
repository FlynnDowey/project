all: nested-socket pru-copy 

nested-socket:
	make --directory=socket

pru-copy:
	mkdir -p $(HOME)/cmpt433/public/project/capture
	cp -r $(HOME)/cmpt433/work/myApps/project/capture/bash.sh $(HOME)/cmpt433/public/project/PI
	cp $(HOME)/cmpt433/work/myApps/project/socket/makeFifo_1.sh $(HOME)/cmpt433/public/project/PI
	cp $(HOME)/cmpt433/work/myApps/project/socket/makeFifo_2.sh $(HOME)/cmpt433/public/project/PI