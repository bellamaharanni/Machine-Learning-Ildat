<?php 
 // Menjalankan perintah dir
$hasil = shell_exec('dir');
//echo $hasil;
?> 

<?php
//$perintah = "C:\\Users\\dedyr\\AppData\\Local\\Programs\\Python\\Python312\\python.exe C:\\xampp\\htdocs\\machine_learning\\tes_python.py";
$perintah = "\\opt\\homebrew\\opt\\python@3.12\\libexec\\bin\\python Applications\\XAMPP\\xamppfiles\\htdocs\\machine-learning\\breast.py";
$output = shell_exec($perintah); 
echo "hasil: <pre>$output</pre>"; 
?>