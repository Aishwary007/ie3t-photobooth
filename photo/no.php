<?php include "header.php" ?>
<br><br><br>
<div class="row">
	<div class="container">
		<div class="col-md-4"></div>
		<div class="col-md-4">
			<form method="post">
				<label for="inputEmail">Email:</label>
				<input type="text" name="email" id="inputEmail" class="form-control" Placeholder="Enter Email(s)">
<br>
				<center><button type="submit" name="submit" class="btn btn-primary">Submit</button></center>
			</form>
		</div>
		<div class="col-md-4"></div>
	</div>
</div>

<?php 
	if (isset($_POST['submit'])) {
		$email = $_POST['email'];
		

		$email_array = explode(',', $email);
		// print_r($email_array);
		$myfile1 = fopen("send1.txt", "w") or die("Unable to open file!");
		fclose($myfile1);

		foreach ($email_array as $key) {
		$myfile1 = fopen("send1.txt", "a") or die("Unable to open file!");
		fwrite($myfile1, $key."\r\n");
		fclose($myfile1);
		}

		header("location:index.php");
	}
 ?>
