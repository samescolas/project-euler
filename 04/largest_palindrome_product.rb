#Add palindrome? method to Numeric class

class Numeric
	def palindrome?
    str_val = self.to_s
    len = str_val.length
    str_val.split("").each_with_index do |ch, i|
      return false if ch != str_val[len - i - 1]
      return true if i > len / 2
    end
    return true
	end
end

val = 999 * 999
found = false

# Search values in descending order starting at max value
loop do
  val -= 1
  if val.palindrome? then
    999.downto(100) do |f1|
      next if val % f1 != 0
      found = (val / f1).to_s.length == 3
      break if found
    end
  end
break if found
end

puts val
