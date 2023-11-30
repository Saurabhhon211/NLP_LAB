"""
Assignment No 6
Name - Hon Saurabh Kalyan
Batch - B2
Roll No - 25
Assignment Title: Implement and visualize Dependency Parsing of Textual Input using Standford CoreNLP and Spacy library

"""

import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

multiline_text = """
Your smile makes me smile,
Your laugh makes me laugh,
Your eyes are enchanting,
You make my thoughts seem daft.
"""

multiline_doc = nlp(multiline_text)

for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(multiline_doc, style="dep")

# OUTPUT –
'''
TOKEN: 

=====
token.tag_ = '_SP'
token.head.text = 'She'
token.dep_ = 'dep'

TOKEN: She
=====
token.tag_ = 'PRP'
token.head.text = 'be'
token.dep_ = 'nsubj'

TOKEN: will
=====
token.tag_ = 'MD'
token.head.text = 'be'
token.dep_ = 'aux'

TOKEN: never
=====
token.tag_ = 'RB'
token.head.text = 'be'
token.dep_ = 'neg'

TOKEN: be
=====
token.tag_ = 'VB'
token.head.text = 'be'
token.dep_ = 'ROOT'

TOKEN: mine
=====
token.tag_ = 'PRP'
token.head.text = 'be'
token.dep_ = 'attr'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = 'mine'
token.dep_ = 'dep'

Using the 'dep' visualizer
Serving on http://0.0.0.0:5000 ...
'''


























