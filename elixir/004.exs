#!/usr/bin/env elixir

# https://projecteuler.net/problem=4

Enum.to_list(for x <- 1..999, y <- x..999, do: x * y)
|> Enum.map(&(Integer.to_string(&1)))
|> Enum.filter(&( String.reverse(&1) == &1 ))
|> Enum.map(&(String.to_integer(&1)))
|> Enum.max
|> IO.inspect
