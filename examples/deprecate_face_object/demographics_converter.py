'''
Example of converting from new format to old format for demographics model.

Similar examples could be made for all other languages. 
If you need help in the conversion, feel free to reach out to support@clarifai.com.
'''

buckets = {}
for c in outputs[0].data.regions[0].data:
  buckets.setdefault(c.vocab_id, [])
  buckets[c.vocab_id].append(c)

# To acces old face.age_appearance:
age_appearance_results = buckets["age_appearance"]

# To acces old face.gender_appearance:
gender_appearance_results = buckets["gender_appearance"]

# To acces old face.multicultural_appearance:
multicultural_appearance_results = buckets["multicultural_appearance"]
