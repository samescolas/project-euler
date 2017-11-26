#!/usr/bin/ruby

def is_pandigital(n)
	num_str = n.to_s
	pandigital = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	num_str.length == 9 && num_str.split('').sort() == pandigital
end

def create_pandigital(seed)
	ret = ""
	multiple = 1
	while ret.length < 9 do
		ret += (multiple * seed).to_s
		multiple += 1
	end
	return ret if is_pandigital(ret.to_i)
	false
end

max_panny = 1

(1..9999).each do |i|
	max_panny = i if create_pandigital(i)
end

puts "#{max_panny} creates the maximum pandigital value: #{create_pandigital(max_panny)}."
