# frozen_string_literal: true

# Decimal to binary converter
def dec_to_bin(integer)
  var = integer.to_i
  binary = []
  until var.zero?
    result = var % 2
    binary << result
    var = (var / 2).floor
  end
  binary.reverse.join.to_s
end
puts dec_to_bin(0)
