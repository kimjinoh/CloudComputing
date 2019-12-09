#!/usr/bin/php
<?php

set_time_limit(0);

function insert()
{
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

    $sql = "LOAD DATA INFILE '/home/ubuntu/project/CloudComputing/CloudComputing/integration/timetable.txt'
     INTO TABLE `movie`
     FIELDS TERMINATED BY '.'";



    if(mysqli_query($conn, $sql))
        echo "LOAD DATA INFILE successfully";
    else
        echo "Error LOAD DATA INFILE:".mysqli_error($conn);
    $conn->close();
}

function delete()
{
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

    $sql = "TRUNCATE TABLE `movie`";



    if(mysqli_query($conn, $sql))
        echo "TRUNCATE successfully</br>";
    else
        echo "Error Delete Data:".mysqli_error($conn);
    $conn->close();
}

$chk_test2 = 0;
$c = 1;
while (1)
{
    if ( $c%85000==0 && !$chk_test2 ) { $chk_test2 = 1; delete(); } // 85000초 후 한 번 실행
if ( $c%85000==0 && $chk_test2 ) insert(); //데이터 삭제 확인 후85000초 마다 후 실행
$chk_test2 = 0;
flush();
sleep(1); // 1초씩 지연
$c++;
}

?>
