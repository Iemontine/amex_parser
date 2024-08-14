# in.txt
Copy + pasted billing info from the Amex website in the format of:
```
Dec 25
TRANSACTION NAME 1

$29.19

Jan 4
TRANSACTION NAME 2

$5.00
```

is transformed into

# out.txt
```
01-04-2023	TRANSACTION NAME 1	$29.19
12-25-2023	TRANSACTION NAME 2	$5.00
```

which allows for easier copy + pasting into a spreadsheet application.