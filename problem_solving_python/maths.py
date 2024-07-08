def Average (num_student):
    total = 0
    counter = 0

    while counter < num_student:
        counter += 1
        


codes = "2-1-19-9-3 3-15-4-5-19 1-18-5 5-1-19-25 20-15 2-18-5-1-11"
sections = codes.split() # split codes based on blankspace
text = ""
for s in sections:
    nums = s.split("-") # split each section based on '-'
for n in nums:
    value = int(n) # convert from string to integer
    ch = chr(value + 64) # this maps 1 to A, 2 to B etc.
    text = text + ch
    text = text + ' '

print(text)