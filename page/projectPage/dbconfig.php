<?php
/**
 *  * Created by PhpStorm.
 *   * User: LG
 *    * Date: 2019-12-09
 *     * Time: 오후 12:03
 *      */
$servername = "3.211.18.78";
$username = "root";
$password = "root";
$port = "8000";

//create connection
$conn = new mysqli($servername, $username, $password, $port);

//check connection
if($conn -> connect_error){
    die("Connection failed : " + $conn -> connect_error);
    }
    $dbname = "movie";
    mysqli_select_db($conn, $dbname) or die('DB selection failed');

  ?>
