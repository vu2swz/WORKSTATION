<?php
exec ( "sudo python ./commands/gpio_out.py 18 0 2>&1" );
header("Location: index.php");
?>
