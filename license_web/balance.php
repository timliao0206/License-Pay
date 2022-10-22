<?php
ob_start();
header("Content-Type:text/html; charset=utf-8");
?>

<html>
	<head>
		<title>License Pay</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
	</head>
	<body class="is-preload">

	<!-- Wrapper -->
		<div id="wrapper">

			<!-- Main -->
				<div id="main">

					<!-- Account -->
						<article id="account">
							<h2 class="major">Search for your Balance</h2>
							<?php   		
								$query=sqlsrv_query($conn,$sql) or die("sql error".sqlsrv_errors());
								while($row=sqlsrv_fetch_array($query))
								{
									echo "
										<table class="alt">
										<tr>
										<td align='center' rowspan='4'><font size='5'><b>Balance in Your Account</b></font></td>
										<td align='center'>Balance</td><td>".$row['balance']."</td></tr>
										</tr>
										</table>
										<style> 
										th,td{
										border-width:1px;
										}
										</style><br/>
										";
								}
							?>

							<!-- Top Up Money -->
							<h2 class="major">Top Up your account</h2>
							<form action="#" method="post" accept-charset="UTF-8" enctype="multipart/form-data">
								<div class="field half">
									<button type="button" class="btn btn-primary btn-sm " onclick="dec()">-</button>
									<button type="button" class="btn btn-sm" id="count">50</button>
									<button type="button" class="btn btn-primary btn-sm " onclick="insc()">+</button>
								</div>
								<p></p> 
								<ul class="actions" >
									<li><input type="submit" value="Submit" class="primary" /></li>
								</ul>
							</form>
						</article>

        <!-- Footer -->
					<footer id="footer">
						<p class="copyright">&copy; 2022 Mei-Chu Hackathon</a>.</p>
					</footer>

			</div>

		<!-- BG -->
			<div id="bg"></div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>
			<script src="assets/js/topup.js"></script>
	</body>
</html>