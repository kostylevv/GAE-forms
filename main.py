#!/usr/bin/env python
#

import webapp2

form="""
<form method="post" action="/" >

	<textarea name="text" >%(message)s</textarea>
	<br />

	<div style="color: red;">%(error)s</div>
	<input type="submit" >

</form>
"""

class MainHandler(webapp2.RequestHandler):
	def escape_html(self, s):
		repl_dict = {'>' : '&gt;', '<': '&lt;', '"': '&quot;', '&': '&amp;'}
		for i, j in repl_dict.iteritems():
			s = s.replace(i, j)
		return s

	def rot13(self, s):
		x = 'pairs: '
		repl_dict = {'a' : 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's',
					 'g' : 't', 'h': 'u', 'i': 'v', 'k': 'x', 'l': 'y', 'm': 'z', 'j' : 'w',
					 'n' : 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f',
					 't' : 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm',
					 'A' : 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
					 'G' : 'T', 'H': 'U', 'I': 'V', 'K': 'X', 'L': 'Y', 'M': 'Z', 'J' : 'W',
					 'N' : 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F',
					 'T' : 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
		slist = list(s)
		for i in range(0, len(slist)):
			#x += 'letter is '
			#x += letter
			if (repl_dict.has_key(slist[i])):
				slist[i] = repl_dict[slist[i]]
	
		#for i, j in repl_dict.iteritems():
			#s = s.replace(i, j)
		#	x += 'pair: '
		#	x += i
		#	x += j
		#	x += '; '
		#x += 'And result is: '
		#x += s;
		s = ''.join(slist)
		return s

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

app = webapp2.WSGIApplication([('/', MainHandler),
							   ('/testform', TestHandler)], 
							   debug=True)
