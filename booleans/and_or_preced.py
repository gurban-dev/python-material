# The and operator takes precedence when used with or in the
# same expression.

# This means that conditions joined with and are grouped together.

has_key = True
knows_code = False
is_daytime = False

# Since has_key is True, the or operator short-circuits:
# Python skips knows_code and is_daytime, and the results
# is True.
print(has_key or knows_code and is_daytime)