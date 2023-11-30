fn main() {
    let input = include_str!("./input.txt");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> i32 {
    let mut tot: i32 = 0;

    for line in input.lines() {
        let mut dim: Vec<i32> = line.split("x").map(|n| n.parse::<i32>().unwrap()).collect();
        dim.sort();
        tot += dim[0] * dim[1] * 3 + dim[0] * dim[2] * 2 + dim[1] * dim[2] * 2;
    }
    tot
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn t1() {
        assert_eq!(part1("2x3x4"), 58);
        assert_eq!(part1("1x1x10"), 43);
    }
}