import System.IO
import Data.List.Split
import Data.List
import System.Environment

format :: String -> [String]
format = splitOn "\n"

halve :: String -> [String]
halve xs = helper xs "" "" 
    where
        helper :: String -> String -> String -> [String]
        helper "" ys zs = [ys,zs]
        helper (x:xs) ys zs = helper (init xs) (ys ++ [x]) ( (last xs) : zs)

commonChar :: [String] -> Char
commonChar (x:xs) = head (helper xs x)
    where
        helper :: [String] -> String -> String
        helper (x:[]) zs = intersect x zs
        helper (x:xs) zs = helper xs (intersect x zs)

eval :: Char -> Int
eval c | fromEnum c > 96 = fromEnum c -96
       | otherwise = fromEnum c -38

part1 :: [String] -> Int
part1 = sum . map eval . map commonChar . map halve

part2 :: [String] -> Int
part2 = sum . map eval . map commonChar . chunksOf 3

main = do
        args <- getArgs
        handle <- openFile (head args) ReadMode
        contents <- hGetContents handle
        let lines = format contents
        print(part1 lines)
        print(part2 lines)
        hClose handle