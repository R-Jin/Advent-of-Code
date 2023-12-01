fn main() {
    let input = include_str!("./input");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> i32 {
    let mut sum = 0;

    for line in input.lines() {

        sum += get_calibration_value(line);
    }
    sum
}

fn get_calibration_value(input: &str) -> i32 {
    let mut calibration_value = "".to_string();

    for c in input.chars() {
        if c.is_digit(10) {
            calibration_value += &c.to_string();
            break;
        }
    }

    for c in input.chars().rev() {
        if c.is_digit(10) {
            calibration_value += &c.to_string();
            break;
        }
    }
    calibration_value.parse().unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn t1() {
        let input = include_str!("./test");
        assert_eq!(part1(input), 142);
    }
}