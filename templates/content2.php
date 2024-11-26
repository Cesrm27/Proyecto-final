<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $cuenta = $_POST['cuenta'];
    $descripcion = $_POST['descripcion'];

    echo "Cuenta: ". $cuenta. "<br>";
    echo "Descripcion: ".  $descripcion. "<br>";
}
?>
