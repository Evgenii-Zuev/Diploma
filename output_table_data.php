<?php
    // определяем начальные данные
    $db_host = 'localhost';
    $db_name = 'test';
    $db_username = '<***>';
    $db_password = '<***>';
    #$db_table_to_show = 'the_beatles';

    // соединяемся с сервером базы данных
    $connect_to_db = mysql_connect($db_host, $db_username, $db_password)
    or die("Could not connect: " . mysql_error());

    // подключаемся к базе данных
    mysql_select_db($db_name, $connect_to_db)
    or die("Could not select DB: " . mysql_error());

    // выбираем все значения из таблицы
    $qr_result = mysql_query("select * from the_beatles order by collectionName, releaseDate")
    or die(mysql_error());

    // выводим на страницу сайта заголовки HTML-таблицы
    echo '<table border="1">';
    echo '<thead>';
    echo '<tr>';
    echo '<th>kind</th>';
    echo '<th>collectionName</th>';
    echo '<th>trackName</th>';
    echo '<th>collectionPrice</th>';
    echo '<th>trackPrice</th>';
    echo '<th>primaryGenreName</th>';
    echo '<th>trackCount</th>';
    echo '<th>trackNumber</th>';
    echo '<th>releaseDate</th>';
    echo '</tr>';
    echo '</thead>';
    echo '<tbody>';

   // выводим в HTML-таблицу все данные из таблицы MySQL
  while($data = mysql_fetch_array($qr_result)){
    echo '<tr>';
    echo '<td>' . $data['kind'] . '</td>';
    echo '<td>' . $data['collectionName'] . '</td>';
    echo '<td>' . $data['trackName'] . '</td>';
    echo '<td>' . $data['collectionPrice'] . '</td>';
    echo '<td>' . $data['trackPrice'] . '</td>';
    echo '<td>' . $data['primaryGenreName'] . '</td>';
    echo '<td>' . $data['trackCount'] . '</td>';
    echo '<td>' . $data['trackNumber'] . '</td>';
    echo '<td>' . $data['releaseDate'] . '</td>';
    echo '</tr>';
  }

    echo '</tbody>';
    echo '</table>';

    // закрываем соединение с сервером  базы данных
    mysql_close($connect_to_db);
?>
