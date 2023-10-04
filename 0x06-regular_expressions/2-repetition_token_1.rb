#!/usr/bin/env ruby
#Ruby script to match "hbttn," "hbtttn," "hbtttttn"

input = ARGV[0]

pattern = /hb?tn/

match = input.match(pattern)

if match
  puts "#{match[0]}"
else
  puts ""
end
