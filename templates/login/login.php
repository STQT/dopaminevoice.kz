<?php
// define variables and set to empty values
$loginErr = $nameErr = $passErr = "";
$login = $name = $password = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["login"])) {
    $loginErr = "*Логинді теріңіз!";
  } else {
    $login = test_input($_POST["login"]);
  }

  if (empty($_POST["name"])) {
    $nameErr = "*Есімді теріңіз!";
  } else {
    $name = test_input($_POST["name"]);
  }

  if (empty($_POST["password"])) {
    $passErr = "*Құпиясөзді теріңіз!";
  } else {
    $password = test_input($_POST["password"]);
  }
}
?>
<!DOCTYPE html>
<html lang="zxx">

<head>
    <meta charset="UTF-8">
    <meta name="description" content="Dopamine Voice сайтына тіркелу немесе жеке кабинетке кіру">
    <meta name="keywords" content="қазақша аниме, қазақша дыбыстама, дофамин войс, dopamine voice">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="icon" href="/img/Dopamine Voice_minilogo.png">
    <title>Тіркелу | Dopamine Voice</title>
    

    <!-- Google Font -->
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Mulish:wght@300;400;500;600;700;800;900&display=swap"
    rel="stylesheet">

    <!-- Css Styles -->
    <link rel="stylesheet" href="logincss/bootstrap.min.css" type="text/css">
    <link rel="stylesheet" href="logincss/font-awesome.min.css" type="text/css">
    <link rel="stylesheet" href="logincss/elegant-icons.css" type="text/css">
    <link rel="stylesheet" href="logincss/plyr.css" type="text/css">
    <link rel="stylesheet" href="logincss/nice-select.css" type="text/css">
    <link rel="stylesheet" href="logincss/owl.carousel.min.css" type="text/css">
    <link rel="stylesheet" href="../css/slicknav.min.css" type="text/css">
    <link rel="stylesheet" href="../css/style.css">
	<script src='https://kit.fontawesome.com/a076d05399.js' crossorigin='anonymous'></script>
	
	<style>
		.hui:hover{
			background-color: rgb(229, 54, 55);
			color: white;
		}
		.featured-button:hover{
			background-color: rgb(229, 54, 55);
			color: white;
		}
		.hover-red:hover{
			color: rgb(229, 54, 55);;
		}
		.title{
			color: white;
		}
		.title:hover{
			color: rgb(229, 54, 55);
		}
		.form-row{
			padding-bottom: 70px;
			width:100%;
			color: white;
		}
		input{
    		margin-right: auto;
			max-width: 350px;
		}
		h1{
			color: white;
		}
	</style>
</head>

<body>
    <!-- Page Preloder 
    <div id="preloder">
        <div class="loader"></div>
    </div>-->	

    <!-- Header Section Begin -->
    <header class="header">
        <div class="container">
            <div class="row">
                <div class="col-lg-2">
                    <div class="header__logo">
                        <a href="/">
                            <img src="../img/logo_darkmode.png" alt="">
                        </a>
                    </div>
                </div>
                <div class="col-lg-8">
                    <div class="header__nav">
                        <nav class="header__menu mobile-menu">
                            <ul>
                                <li class="hui"><a href="/">БАСТЫ</a></li>
                                <li class="hui"><a href="../categories">КАТЕГОРИЯЛАР</a>
                                    <ul class="dropdown">
                                        <!-- <li class="hui"><a href="../index.html">Толықметражды</a></li>
                                        <li class="hui"><a href="../index.html">ТВ сериалар</a></li>
                                        <li class="hui"><a href="../index.html">2021</a></li> !-->
										<li class="hui"><a href="../categories">Барлығы</a></li>
                                    </ul>
                                </li>
								<li class="hui"><a href="../manga">МАНГАЛАР</a></li>
                                <li class="hui"><a href="../news">ЖАҢАЛЫҚТАР</a></li>
                                <li class="hui"><a href="../about">БІЗ ЖАЙЛЫ</a></li>	
                            </ul>
                        </nav>
                    </div>
                </div>
                <div class="col-lg-2">
                    <div class="header__right">
                        <a href="./login" style="background: #e53637; padding: 10px; border-radius: 15px; font-weight: 700;">ПРОФИЛЬ</a>
                    </div>
                </div>
            </div>
            <div id="mobile-menu-wrap"></div>
        </div>
    </header>
    <!-- Header End -->
    
	    <div class="container mt-4">
        <?php
            if(isset($_COOKIE['user']) == false):
        ?>
    
        <div class="form-row">
            <div class="col">
                <h1 style="padding-bottom: 20px;">Кіру</h1>
                <form action="./auth" method="post">
                    <input type="text" class="form-control" name="login" id="login" placeholder="Логин теріңіз">
					<span class="error"> <?php echo $loginErr;?></span><br>
                    <input type="password" class="form-control" name="password" id="password2" placeholder="Құпиясөзді теріңіз">
					<span class="error"> <?php echo $passErr;?></span><br>
					<input type="checkbox" class="checkbox" onclick="myFunction2()">Құпиясөзді көрсету <br>
					<br>
                    <button class="btn btn-success" type="submit">Кіру</button>
					<br><br>
					<p style="color: white; font-size: 20px;">Cіз тіркелмегенсіз бе? Тіркелу үшін мұнда  <a href="./register">басыңыз</a></p>
                </form>
            </div>
            <?php else: ?>
                <h3 style="color: white; padding-bottom: 370px;">Сәлем <?=$_COOKIE['user']?>! Шығу үшін мұнда <a href="./exit.php">басыңыз.</a></h3>
            <?php endif; ?>
        </div>
    </div>
	
	
<!-- Footer Section Begin -->
<footer class="footer">
    <div class="container">
        <div class="row">
            <div class="col-lg-3">
                <div class="footer__logo">
                    <a href="/"><img class="footer-logo" src="../img/logo_darkmode.png" alt=""></a>
					<p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
                  Dopamine Voice &copy;<script>document.write(new Date().getFullYear());</script> Барлық құқықтар сақталған.
						Дизайн: <a href="https://colorlib.com" target="_blank">Colorlib</a>
                </div>
            </div>
            <div class="col-lg-6">
               <!--  <div class="footer__nav">
                    <ul>
                        <li class="active"><a href="./index.html">Homepage</a></li>
                        <li><a href="./categories.html">Categories</a></li>
                        <li><a href="./blog.html">Our Blog</a></li>
                        <li><a href="#">Contacts</a></li>
                    </ul>
                </div> -->
            </div>
            <div class="col-lg-3">
                  <p>Сайттағы барлық материалдар тек үйде шолу үшін ұсынылған.
                    Авторлық құқық бұзылған жағдайда-поштаға хабарласыңыз: dopaminevoice@inbox.ru</p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
            </div>
      </div>
  </footer>
  <!-- Footer Section End -->


<!-- Js Plugins -->
<script src="js/jquery-3.3.1.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/player.js"></script>
<script src="js/jquery.nice-select.min.js"></script>
<script src="js/mixitup.min.js"></script>
<script src="js/jquery.slicknav.js"></script>
<script src="js/owl.carousel.min.js"></script>
<script src="js/main.js"></script>
<script>
		function myFunction() {
  var x = document.getElementById("password");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
	</script>
	<script>
		function myFunction2() {
  var x = document.getElementById("password2");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
	</script>

</body>

</html>