#!/usr/bin/env ruby
#Ruby script to match "School" using a regular expression

input = ARGV[0]

pattern = /School/

match = input.match(pattern)

if match
  puts "#{match[0]}"
else
  puts "No match found."
end
