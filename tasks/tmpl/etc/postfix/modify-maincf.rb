
lines = File.open(ARGV[0]).readlines.map(&:chomp)

# debugger

def set_relayhost_value(v, newval)
  return v unless /^relayhost/ =~ v

  v.gsub(/=.*$/, "= ") + newval
end

def add_or_override_newlines(lines, newlines)
  result = lines.map do |v|
    r = newlines.any? do |line|
      key = line.gsub(/\s*=.*$/, "")
      v.include?(key)
    end
    r ? nil : v
  end
  result.compact.concat(newlines)
end

newlines = [
  "# -------------------------------",
  "smtp_sasl_auth_enable = yes",
  "smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd",
  "smtp_sasl_security_options = noanonymous",
  "smtp_sasl_tls_security_options = noanonymous",
  "smtp_sasl_mechanism_filter = AUTH LOGIN",
  "smtpd_relay_restrictions = permit_mynetworks permit_sasl_authenticated defer_unauth_destination",
]

result = lines.map do |line|
  line.then {|v| set_relayhost_value(v, "[email-smtp.us-east-1.amazonaws.com]:587") }
end.then {|v|
  add_or_override_newlines(v, newlines)
}

result.each do |line|
  puts line
end