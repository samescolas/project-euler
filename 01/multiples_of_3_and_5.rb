max_val = ARGV[0].to_i unless ARGV.length == 0
max_val = 1000 if max_val.nil? || max_val == 0

total = 0
max_val.times do |n|
	total += n if n % 3 == 0 || n % 5 == 0
end

puts "Sum: #{total}"
