module Main where
  
import Text.Printf (printf)
  
main :: IO ()
main = do
  line <- getLine
  let [a, b] = map read (words line) :: [Int]
  printf "%d\n" (a + b)