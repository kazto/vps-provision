
lines = File.open(ARGV[0]).readlines.map(&:chomp)
mailto = ARGV[1]
mailfrom = ARGV[2]

def set_mailto(line, value)
  set_value_if_match_line(line, "MailTo", value)
end

def set_detail(line, value)
  set_value_if_match_line(line, "Detail", value)
end

def set_mailfrom(line, value)
  set_value_if_match_line(line, "MailFrom", value)
end

def set_value_if_match_line(line, reg, value)
  return line unless /^#{reg}/ =~ line
  return line if value.nil? || value.empty?

  line.gsub(/\s*=.*$/, " = ") + value
end

result = lines.map do |line|
  line.then {|v| set_mailto(v, mailto) }
      .then {|v| set_detail(v, "High") }
      .then {|v| set_mailfrom(v, mailfrom) }
end

result.each {|v| puts v }