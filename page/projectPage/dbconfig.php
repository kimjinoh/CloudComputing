<?php
/**
 * Created by PhpStorm.
 * User: LG
 * Date: 2019-12-09
 * Time: 오후 12:03
 */
$servername = "localhost:3306";
$username = "root";
$password = "0512";

//create connection
$conn = new mysqli($servername, $username, $password);

//check connection
if($conn -> connect_error){
    die("Connection failed : " + $conn -> connect_error);
}
$dbname = "hw";
mysqli_select_db($conn, $dbname) or die('DB selection failed');

?>