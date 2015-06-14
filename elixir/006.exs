#!/usr/bin/env elixir

# https://projecteuler.net/problem=6

defmodule P6 do
	def powsum(n) do
		1..n
		|> Enum.map(&( &1 * &1 ))
		|> Enum.sum
	end
	def sumpow(n) do
		s = Enum.sum(1..n)
		s * s
	end
end

P6.sumpow(100) - P6.powsum(100)
|> IO.inspect
