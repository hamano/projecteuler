#!/usr/bin/env elixir

1..1000
|> Stream.filter(&(rem(&1, 3) == 0 or rem(&1, 5) == 0))
|> Enum.sum
|> IO.inspect
