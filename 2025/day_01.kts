import java.io.File

val lines = File("input.txt").readLines()

fun part1() {
    var pos = 50
    var cnt = 0

    for (line in lines) {
        var num = line.substring(1).toInt()

        if (line[0] == 'R') {
            pos = (pos + num) % 100
        } else {
            pos = (pos - num + 100) % 100
        }
        if (pos == 0) {
            ++cnt
        }
    }
    println(cnt)
}

fun part2() {
    var pos = 50
    var cnt = 0

    for (line in lines) {
        var num = line.substring(1).toInt()

        cnt += num / 100
        num %= 100

        if (line[0] == 'R') {
            if (pos + num >= 100) {
                ++cnt
            }
            pos = (pos + num) % 100
        } else {
            if (pos > 0 && pos - num <= 0) {
                ++cnt
            }
            pos = (pos - num + 100) % 100
        }
    }
    println(cnt)
}

part1()
part2()
