use std::fs::File;
use std::i32::MIN;
use std::io::{BufRead, BufReader, Lines, Result};
use std::path::Path;

fn main() {
    let mut max = MIN;
    if let Ok(lines) = read_lines("../input.txt") {
        let mut current_elves_calories = 0;
        for line in lines {
            if let Ok(food_cal) = line {
                if food_cal.is_empty() {
                    if current_elves_calories > max {
                        max = current_elves_calories;
                        current_elves_calories = 0;
                    }
                } else {
                    current_elves_calories += food_cal.parse::<i32>().unwrap();
                }
            }
        }
    }
    println!("{}", max);
}

fn read_lines<P>(filename: P) -> Result<Lines<BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename).ok().unwrap();
    Ok(BufReader::new(file).lines())
}
