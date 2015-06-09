#!/usr/bin/env elixir

# https://projecteuler.net/problem=1

1..1000
|> Enum.filter(&(rem(&1, 3) == 0 or rem(&1, 5) == 0))
|> Enum.sum
|> IO.inspect
