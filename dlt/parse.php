<?php


ini_set('date.timezone', 'Asia/Chongqing');

$csv = 'result.csv';
for ($i = 1; $i <= 85; $i++) {
	$content = file_get_contents("https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=30&isVerify=1&pageNo=$i");
	$dataJson = json_decode($content, true);
	
	$rows = $dataJson['value']['list'];
	foreach ($rows as $row) {
		file_put_contents($csv, $row['lotteryDrawNum'], FILE_APPEND);

		$date = $row['lotteryDrawTime'];
		$time = strtotime($date);

		$year = date('Y', $time);
		file_put_contents($csv, ',', FILE_APPEND);
		file_put_contents($csv, $year, FILE_APPEND);

		$month = date('m', $time);
		file_put_contents($csv, ',', FILE_APPEND);
		file_put_contents($csv, $month, FILE_APPEND);

		$day = date('d', $time);
		file_put_contents($csv, ',', FILE_APPEND);
		file_put_contents($csv, $day, FILE_APPEND);
		file_put_contents($csv, ',', FILE_APPEND);
		file_put_contents($csv, $day % 2, FILE_APPEND);

		$week = date('w', $time);
		file_put_contents($csv, ',', FILE_APPEND);
		file_put_contents($csv, $week, FILE_APPEND);
		
		$numbers = explode(' ', $row['lotteryDrawResult']);
		foreach ($numbers as $no) {
			file_put_contents($csv, ',', FILE_APPEND);
			file_put_contents($csv, $no, FILE_APPEND);
		}
		file_put_contents($csv, "\n", FILE_APPEND);
	}
}
