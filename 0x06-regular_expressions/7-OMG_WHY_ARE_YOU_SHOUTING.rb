#!/usr/bin/env ruby
#Ruby script to match "hbttn," "hbtttn," "hbtttttn"

input = ARGV[0]

pattern = /[A-Z]/

match = input.scan(pattern)

if match.any?
  puts "#{match.join('')}"
else
  puts ""
end
