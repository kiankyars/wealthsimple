module Gold where
import Data.List

-- The golden ratio
phi :: Double
phi = (sqrt 5 + 1) / 2

polynomial :: Double -> Double
polynomial x = x^2 - x - 1

f x = polynomial (polynomial x)

main = do
  print (polynomial phi)
  print (f phi)

  let product = "mil"

  let price = if product == "milk" then 5 else 2

  print (price)

-- recursive sum of a list
sumList :: [Int] -> Int
sumList [] = 0
sumList (x : xs) = x + sumList xs


readInt :: String -> Either String Int
readInt "0" = Right 0
readInt "1" = Right 1
readInt s = Left ("Unsupported string: " ++ s)

iWantAString :: Either Int String -> String
iWantAString (Right str)   = str
iWantAString (Left number) = show number

lectureParticipants :: [Either String Int]
lectureParticipants = [Right 10, Right 13, Left "easter vacation", Right 17, Left "lecturer was sick", Right 3]

-- parse country code into country name, returns Nothing if code not recognized
parseCountry :: String -> Maybe String
parseCountry "FI" = Just "Finland"
parseCountry "SE" = Just "Sweden"
parseCountry _ = Nothing

flyTo :: String -> String
flyTo countryCode = case parseCountry countryCode of
  Just country -> "You're flying to " ++ country
  Nothing -> "You're not flying anywhere"

-- sentenceType :: String -> String
-- sentenceType sentence = case last sentence of 
--   '.' -> "statement"
--   '?' -> "question"
--   '!' -> "exclamation"
--   _   -> "not a sentence"

-- lastLetter :: String -> Char
lastLetter sentence = last sentence

-- sentenceType :: String -> String
sentenceType sentence = handleResult (lastLetter sentence)
  where handleResult '.' = "statement"
        handleResult '?' = "question"
        handleResult '!' = "exclamation"
        handleResult _   = "not a sentence"

function number = case number of
  0 -> "zero"
  1 -> "one"
  _ -> "not zero or one"

direction :: Either Int Int -> String
direction (Left i) = "you should go left " ++ show i ++ " meters!"
direction (Right i) = "you should go right " ++ show i ++ " meters!"



doTwice f x = f (f x)

makeCool x = "wow " ++ x ++ "!"

pos x = x< 0

-- substringsOfLength gives all substrings of a string that are n or shorter

substringsOfLength n s = map (take n) (tails s)

whatFollows :: Char -> Int -> String -> [String]
whatFollows c k string = map tail (filter match (substringsOfLength (k+1) string))
  where match sub = take 1 sub == [c]


between lo hi x = x < hi && x > lo