<?php
$servername = "3.211.18.78";
$username = "root";
$password = "root";
$dbname = "movie";
$port = "8000";
//create connection
$conn = new mysqli($servername, $username, $password, $dbname, $port);
//check connection
if($conn -> connect_error){
    die("Connection failed : " + $conn -> connect_error);
}
$dbname = "movie";
mysqli_select_db($conn, $dbname) or die('DB selection failed');
if(isset($_POST['mname'])||isset($_POST['lname'])) {
    $op1 = $_POST['mname'];
    $op2 = $_POST['lname'];
    $result = mysqli_query($conn, "SELECT mv_brand, mv_branch, mv_time FROM movie WHERE mv_name='" . $op1 . "' AND mv_loc='" . $op2 . "' ORDER BY mv_time");
    // $street = mysqli_fetch_array($result);
    while($street = mysqli_fetch_array($result)){
        echo $result_street = $street['mv_brand'];
        echo '&nbsp;';
        echo $result_street = $street['mv_branch'];
        echo '&nbsp;';
        echo $result_street = $street['mv_time'];
        echo '<br/><br/>';
    }
}
?>
