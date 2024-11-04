## Description

My dog-sitter's brother made this website but I can't get in; can you help?[login.mars.picoctf.net](https://login.mars.picoctf.net/)
#### Hints
- (None)
## Solución

![[Pasted image 20241104002711.png]]

```html
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="styles.css">
        <script src="index.js"></script>
    </head>
    <body>
        <div>
          <h1>Login</h1>
          <form method="POST">
            <label for="username">Username</label>
            <input name="username" type="text"/>
            <label for="username">Password</label>
            <input name="password" type="password"/>
            <input type="submit" value="Submit"/>
          </form>
        </div>
    </body>
</html>

```

```js
(async()=>{await new Promise((e=>window.addEventListener("load",e))),document.querySelector("form").addEventListener("submit",(e=>{e.preventDefault();const r={u:"input[name=username]",p:"input[name=password]"},t={};for(const e in r)t[e]=btoa(document.querySelector(r[e]).value).replace(/=/g,"");return"YWRtaW4"!==t.u?alert("Incorrect Username"):"cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ"!==t.p?alert("Incorrect Password"):void alert(`Correct Password! Your flag is ${atob(t.p)}.`)}))})();
```

##### JS corregido 
```js
(async () => {
    await new Promise((resolve) => window.addEventListener("load", resolve));

    document.querySelector("form").addEventListener("submit", (event) => {
        event.preventDefault();

        const selectors = {
            u: "input[name=username]",
            p: "input[name=password]"
        };

        const encodedValues = {};
        
        for (const key in selectors) {
            encodedValues[key] = btoa(document.querySelector(selectors[key]).value).replace(/=/g, "");
        }

        if (encodedValues.u !== "YWRtaW4") {
            alert("Incorrect Username");
        } else if (encodedValues.p !== "cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ") {
            alert("Incorrect Password");
        } else {
            alert(`Correct Password! Your flag is ${atob(encodedValues.p)}.`);
        }
    });
})();

```

Usando [CyberChef](https://gchq.github.io/CyberChef/):
![[Pasted image 20241104003158.png]]
![[Pasted image 20241104003216.png]]
![[Pasted image 20241104003249.png]]
## Bandera
```css
flag: picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}
```
## Notas Adicionales

## Referencias
- [CyberChef](https://gchq.github.io/CyberChef/)