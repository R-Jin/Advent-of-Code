fn main() {
    let input = include_str!("./input.txt");
    let output = part2(input);
    dbg!(output);
}

fn part2(input: &str) -> i32 {
    let mut tot: i32 = 0;

    for line in input.lines() {
        let mut dim: Vec<i32> = line.split("x").map(|n| n.parse::<i32>().unwrap()).collect();
        dim.sort();
        tot += dim[0] * 2 + dim[1] * 2 + dim[0] * dim[1] * dim[2];
    }
    tot
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn t1() {
        assert_eq!(part2("2x3x4"), 34);
        assert_eq!(part2("1x1x10"), 14);
    }
}