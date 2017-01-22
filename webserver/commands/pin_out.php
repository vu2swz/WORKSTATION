<?php
$pin=$_POST['pin'];
$state=$_POST['state'];
exec ( "sudo python ./commands/gpio_out.py ".$pin." ".$state." 2>&1" );
header("Location: index.php");
?>


