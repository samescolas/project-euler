def min_factor(x)
	m = Math.sqrt(x).to_i + 1
	for i in 2..m do
		return i if x % i == 0
	end
	return 1
end

class Numeric
	def prime?
		return false if self <= 0
		return min_factor(self) == 1
	end
end

val = ARGV[0].to_i unless ARGV.length == 0
val = 600851475143 if val.nil? || val == 0

guess = val / min_factor(val)
while true
	if guess.prime? then
		puts guess
		break
	end
	guess = guess / min_factor(guess)
end
