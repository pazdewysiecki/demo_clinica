<?php
		/*	
		// check que estén todos los datos
		// los datos como ['campo'] corresponden al atributo name="campo" del input en el form
		if(!isset($_POST['name']) || !isset($_POST['email']) || !isset($_POST['subject']) || !isset($_POST['message'])) {
			//darMensajeDeError(); ESTA FUNCION TIRABA ERROR PORQUE NO ESTABA DECLARADA EN NINGUN LADO
			die('Datos incompletos'); ESTA FUNCION TERMINA LA EJECUCION Y SI LE PONES PARAMETRO TE DEVUELVE EN PANTALLA LO QUE LE PONGAS
		}*/

		$nombre = $_POST['name'];
		$email = $_POST['email'];
		$asunto = $_POST['subject'];
		$mensaje = $_POST['message'];

		// Debes editar las próximas dos líneas de código de acuerdo con tus preferencias
		$email_to = "berteuris@gmail.com,suarezhermanos2@gmail.com"; // <- Aquí va el mail al que llegará el mensaje
		//$email_to = "fer.rovito@gmail.com"; // <- Aquí va el mail al que llegará el mensaje
		$email_subject = "Formulario contacto";

		$email_message = "Detalles del formulario de contacto:<br><br>\n\n";
		$email_message .= "Nombre: ".$nombre."<br>";
		$email_message .= "E-Mail: ".$email."<br>";
		$email_message .= "Asunto: ".$asunto."<br>";
		$email_message .= "Mensaje: ".$mensaje."<br><br>";

		// Ahora se envía el e-mail usando la función mail() de PHP
		$headers = 'From: Info Suarez Hnos<info@suarezhnos-si.com.ar>' . "\r\n" .
			    'Reply-To: Info <info@suarezhnos-si.com.ar>' . "\r\n" .
			    'X-Mailer: PHP/' . phpversion();

		$headers .= "MIME-Version: 1.0\r\n";
		$headers .= "Content-Type: text/html; charset=UTF-8\r\n";

		
		if(mail($email_to, $email_subject, $email_message, $headers)){
			echo "<META HTTP-EQUIV=\"Refresh\" CONTENT=\"0;URL=http://www.suarezhnos-si.com.ar/?contact=success\">";
		} else {
			die('Mail function failed');
		} 
?>