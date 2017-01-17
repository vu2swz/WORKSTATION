<?php
$page = $_SERVER['PHP_SELF'];
$sec = "10";
?>
<head>
<title>Server  Page</title>
<meta http-equiv="refresh" content="<?php echo $sec?>;URL='<?php echo $page?>'">
<meta name="viewport" content="width=device-width, initial-scale=1" /> 
    
</head>
<body>
<h1>Server Page</h1>

<a href="log.php">Log File</a>
<br><a href="on.php">LED ON</a></br>
<a href="off.php">LED OFF</a></br>


</body>
