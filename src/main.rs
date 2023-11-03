mod days;
mod util;

use clap::Parser;
use days::*;

fn main() {
    let args = util::Cli::parse();
    if let Some(day) = args.run {
        println!("~~~~~~~~~~~~~~~~~~~~~~~");
        println!("Solving day: {}", day);
        match day {
            1 => days_1::solve(),
            2 => days_2::solve(),
            _ => println!("Solution for day {} does not exist.", day),
        }
        println!("~~~~~~~~~~~~~~~~~~~~~~~");
    }
    if let Some(day) = args.measure {
        println!("~~~~~~~~~~~~~~~~~~~~~~~");
        println!("Measuring day: {}", day);
        match day {
            _ => println!("Can not measure day {} solution.", day),
        }
        println!("~~~~~~~~~~~~~~~~~~~~~~~");
    }
}
