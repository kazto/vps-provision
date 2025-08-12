lines = File.open(ARGV[0]).readlines.map(&:chomp)

configs = {
  "MAILTO" => ARGV[1],
  "MAILON" => "always",
  "APTCOMMAND" => "apt-get",
}

# delete existing value
lines = lines.map do |line|
  configs.keys.each do |key|
    if /^#{key}/ =~ line
      line = line.gsub(/=.*$/, "=")
    end
  end
  line
end

# add key if not exist
configs.keys.each do |key|
  unless lines.any? { |v| v.include?(key) }
    lines << "#{key}="
  end
end

# modify value
configs.keys.each do |key|
  lines.map! do |line|
    if /^#{key}/ =~ line
      line + configs[key]
    else
      line 
    end
  end
end

lines.each{|v| puts v }
