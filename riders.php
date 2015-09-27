<?php

$dir = 'sqlite:ride_info.db';

$dbh = new PDO($dir) or die("cannot open database!")

$query = "SELECT * FROM rider_info";

foreach ($dbh->query($query) as $row) {
    echo json_encode($row[0]);
}

?>