#### Два блока кода приводящих к одному результату (долго искал/пригодится)
***
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
        <script type=text/javascript>
                $(function() {
                  $('#refresh_button').bind('click', function() {
                  $('#refresh_button').text('Обновление данных.');
                  $('#refresh_button').attr('disabled','disabled');
                
                $.ajax({
                        url: 'http://192.168.1.56:5000/',
                        async: true,
                        type: "get",
                        success: function(data){
                           alert("Данные обновлены.");
                           location.reload();
                        },
                        error: function(data){
                           alert("Данные обновлены.");
                           location.reload();
                        }
                    });
                    return false;
                  });
                });
        </script>
***
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
        <script type=text/javascript>
                $(function() {
                  $('#refresh_button').bind('click', function() {
                  $('#refresh_button').text('Обновление данных.');
                  $('#refresh_button').attr('disabled','disabled');
        
        $.ajax({
                        url: 'http://192.168.1.56:5000/',
                        async: true,
                        type: "get",
                        complete: function(data){
                           location.reload();
                        }
                    });
                    return false;
                  });
                });
        </script>
***
