#!/usr/bin/ruby

def is_palindrome(n)
	num_str = n.to_s
	length = num_str.length
	num_str.split('').each_with_index do |ch,ix|
		return true if ix > length
		return false if num_str[length - 1 - ix] != ch
	end
	true
end

def binary(n)
	n.to_s(2).to_i
end

double_palindromes = []

(1..1000000).each do |i|
	double_palindromes.push(i) if is_palindrome(i) && is_palindrome(binary(i))
end

puts "There are #{double_palindromes.length} double palindromes with a total sum of #{double_palindromes.reduce(:+)}."
