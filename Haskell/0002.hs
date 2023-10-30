main :: IO ()
main = do
  input <- getLine
  let [a, b] = map (read :: String -> Int) (words input)
  let x = if a > b then ">" else if a == b then "=" else "<"
  putStrLn x