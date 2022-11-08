<?php
    setcookie('user', $user['name'], time() - 3600 * 24 * 7, "/");
    header('Location: ./login');
?>