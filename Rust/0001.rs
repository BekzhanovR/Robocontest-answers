use std::io;

fn main() {
    let mut input = String::new();

    io::stdin().read_line(&mut input).expect("Failed to read input");

    let numbers: Vec<i32> = input
        .split_whitespace()
        .map(|x| x.parse().expect("Failed to parse input"))
        .collect();

    let sum = numbers.iter().sum::<i32>();

    println!("{}", sum);
}