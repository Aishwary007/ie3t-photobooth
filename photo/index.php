<?php include "header.php" ?>
		<br>
	<div class="row">
		<div class="container">
			<center>
			<h2>Paid:</h2>
			<form method="post">
			<!-- <input type="radio" name="paid" id="inputYes" class="form-control" value="yes">Yes
			<input type="radio" name="paid" id="inputNo" class="form-control" value="no">No -->
			<div class="radio">
				<label>
					<input type="radio" name="paid" id="input" value="yes" checked="checked">
					Yes
				</label>
				<label>
					<input type="radio" name="paid" id="input" value="no">
					No
				</label>
			</div>
			<button type="submit" name="submit"class="btn btn-primary">Submit</button></center>
		</form>
		</div>
	</div>
</body>
</html>

<?php 
	if (isset($_POST['submit'])) {
		$paid = $_POST['paid'];
		if ($paid == "yes") {
			header("location:yes.php");
			$myfile2 = fopen("flag.txt", "w") or die("Unable to open file!");
			fwrite($myfile2, "1");
			fclose($myfile2);
		}else{
			header("location:no.php");
			$myfile2 = fopen("flag.txt", "w") or die("Unable to open file!");
			fwrite($myfile2, "0");
			fclose($myfile2);
		}
	}

 ?>

