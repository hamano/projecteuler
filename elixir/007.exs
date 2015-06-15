#!/usr/bin/env elixir

# https://projecteuler.net/problem=7

defmodule P7 do
	def solve(n) do
		List.last(genPrime(n))
	end
	def genPrime(n) do
		genPrime(7, n, [2, 3, 5])
	end
	def genPrime(_, n, l) when length(l) >= n do
		l
	end
	def genPrime(i, n, l) do
		if isPrime(i, l) do
			genPrime(i+2, n, l ++ [i])
		else
			genPrime(i+2, n, l)
		end
	end
	def isPrime(i, [h|_]) when h * h > i do true end
	def isPrime(i, [h|_]) when rem(i, h) == 0 do false end
	def isPrime(i, [_|t]) do isPrime(i, t) end
	def isPrime(_, []) do true end
end

P7.solve(10_001)
|> IO.inspect
