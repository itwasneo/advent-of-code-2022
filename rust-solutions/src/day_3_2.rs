use std::collections::HashSet;
use std::fs::File;
use std::io::{BufRead, BufReader, Result};
use std::path::Path;
#[allow(dead_code)]
fn day_3_2() -> u32 {
    let mut total_prios = 0;
    if let Ok(mut reader) = get_reader("../input/input_3_1.txt") {
        loop {
            let mut buf1 = Vec::<u8>::new();
            let mut buf2 = Vec::<u8>::new();
            let mut buf3 = Vec::<u8>::new();
            // First item group
            if let Ok(byte_count) = reader.read_until(10, &mut buf1) {
                if byte_count == 0 {
                    break;
                }
            }
            // Second item group
            if let Ok(byte_count) = reader.read_until(10, &mut buf2) {
                if byte_count == 0 {
                    break;
                }
            }
            // Third item group
            if let Ok(byte_count) = reader.read_until(10, &mut buf3) {
                if byte_count == 0 {
                    break;
                }
            }

            // Removing last inside the buffers due to the fact that
            // read_until includes the delimiters (in this case LF 10)
            // which was messing with the Hash Set intersections.
            let first_item_group: HashSet<u8> =
                HashSet::from_iter(buf1[..buf1.len() - 1].iter().cloned());
            let second_item_group: HashSet<u8> =
                HashSet::from_iter(buf2[..buf2.len() - 1].iter().cloned());
            let third_item_group: HashSet<&u8> = HashSet::from_iter(buf3[..buf3.len() - 1].iter());

            let first_intersection: HashSet<&u8> =
                HashSet::from_iter(first_item_group.intersection(&second_item_group));

            if let Some(common_item) = first_intersection.intersection(&third_item_group).next() {
                total_prios += get_priority(**common_item);
            }
        }
    }

    total_prios
}

fn get_priority(c: u8) -> u32 {
    if c < 91 {
        return (c - 38) as u32;
    }
    (c - 96) as u32
}

pub fn get_reader<P>(filename: P) -> Result<BufReader<File>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename).ok().unwrap();
    Ok(BufReader::new(file))
}

#[cfg(test)]
mod tests {

    use super::day_3_2;

    #[test]
    fn day_3_2_test() {
        let result = day_3_2();
        println!("day_3_2_solution: {}", result);
        assert_eq!(result, 2342);
    }
}
