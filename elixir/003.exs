#!/usr/bin/env elixir

# https://projecteuler.net/problem=3

defmodule P3 do
	def factor(n) do
		factor(n, 2, [])
	end
	def factor(1, _, factors) do
		factors
	end
	def factor(n, m, factors) when rem(n, m) == 0 do
		factor(div(n, m), m, [ m | factors ]);
	end
	def factor(n, m, factors) do
		factor(n, m + 1, factors)
	end
end

P3.factor(600851475143)
|> Enum.max
|> IO.inspect
