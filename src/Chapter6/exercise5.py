string = 'X-DSPAM-Confidence:0.8475'
first=string.find(":")
extract=string[first+1:]
extract=float(extract)
print(type(extract))