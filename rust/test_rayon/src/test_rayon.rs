extern crate rayon;
use rayon::prelude::*;

fn sum_of_squares(input: &[i32]) -> i32 {
    input.par_iter().map(|&i| i * i).sum()
}

fn main() {
    let rand_val = 10;
    let sum_sq = sum_of_squares(&[rand_val]);
    println!("Sum of squares of {0} is {1}", rand_val, sum_sq);    
}