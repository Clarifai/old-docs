'''
Example of converting new format to old format.

Similar examples could be made for all other languages. 
If you need help in the conversion, feel free to reach out to support@clarifai.com.
'''

buckets = {}
for c in outputs[0].data.regions[0].data:
  buckets.setdefault(c.vocab_id, [])
  buckets[c.vocab_id].append(c)
