probilu = "ex 2 about testing functions"
print(f"Original string: '{probilu}'")
# 1
no_probilu = probilu.strip()
print(f"strip(): '{no_probilu}'")
# 2
firstBIG = no_probilu.capitalize()
print(f"capitalize(): '{firstBIG}'")
# 3
everywordBIG = no_probilu.title()
print(f"title(): '{everywordBIG}'")
# 4
everylitBIG = no_probilu.upper()
print(f"upper(): '{everylitBIG}'")
# 5
everylitsmall = everylitBIG.lower() 
print(f"lower(): '{everylitsmall}'")