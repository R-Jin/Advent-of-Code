fn main() {
    let input = include_str!("./input");
    let output = part2(input);
    dbg!(output);
}

fn part2(input: &str) -> i32 {
    let mut sum = 0;

    for line in input.lines() {
        sum += get_calibration_value(line);
    }
    sum
}

fn get_calibration_value(input: &str) -> i32 {
    let nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

    // Find first occurence of nums
    let mut l_i: i32 = input.len() as i32;
    let mut l_num = "";
    for num in nums {
        match input.find(num) {
            Some(i) => {
                if (i as i32) < l_i { 
                    l_i = i as i32; 
                    l_num = num;
                }
            }
            None => continue
        }
    }

    // Find last occurence of nums
    let mut r_i: i32 = input.len() as i32;
    let mut r_num = "";
    let reversed_input: String = input.chars().rev().collect();
    for num in nums {
        let reversed_num: String = num.chars().rev().collect();
        match reversed_input.find(&reversed_num) {
            Some(i) => {
                if (i as i32) < r_i { 
                    r_i = i as i32; 
                    r_num = &num;
                }
            }
            None => continue
        }
    }

    // Convert from num to digit
    let mut l_num = nums.iter().position(|&num| num == l_num).unwrap() as i32;
    l_num = if l_num < 9 {l_num + 1} else {l_num - 8};

    let mut r_num = nums.iter().position(|&num| num == r_num).unwrap() as i32;
    r_num = if r_num < 9 {r_num + 1} else {r_num - 8};

    // Return number
    l_num * 10 + r_num

}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn t1() {
        let input = include_str!("./test2");
        assert_eq!(part2(input), 281);
    }
}