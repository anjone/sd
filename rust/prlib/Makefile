all: run

build:
	cargo build --release
	cp ./target/release/libprlib.so ./prlib.so

run: build
	python test.py

clean:
	cargo clean
	rm ./prlib.so