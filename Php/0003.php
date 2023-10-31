<?php
$fileInput = fopen("input.txt", "r");
$fileOutput = fopen("output.txt", "w");

$s1 = trim(fgets($fileInput));
$s2 = trim(fgets($fileInput));

$a = str_split($s1);
$b = str_split($s2);

$c = array_fill(0, max(strlen($s1), strlen($s2)), 0);

$m = min(strlen($s1), strlen($s2));
$Max = max(strlen($s1), strlen($s2)) - 1;

for ($i = $Max; $i >= 0; $i--) {
    if (strlen($s1) >= strlen($s2)) {
        $c[$i] = $c[$i] + $a[$i] + $b[$m - 1];
        if ($i > 0) {
            $c[$i - 1] = intval($c[$i] / 10);
            $c[$i] = $c[$i] % 10;
        }
        $m -= 1;
    } elseif (strlen($s2) > strlen($s1)) {
        $c[$i] = $c[$i] + $b[$i] + $a[$m - 1];
        if ($i > 0) {
            $c[$i - 1] = intval($c[$i] / 10);
            $c[$i] = $c[$i] % 10;
        }
        $m -= 1;
    }
}

$result = implode("", $c);
fwrite($fileOutput, $result);

fclose($fileInput);
fclose($fileOutput);
?>