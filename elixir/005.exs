#!/usr/bin/env elixir

# https://projecteuler.net/problem=5

defmodule P5 do
	def gcd(a, 0) do a end
	def gcd(a, b) do gcd(b, rem(a,b)) end
	def lcm(a, b) do a * div(b, gcd(a, b)) end
end

1..20
|> Enum.reduce(fn(a, b) -> P5.lcm(a, b) end)
|> IO.inspect
