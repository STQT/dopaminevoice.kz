<?php
    $login = filter_var(trim($_POST['login']),
    FILTER_SANITIZE_STRING);
    $password = filter_var(trim($_POST['password']),
    FILTER_SANITIZE_STRING);

    $password =md5($password."dfgstdjdfd2342");

    require "./blocks/connect.php";

    if ($mysql -> connect_errno) {
        echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
        exit();
    }
      
    $res = $mysql -> query("SELECT * FROM users WHERE login = '$login' AND password = '$password'");
    $user = $res -> fetch_assoc();

    if(!$user){
        echo "<p style='font-size: 20px; margin-top:50px; margin-left:50px; '>" . "Логин немесе құпиясөз қате, қайтадан тырысып көріңіз" . "</p>";
		echo "<a href='./login' style='font-size: 20px; margin-left:50px; '>" . "Артқа шығу" . "</a>";
        exit();
    } 
 
    setcookie('user', $user['name'], time() + 3600 * 24 * 7, "/");

    $mysql -> close();

    header('Location: ./login'); 
?>