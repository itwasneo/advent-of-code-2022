use std::collections::VecDeque;

use crate::day_1_1::read_lines;

struct Stack {
    pub size: usize,
    pub capacity: usize,
    pub items: VecDeque<i32>,
}

#[allow(dead_code)]
fn day_1_2() -> i32 {
    let mut top_3 = Stack {
        size: 0,
        capacity: 3,
        items: VecDeque::new(),
    };

    if let Ok(lines) = read_lines("../input/input_1_1.txt") {
        let mut current_elves_calories = 0;
        for line in lines {
            if let Ok(food_cal) = line {
                if food_cal.is_empty() {
                    // If queue is full
                    if top_3.size == top_3.capacity {
                        //push to front, pop from back
                        // bigger than 1st
                        if top_3.items.front().unwrap() < &current_elves_calories {
                            top_3.items.push_front(current_elves_calories);
                            top_3.items.pop_back();
                        }
                        // push back
                        else if top_3.items.back().unwrap() < &current_elves_calories {
                            top_3.items.pop_back();

                            // bigger than 2nd
                            if top_3.items.back().unwrap() < &current_elves_calories {
                                let tmp = top_3.items.pop_back().unwrap();
                                top_3.items.push_back(current_elves_calories);
                                top_3.items.push_back(tmp);
                            }
                            // bigger than 3rd
                            else {
                                top_3.items.push_back(current_elves_calories);
                            }
                        }
                    }
                    // If queue is not empty, but it is not full
                    else if top_3.size > 0 && top_3.size < top_3.capacity {
                        top_3.size += 1;
                        if top_3.items.front().unwrap() < &current_elves_calories {
                            top_3.items.push_front(current_elves_calories);
                        } else if top_3.items.back().unwrap() < &current_elves_calories {
                            let tmp = top_3.items.pop_back().unwrap();
                            top_3.items.push_back(current_elves_calories);
                            top_3.items.push_back(tmp);
                        } else {
                            top_3.items.push_back(current_elves_calories);
                        }
                    }
                    // If queue is empty
                    else if top_3.items.is_empty() {
                        top_3.items.push_front(current_elves_calories);
                        top_3.size += 1;
                    }
                    current_elves_calories = 0;
                } else {
                    current_elves_calories += food_cal.parse::<i32>().unwrap();
                }
            }
        }
    }
    top_3.items.iter().for_each(|x| println!("{:?}", x));
    top_3.items.iter().sum()
}

#[cfg(test)]
mod tests {
    use super::day_1_2;

    #[test]
    fn day_1_2_test() {
        println!("day_1_2_solution: {:?}", day_1_2());
    }
}
