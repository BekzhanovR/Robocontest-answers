use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    
    let numbers: Vec<i32> = input
        .split_whitespace()
        .map(|s| s.parse().expect("Failed to parse integer"))
        .collect();

    let a = numbers[0];
    let b = numbers[1];

    let x = if a > b { ">" } else if a == b { "=" } else { "<" };
    println!("{}", x);
}
