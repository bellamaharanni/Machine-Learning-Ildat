<!DOCTYPE html>
<html>
<head>
    <title>Upload File</title>
 </head>
<?php 
    function panggil_model(){
        $perintah = "\\opt\\homebrew\\opt\\python@3.12\\libexec\\bin\\python Applications\\XAMPP\\xamppfiles\\htdocs\\machine-learning\\breast.py";
        $output = shell_exec($perintah); 
        return $output; 
    }
?>
<body>
    <div class="container">
        <h2>Upload File</h2>
        <form action="" method="post" enctype="multipart/form-data">
            <label for="berkas">Pilih file:</label>
            <input type="file" id="berkas" name="berkas" class="pilih" />
            <button type="submit" name="upload" class="btn">Upload</button>
        </form>
        <?php
        if(isset($_POST["upload"])) {
            $namaFile = 'dataset.csv';
            $namaSementara = $_FILES['berkas']['tmp_name'];
            $dirUpload = "dataset/";
            $terupload = move_uploaded_file($namaSementara, $dirUpload.$namaFile);

            if ($terupload) {
                echo "<p>Upload berhasil!</p>";
                echo "<p>Link dataset: <a href='".$dirUpload.$namaFile."'>".$namaFile."</a></p>";
                $hasil = panggil_model();

                // Displaying the output in table format
                echo "<h3>Hasil Prediksi:</h3>";
                echo "<table class='result-table'>";
                echo "<tr><th>Index</th><th>Hasil Prediksi</th></tr>";

                $hasil_array = explode("\n", trim($hasil)); // Split the output into an array by new lines
                foreach ($hasil_array as $index => $value) {
                    echo "<tr><td>" . ($index + 1) . "</td><td>" . $value . "</td></tr>";
                }

                echo "</table>";
                echo "<p class='link'>Link hasil: <a href='hasil.csv'>hasil.csv</a></p>";
            } else {
                echo "<p>Upload Gagal!</p>";
            }
        }
        ?>
    </div>
</body>
</html>