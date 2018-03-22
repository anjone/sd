package com.upi.playboot2;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Playboot2Application implements CommandLineRunner {

	public static void main(String[] args) {
		SpringApplication.run(Playboot2Application.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		System.out.println("Playing...");
	}
}
