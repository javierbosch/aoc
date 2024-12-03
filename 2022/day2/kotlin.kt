import java.io.File

val part1Map = mapOf("rockpaper" to "win", "rockscissors" to "lose", "paperrock" to "lose", "paperscissors" to "win", "scissorsrock" to "win", "scissorspaper" to "lose", "rockrock" to "draw", "paperpaper" to "draw", "scissorsscissors" to "draw")
val opponentValues = mapOf("A" to "rock", "B" to "paper", "C" to "scissors")
val playerValues = mapOf("X" to "rock", "Y" to "paper", "Z" to "scissors")
val outcomeValues = mapOf("lose" to 0, "draw" to 3, "win" to 6)
val play_values = mapOf("rock" to 1, "paper" to 2, "scissors" to 3)

val part2Map = mapOf("rockwin" to "paper", "rocklose" to "scissors", "rockdraw" to "rock", "paperwin" to "scissors", "paperlose" to "rock", "paperdraw" to "paper", "scissorswin" to "rock", "scissorslose" to "paper", "scissorsdraw" to "scissors")
val wantedOutcome = mapOf("Z" to "win", "Y" to "draw", "X" to "lose")

fun evalPart1(input: String): Int {
    var reuslt = 0
    val (o,p) = input.split(" ")
    val pM = playerValues[p]
    val oM = opponentValues[o]
    val re = part1Map[oM + pM]
    reuslt += (outcomeValues[re]!!) + (play_values[pM]!!)
    return reuslt
}

fun evalPart2(input: String): Int {
    var reuslt = 0
    val (o,r) = input.split(" ")
    val oM = opponentValues[o]
    val re = wantedOutcome[r]
    val pM = part2Map[oM + re]
    reuslt += (play_values[pM]!!) + (outcomeValues[re]!!)
    return reuslt
}

fun main() {
    val lines = File("input_data.txt").readLines()
    var t1 = 0
    var t2 = 0
    for (line in lines) {
        t1 += evalPart1(line)
        t2 += evalPart2(line)
    }
    println("Part 1: $t1")
    println("Part 2: $t2")
}

