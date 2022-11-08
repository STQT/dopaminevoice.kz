<?php
    $login = filter_var(trim($_POST['login']),
    FILTER_SANITIZE_STRING);
    $name = filter_var(trim($_POST['name']),
    FILTER_SANITIZE_STRING);
    $password = filter_var(trim($_POST['password']),
    FILTER_SANITIZE_STRING);

    if(mb_strlen($login) < 5 || mb_strlen($login) > 50){
        echo "<p style='font-size: 20px; margin-top:50px; margin-left:50px; '>" . "Логин ұзындығы қате (5 тен 50 ға дейін таңба/әріп аралығында болу керек)" . "</p>";
		echo "<a href='./register' style='font-size: 20px; margin-left:50px;' >" . "Артқа шығу" . "</a>";
        exit();
    } else if(mb_strlen($name) < 3 || mb_strlen($login) > 50){
        echo "<p style='font-size: 20px; margin-top:50px; margin-left:50px; '>" . "Есім ұзындығы қате (3 тен 50 ға дейін таңба/әріп аралығында болу керек)" . "</p>";
		echo "<a href='./register' style='font-size: 20px; margin-left:50px;' >" . "Артқа шығу" . "</a>";
        exit();
    } else if(mb_strlen($password) < 6 || mb_strlen($password) > 30){
        echo "<p style='font-size: 20px; margin-top:50px; margin-left:50px; '>" . "Құпиясөздің ұзындығы қате (6 дан 30 ға дейін таңба/әріп аралығында болу керек)" . "</p>";
		echo "<a href='./register' style='font-size: 20px; margin-left:50px; '>" . "Артқа шығу" . "</a>";
        exit();
    }


    $password =md5($password."dfgstdjdfd2342");

    require "./blocks/connect.php";
   /*  $mysql = new mysqli('localhost:8889', 'root', 'root', 'register-bd'); */
    if ($mysql -> connect_errno) {
        echo "Failed to connect to MySQL: " . $mysql -> connect_error;
        exit();
      }
      
      // Perform query
      if ($result = $mysql -> query("INSERT INTO users (login, password, name) VALUES ('$login', '$password', '$name')")) {
        $mysql -> close();
      }
      
    header('Location: ./login');
?>