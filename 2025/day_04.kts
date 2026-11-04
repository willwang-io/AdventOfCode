import java.io.File

val dirs = listOf(0 to 1, 0 to -1, 1 to 0, -1 to 0, -1 to -1, -1 to 1, 1 to -1, 1 to 1)

fun part1() {
    var grid = File("input.txt").readLines().map { it.toCharArray() }
    println(helper(grid))
}

fun part2() {
    var grid = File("input.txt").readLines().map { it.toCharArray() }

    var ans = 0

    while (true) {
        val cnt = helper(grid)
        if (cnt == 0) {
            break
        }
        ans += cnt
    }

    println(ans)
}

part1()
part2()

fun helper(grid: List<CharArray>): Int {
    val n = grid.size
    val m = grid[0].size

    val curGrid = grid
    val tmpGrid = curGrid.map { it.copyOf() }

    var ans = 0

    for (i in 0..<n) {
        for (j in 0..<m) {
            if (curGrid[i][j] != '@') {
                continue
            }
            var cnt = 0
            for ((di, dj) in dirs) {
                val ni = i + di
                val nj = j + dj
                if (ni >= 0 && ni < n && nj >= 0 && nj < m && curGrid[ni][nj] == '@') {
                    ++cnt
                }
            }
            if (cnt < 4) {
                tmpGrid[i][j] = '.'
                ++ans
            }
        }
    }

    for (i in grid.indices) {
        tmpGrid[i].copyInto(grid[i])
    }

    return ans
}
