#!/usr/bin/ruby

class Integer
    def rotate
        (self.to_s[1..-1] + self.to_s[0]).to_i
    end
end

def is_prime(n)
    ubound = (Math.sqrt(n) + 1).to_i
    (2..ubound).each do |i|
        return false if n % i == 0
    end
    true
end

def is_circular_prime(n)
    return false if n.to_s.include? '2' or n.to_s.include? '0'
	return false if n.to_s.split('').map{|ch| ch.to_i}.reduce(:+) % 3 == 0
	new_number = n
	loop do
		return false unless is_prime(new_number)
		new_number = new_number.rotate
		return true if new_number == n
	end
end

circular_primes = [2, 3]

(5..1000000).each do |n|
	circular_primes.push(n) if is_circular_prime(n)
end

puts "There are #{circular_primes.length} circular primes: #{circular_primes.join(',')}."
