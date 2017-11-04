#!/usr/bin/ruby

def factorial(n)
  return 1 if n == 0
  n * factorial(n - 1)
end

def special(n)
  n == n.to_s.split('').map{|ch| factorial(ch.to_i)}.reduce(:+)
end

factorials = (0..9).to_a.map{|i| factorial(i)}
result = []
upper_bound = 7 * factorials[9]

for i in (3..upper_bound).to_a do
  result.push(i) if special(i)
end

puts("There are #{result.length} values satisfying this condition: #{result}.")
puts("Their sum is #{result.reduce(:+)}.")
