## Description

How about trying to match a regular expressionThe website is running [here](http://saturn.picoctf.net:57565/).
## Solución

```html
<!DOCTYPE html>
<html>

<head>
	<!-- <link rel="stylesheet" href="./index.css" /> -->
	<style>
		.heading {
			width: 100%;
			height: 40px;
			background-color: coral;
			padding-left: 10px;
			font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
		}

		.normal-form {
			text-align: center;
			margin-top: 5%;
		}

		#submit-but {
			border-radius: 0;
			width: 250px;
			height: 25px;

		}

		#name {
			width: 250px;
			height: 25px;
			background-color: rgb(241, 226, 206);
		}

		#sub-heading {
			color: brown;
		}
	</style>
</head>

<body>

	<h1 class="heading">PicoCTF</h1>
	<p></p>

	<div class="normal-form">
		<h2 id="sub-heading">Valid Input</h2>
		<form action="#" onsubmit="return send_request()">
			<input type="text" id="name" name="input" placeholder="Input text">
			<br>
			<br>
			<button id="submit-but" type="submit" id="submit-button">SUBMIT</button>
		</form>
	</div>
</body>
<script>
	function send_request() {
		let val = document.getElementById("name").value;
		// AQUÍ ESTÁ LA RESPUESTA ES UN REGEX
		// ^p.....F!?
		fetch(`/flag?input=${val}`)
			.then(res => res.text())
			.then(res => {
				const res_json = JSON.parse(res);
				alert(res_json.flag)
				return false;
			})
		return false;
	}

</script>

</html>
```
![[Pasted image 20241001221615.png]]

## Bandera
```css
flag: picoCTF{succ3ssfully_matchtheregex_08c310c6}
```
## Notas Adicionales
La bandera se obtuvo a partir de que revisáramos el código fuente de la página y nos diéramos cuenta de que con una REGEX  que cumpliera con empezar con la letra `p` y terminara con `f` nos regresaría la bandera.
# comandos utilizados

## Referencias
****