#!/usr/bin/ruby

0x980.upto(0x9ff) {|i| print i, " 0x", i.to_s(16), " ", [i].pack("U*"), "\n"}
