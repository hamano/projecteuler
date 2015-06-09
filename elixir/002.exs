#!/usr/bin/env elixir

# https://projecteuler.net/problem=2

defmodule P2 do
	def fib(max, [h|t]) when h > max do
		t
	end
	def fib(max, l) do
		[a|t] = l
		[b|_] = t
		fib(max, [a+b|l])
	end
	def fib(max) do
		fib(max, [2, 1])
	end
end

P2.fib(4000000)
|> Enum.filter(&(rem(&1, 2) == 0))
|> Enum.sum
|> IO.inspect
