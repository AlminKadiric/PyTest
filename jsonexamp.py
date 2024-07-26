import json

# Sample JSON content
json_content = '''
{
  "current_page": 1,
  "data": [
    {
      "fact": "Unlike dogs, cats do not have a sweet tooth. Scientists believe this is due...",
      "length": 114
    },
    {
      "fact": "When a cat chases its prey, it keeps its head level. Dogs and humans bob the...",
      "length": 97
    },
    {
      "fact": "The technical term for a cat's hairball is a “bezoar.”",
      "length": 54
    }
  ]
}
'''

# Load JSON into a Python dictionary
data = json.loads(json_content)

# Extract the third length
third_length = data['data'][2]['length']

# Print the third length
print(third_length)
