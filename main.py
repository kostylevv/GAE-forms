#!/usr/bin/env python
#

import webapp2

form="""
<form method="get" action="/testform" >
	<input type="radio" name="q" value="1">
	<input type="radio" name="q" value="2">
	<input type="radio" name="q" value="3"> <br />
	<div style="color: red;">%(error)s</div>
	<input type="submit" >
</form>
"""

class MainHandler(webapp2.RequestHandler):
	def write_form(error=""):
		self.response.out.write(form % {"error": error})

    def get(self):
    	#self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write(form)
        self.write_form()

class TestHandler(webapp2.RequestHandler):
	def get(self):
		q = self.request.get("q")
		self.response.write(q)

		#self.response.headers['Content-Type'] = 'text/plain'

app = webapp2.WSGIApplication([('/', MainHandler),
							   ('/testform', TestHandler)], 
							   debug=True)
