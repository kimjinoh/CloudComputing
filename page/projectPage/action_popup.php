<?php
include "dbconfig.php";

                if(isset($_POST['mname'])||isset($_POST['lname'])) {
                    $op1 = $_POST['mname'];
                    $op2 = $_POST['lname'];
                    $result = mysqli_query($conn, "SELECT * FROM store WHERE Stno='" . $op1 . "' AND City='" . $op2 . "' ORDER BY Stno");
                    $street = mysqli_fetch_array($result);
                    echo $result_street = $street['phoneNo'];
                    echo $result_street = $street['Stname'];
                    //echo $result_street = $street['mv_time'];
                }
//                while ($row=mysqli_fetch_assoc($result));{
//                       echo $row['gu'];
//                       echo $row['phoneNo'];
//                       echo "<br/>";
//                }
$conn->close();
?>


