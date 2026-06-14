$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("C:\Users\Admin\Desktop\So_Tay_AI.lnk")
$Shortcut.TargetPath = "notepad.exe"
$Shortcut.Arguments = "C:\Users\Admin\Desktop\Ghi_Chu_Lenh_AI.txt"
$Shortcut.Description = "Sổ tay lệnh AI"
$Shortcut.Save()
