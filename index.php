<?php
$servername = "localhost";
$username = "root";
$password = "54321qwe";
$dbname = "sensor";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$sql = "SELECT datetime, temperature FROM bmesensor";
$result = mysqli_query($conn, $sql);
//$result = $conn->query($sql);
$dateTemp = array();  

    while($row = mysqli_fetch_row($result)) {;
		
		$dateTemp[]=$row;
		
    }
//echo json_encode($dateTemp, JSON_NUMERIC_CHECK); // tomb feltoltes ellenorzes
$conn->close();
?>


<!DOCTYPE html>  
<html>  
<head>  
<title>KAMONDY</title>  
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">  
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.js"></script>  
<script src="https://code.highcharts.com/highcharts.js"></script>  
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.18.1/moment.min.js"></script>  
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment-timezone/0.5.13/moment-timezone-with-data-2012-2022.min.js"></script>  
  
</head>  
<body>  
  
<script type="text/javascript">  
$(function () {  
  
$('#container').highcharts({  
chart: {  
type: 'line'  
},  
time: {  
timezone: 'Europe/Budapest'  
},  
title: {  
text: 'Hőmérséklet vs. Idő'  
},  
xAxis: {  
title: {  
text: 'Idő'  
},  
type: 'datetime',  
},  
yAxis: {  
title: {  
text: 'Hőmérséklet'  
}  
},  
series: [{  
name: 'Celcius',  
data: <?php echo json_encode($dateTemp, JSON_NUMERIC_CHECK);?>  
}]  
});  
});  
  
</script>  
<script src="charts/js/highcharts.js"></script>  
<script src="charts/js/modules/exporting.js"></script>  
  
<div class="container">  
<br/>  
<h2 class="text-center">Szoba 1 szenzor - Hőm. vs. Idő</h2>  
<div class="row">  
<div class="col-md-10 col-md-offset-1">  
<div class="panel panel-default">  
<div class="panel-heading">30 percenkénti hőmérséklet rögzítés</div>  
<div class="panel-body">  
<div id="container"></div>  
</div>  
</div>  
</div>  
</div>  
</div>  
  
</body>  
</html>  