#!/usr/bin/ruby

def avg(arr)
    arr.inject{ |sum, el| sum + el }.to_f / arr.size
end

import_times = []
calc_times = []
export_times = []
reimport_times = []

f = File.open('output.txt', 'r')
f.each_line do |line|
    line.chomp!
    m = line.match /\"(?<name>.*): -?(\d*:)+(?<time>.*)\"/
    if m.nil? then next end

    if m[:name] == 'Import'
        import_times.push(m[:time].to_f)
    elsif m[:name] == 'Calculation'
        calc_times.push(m[:time].to_f)
    elsif m[:name] == 'Export'
        export_times.push(m[:time].to_f)
    elsif m[:name] == 'Reimport'
        reimport_times.push(m[:time].to_f)
    else
        next
    end
end
f.close

puts "     Import: (#{import_times.join("+")})/#{import_times.size}=%.4f" % avg(import_times)
puts "Calculation: (#{calc_times.join("+")})/#{calc_times.size}=%.4f" % avg(calc_times)
puts "     Export: (#{export_times.join("+")})/#{export_times.size}=%.4f" % avg(export_times)
puts "   Reimport: (#{reimport_times.join("+")})/#{reimport_times.size}=%.4f" % avg(reimport_times)