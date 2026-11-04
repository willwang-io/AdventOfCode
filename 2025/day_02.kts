import java.io.File

val intervals =
    File("input.txt")
        .readText()
        .trimEnd()
        .split(",")
        .map { interval ->
            val (start, end) = interval.split("-")
            start.toLong() to end.toLong()
        }

fun part1() {
    var ans = 0L
    for (i in 1..100000) {
        var cur = "$i$i".toLong()
        for ((start, end) in intervals) {
            if (cur >= start && cur <= end) {
                ans += cur
                break
            }
        }
    }
    println(ans)
}

fun part2() {
    var ans = 0L
    for ((start, end) in intervals) {
        val seen = mutableSetOf<Long>()
        for (i in 1..100000) {
            for (j in 2..10) {
                var cur = "$i".repeat(j).toLong()
                if (cur > end) {
                    break
                }
                if (cur >= start && cur <= end && seen.add(cur)) {
                    ans += cur
                }
            }
        }
    }
    println(ans)
}

part1()
part2()
