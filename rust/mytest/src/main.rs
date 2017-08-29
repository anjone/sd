extern crate primal;
use primal::Sieve;

fn main() {
    println!("Hello, world!");
    let sieve = Sieve::new(10000);
    let n = 1000;
    match sieve.primes_from(0).nth(n - 1){
        Some(number) => println!("{}th prime is {}", n, number),
        None => println!("I don't know anything about {}th prime.", n),
    }
}
