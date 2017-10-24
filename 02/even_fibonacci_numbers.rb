max_val = ARGV[0].to_i unless ARGV.length == 0
max_val = 4000000 if max_val.nil? || max_val == 0

total = 0

curr = 1
prev = 0

while curr < max_val
	total += curr if curr % 2 == 0
	tmp = curr
	curr = curr + prev
	prev = tmp
end

puts "Sum: #{total}"
