#!/usr/bin/php


<?php
                $servername = "localhost";
                $username = "root";
                $password = "root";

                //create connection
                $conn = new mysqli($servername, $username, $password);

                //check connection
                if($conn -> connect_error){
                    die("Connection failed : " + $conn -> connect_error);
                }
                $dbname = "movie";
                mysqli_select_db($conn, $dbname) or die('DB selection failed');
                if(isset($_POST['mname'])||isset($_POST['lname'])) {
                    $op1 = $_POST['mname'];
                    $op2 = $_POST['lname'];
                    $result = mysql_query($conn, "SELECT mv_brand, mv_branch, mv_time FROM movie WHERE mv_name='" . $op1 . "' AND mv_loc='" . $op2 . "' ORDER BY mv_time");
		   // $street = mysqli_fetch_array($result);
		    while($street = mysqli_fetch_array($result)){
		    	echo $result_street = $street['mv_brand'];
		    	echo $result_street = $street['mv_branch'];
		    	echo $result_street = $street['mv_time'];
		    }
                }
//                while ($row=mysqli_fetch_assoc($result));{
//                       echo $row['gu'];
//                       echo $row['phoneNo'];
//                       echo "<br/>";
//                }
$conn->close();
?>


