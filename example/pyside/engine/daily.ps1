$YearOfToday = (Get-Date).Year
$MonthOfToday = (Get-Date).Month.ToString("D2")
$Today = (Get-Date).Day.ToString("D2")

$YearOfYesterday = (Get-Date).AddDays(-1).Year
$MothOfYesterday = (Get-Date).AddDays(-1).Month.ToString("D2")
$Yesterday = (Get-Date).AddDays(-1).Day.ToString("D2")

$YearOfTomorrow = (Get-Date).AddDays(1).Year
$MonthOfTomorrow  = (Get-Date).AddDays(1).Month.ToString("D2")
$Tomorrow = (Get-Date).AddDays(1).Day.ToString("D2")


$rootDir = Split-Path -Path $PSScriptRoot -Parent
$todayFolder = Join-Path $rootDir data/$YearOfToday/$MonthOfToday/$Today
$yesterdayFolder = Join-Path $rootDir data/$YearOfYesterday/$MothOfYesterday/$Yesterday
$tomorrowFolder = Join-Path $rootDir data/$YearOfTomorrow/$MonthOfTomorrow/$Tomorrow
$COOPEngine = Join-Path $rootDir engine/COOP.exe
New-Item -ItemType Directory -Path $yesterdayFolder -Force
# Remove-Item -Path $yesterdayFolder/EVENTSEQ -Recurse
# Remove-Item -Path $todayFolder/EVENTSEQ -Recurse
# Remove-Item -Path $tomorrowFolder/EVENTSEQ -Recurse


New-Item -ItemType Directory -Path $todayFolder/EVENTSEQ -Force
# 1 week = 604800 seconds
$TotalSeconds = 86400 
$PredictionCommandContext = $todayFolder + "\ " + "recent.tle 0 100 1.0e-3" + " " + $TotalSeconds + " " + $YearOfToday + " " + $MonthOfToday + " " + $Today + " 0 0 0"
$PredictionCommandFile = Join-Path $todayFolder "COMMAND.txt"
$PredictionArguments = $PredictionCommandFile + " EVENTSEQGEN 0 128 -1 -1" 
Write-Host "PredictionArguments: " $PredictionArguments
Write-Host "COOPEngine: $COOPEngine"
$PredictionCommandContext | Out-File $PredictionCommandFile -NoNewline -Encoding ascii
Start-Process -FilePath $COOPEngine -ArgumentList $PredictionArguments -Wait
New-Item -ItemType Directory -Path $tomorrowFolder/EVENTSEQ -Force


Write-Host "Logging completed."



# Path: engine\engine.ps1