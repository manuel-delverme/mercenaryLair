<?php
$filename = 'emails.txt';
$email = $_POST['email']."\n";

if (is_writable($filename)) {
  if (!$handle = fopen($filename, 'a')) {
    echo "Cannot open file ($filename)";
    exit;
  }
  if (fwrite($handle, $email) === FALSE) {
    echo "Cannot write to file ($filename)";
    exit;
  }
  echo "Success, wrote ($email) to file ($filename)";
  fclose($handle);
} else {
  echo "The file $filename is not writable";
}
?>

<!DOCTYPE HTML>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Coming Soon Splash Page CSS3</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <div id="coming-soon">
      <h1>Thank you</h1>
      <h2> you'll get a mail as soon as we start the beta phase</h2>
      <br/>
      <a href="http://facebook.com/offended" title="Visit our Facebook Page" class="facebook center">Pros 4 hire</a>
    </div>
  </body>
</html>
