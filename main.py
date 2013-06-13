#!/usr/bin/env python
#

import webapp2

form="""
<form method="post" action="/ps2-1" >

	<textarea name="text" >%(message)s</textarea>
	<br />

	<div style="color: red;">%(error)s</div>
	<input type="submit" >

</form>
"""

class PS21Handler(webapp2.RequestHandler):

	# Replaces some raw HTML chars to escape chars
	#
	def escape_html(self, s):
		repl_dict = {'>' : '&gt;', '<': '&lt;', '"': '&quot;', '&': '&amp;'}
		for i, j in repl_dict.iteritems():
			s = s.replace(i, j)
		return s

	# Encodes/decodes given string by ROT13 cipher (Caesar cipher)
	#
	def rot13(self, string_to_replace):
		#replacement dictionary
		repl_dict = {'a' : 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's',
					 'g' : 't', 'h': 'u', 'i': 'v', 'k': 'x', 'l': 'y', 'm': 'z', 'j' : 'w',
					 'n' : 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f',
					 't' : 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm',
					 'A' : 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
					 'G' : 'T', 'H': 'U', 'I': 'V', 'K': 'X', 'L': 'Y', 'M': 'Z', 'J' : 'W',
					 'N' : 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F',
					 'T' : 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
		list_string = list(string_to_replace) #convert unicode word to list, 
														 #to be able to access by index
		#walking our word, char by char 
		for i in range(0, len(list_string)):
			if (repl_dict.has_key(list_string[i])):  #if we have replacement for current char
				list_string[i] = repl_dict[list_string[i]] #then - replace		
		
		string_to_replace = ''.join(list_string) #finally joining our list back to string
		return string_to_replace

	def write_form(self, message, error=""):
		self.response.out.write(form % {"error": error, "message": message})

	def get(self):
		self.write_form('','')

	def post(self):
		text = self.request.get("text")
		message = self.rot13(text)
		message = self.escape_html(message)
		self.write_form(message, text)


class TestHandler(webapp2.RequestHandler):
	def get(self):
		q = self.request.get("text")
		self.response.write(text)

		#self.response.headers['Content-Type'] = 'text/plain'

app = webapp2.WSGIApplication([('/ps2-1', PS21Handler),
							   ('/testform', TestHandler)], 
							   debug=True)
