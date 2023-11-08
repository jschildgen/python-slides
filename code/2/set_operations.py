a = { "Peter", "Ute", "Hans" }
b = { "Otto", "Peter "}

schnittmenge = a & b   # { "Peter" }
vereinigung  = a | b   # { "Peter", "Ute", "Hans", "Otto" }
differenz    = a - b   # { "Ute", "Hans" }