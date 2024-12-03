import System.IO
import Control.Monad
import Data.List.Split
import Data.List
import System.Environment


data ValidMove = Rock | Paper | Scissors deriving (Show, Eq)

data MoveInfo = MoveInfo {move :: ValidMove, wins :: ValidMove, loses :: ValidMove} deriving (Show)

data Outcome = Win | Lose | Draw deriving (Show, Eq)

format :: String -> [[String]]
format = map (splitOn " ") . splitOn "\n"

parseMove :: String -> ValidMove
parseMove "X" = Rock
parseMove "Y" = Paper
parseMove "Z" = Scissors
parseMove "A" = Rock
parseMove "B" = Paper
parseMove "C" = Scissors
parseMove _ = error "Invalid move"


parseMoveInfo :: ValidMove -> MoveInfo
parseMoveInfo Rock = MoveInfo Rock Scissors Paper
parseMoveInfo Paper = MoveInfo Paper Rock Scissors
parseMoveInfo Scissors = MoveInfo Scissors Paper Rock

outcomePlay :: MoveInfo -> ValidMove -> Outcome
outcomePlay moveInfo playerMove
    | playerMove == wins moveInfo = Lose
    | playerMove == loses moveInfo = Win
    | otherwise = Draw

outcomeToInt :: Outcome -> Int
outcomeToInt Win = 6
outcomeToInt Draw = 3
outcomeToInt Lose = 0

valueMove :: ValidMove -> Int
valueMove Rock = 1
valueMove Paper = 2
valueMove Scissors = 3

evaluatePlay :: ValidMove -> Outcome -> Int 
evaluatePlay playerMove outcome = (outcomeToInt outcome) + (valueMove playerMove) 

part1 :: [[String]] -> Int
part1 [] = 0
part1 ((x:y):xs) = evaluatePlay playerMove (outcomePlay (parseMoveInfo (parseMove x)) playerMove) + (part1 xs)
        where
                playerMove = parseMove (head y)

parseWantedOutcome :: String -> Outcome
parseWantedOutcome "X" = Lose
parseWantedOutcome "Y" = Draw
parseWantedOutcome "Z" = Win
parseWantedOutcome _ = error "Invalid outcome"

moveForOutcome :: MoveInfo -> Outcome -> ValidMove
moveForOutcome moveInfo outcome
    | outcome == Win = loses moveInfo
    | outcome == Draw = move moveInfo
    | outcome == Lose = wins moveInfo

part2 :: [[String]] -> Int
part2 [] = 0
part2 ((x:y):xs) = (outcomeToInt outcome) + (valueMove playerMove) + (part2 xs)
        where
                outcome = parseWantedOutcome (head y)
                playerMove = moveForOutcome (parseMoveInfo (parseMove x)) outcome

main = do
        args <- getArgs
        handle <- openFile (head args) ReadMode
        contents <- hGetContents handle
        let moves = format contents
        print $ part1 moves
        print $ part2 moves
        hClose handle
