#!/usr/bin/env ruby
#Ruby script to match "School" using a regular expression

input = ARGV[0]

pattern = /School+/

match = input.scan(pattern)

if match.any?
  puts "#{match.join('')}"
else
  puts ""
end
