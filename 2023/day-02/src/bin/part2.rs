use std::collections::HashMap;

fn main() {
    let input = include_str!("./input");
    let result = part2(input);
    dbg!(result);
}

fn part2(input: &str) -> i32 {
    let mut sum_of_cube_power = 0;

    let lines = input.lines();

    for line in lines {
        let cubes = line.split(": ").skip(1).next().unwrap();
        let min_cube_set = get_minimum_cube_set(cubes);
        sum_of_cube_power += min_cube_set.0 * min_cube_set.1 * min_cube_set.2;
    }
    sum_of_cube_power
}

fn parse_cube_set(input: &str) -> Vec<&str> {
    input.split(&[',', ';'][..]).map(|str| str.trim()).collect()
}

fn get_minimum_cube_set(input: &str) -> (i32, i32, i32) {
    let mut possible_bag = HashMap::new();

    for cube in parse_cube_set(input) {
        let mut split_input = cube.split(" ");
        let size: i32 = split_input.next().unwrap().parse().unwrap();
        let color = split_input.next().unwrap();

        if !possible_bag.contains_key(color) {
            possible_bag.insert(color, size);
        } else if *possible_bag.get(color).unwrap() < size {
            possible_bag.insert(color, size);
        }
    }

    (*possible_bag.get("red").unwrap(), *possible_bag.get("green").unwrap(), *possible_bag.get("blue").unwrap())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn get_minimum_cube_set_test() {
        assert_eq!(get_minimum_cube_set("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"), (4, 2, 6));
    }

    #[test]
    fn t1() {
        let input = include_str!("./test_input");
        assert_eq!(part2(input), 2286);
    }
}