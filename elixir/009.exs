#!/usr/bin/env elixir

# https://projecteuler.net/problem=9

defmodule P9 do
	def solve(n) do
		Enum.to_list(for a <- 1..div(n, 3), b <- a..div(n, 2), do: {a, b})
		|> Enum.filter_map(
			fn ({a, b}) ->
				c = (n - a - b)
				a * a + b * b == c * c
			end,
			fn ({a, b}) ->
				a * b * (n - a - b)
			end
		)
	end
end

P9.solve(1000)
|> IO.inspect
