<?php
$page = $_SERVER['PHP_SELF'];
$sec = "1";
?>
<head>
<title>Server Log</title>
<meta http-equiv="refresh" content="<?php echo $sec?>;URL='<?php echo $page?>'">
<meta name="viewport" content="width=device-width, initial-scale=1" /> 
    
</head>

<body>
<h1>LOG FILE</h1>


<?php
$fh = fopen("logs.txt", 'r');

    $pageText = fread($fh, 25000);

    echo nl2br($pageText);
	?>
</body>
