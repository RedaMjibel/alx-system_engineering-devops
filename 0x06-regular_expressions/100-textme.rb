#!/usr/bin/env ruby
#Ruby script to match "hbttn," "hbtttn," "hbtttttn"

input = ARGV[0]

pattern = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

match = input.scan(pattern)

if match.any?
  puts "#{match.join(",")}"
else
  puts ""
end
