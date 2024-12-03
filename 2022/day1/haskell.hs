import System.IO
import Control.Monad
import Data.List.Split
import Data.List
import System.Environment

main = do
        args <- getArgs
        handle <- openFile (head args) ReadMode
        contents <- hGetContents handle
        let elves = format contents
            sol1 = part1 elves
            sol2 = part2 elves
        putStrLn ("Part 1: " ++ sol1)
        putStrLn ("Part 2: " ++ sol2)
        hClose handle

format :: String -> [Int]
format = map ( sum . map (read :: String -> Int)) . map (splitOn "\n" ) . splitOn "\n\n"

sumFirstThree :: [Int] -> Int
sumFirstThree (x:y:z:xs) = sum([x,y,z])

part1 :: [Int] -> String
part1 = show . maximum

part2 :: [Int] -> String
part2 = show . sumFirstThree . reverse . sort