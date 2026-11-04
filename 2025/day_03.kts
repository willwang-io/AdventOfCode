import java.io.File

val lines = File("input.txt").readLines()

fun part1() {
    var ans = 0
    for (line in lines) {
        var mx = 0
        for (i in 0..<line.length) {
            for (j in i + 1..<line.length) {
                mx = maxOf(mx, (line[i] - '0') * 10 + (line[j] - '0'))
            }
        }
        ans += mx
    }
    println(ans)
}

fun part2() {
    var ans = 0L

    for (line in lines) {
        val stack = mutableListOf<Int>()
        var drops = line.length - 12

        for (i in 0..<line.length) {
            val cur = line[i] - '0'
            while (stack.isNotEmpty() && stack.last() < cur && drops > 0) {
                stack.removeLast()
                --drops
            }
            stack.add(cur)
        }

        repeat(drops) {
            stack.removeLast()
        }

        ans += stack.fold(0L) { value, digit -> value * 10 + digit }
    }

    println(ans)
}

part1()
part2()
