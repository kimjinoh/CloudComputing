<?php
/**
<<<<<<< HEAD
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
=======
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
>>>>>>> 3771e05e05df37aa7eb2c816ade6130d49c851fc

//check connection
if($conn -> connect_error){
    die("Connection failed : " + $conn -> connect_error);
<<<<<<< HEAD
    }
    $dbname = "movie";
    mysqli_select_db($conn, $dbname) or die('DB selection failed');

  ?>
=======
}
$dbname = "movie";
mysqli_select_db($conn, $dbname) or die('DB selection failed');

?>
>>>>>>> 3771e05e05df37aa7eb2c816ade6130d49c851fc
