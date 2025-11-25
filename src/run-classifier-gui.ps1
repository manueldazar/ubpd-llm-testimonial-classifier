Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# ========================================
# CONFIG
# ========================================
$CondaEnv = "ubpd_env"
$PythonCmd = "conda run -n $CondaEnv python runner.py"

# ========================================
# WINDOW
# ========================================
$form = New-Object System.Windows.Forms.Form
$form.Text = "UBPD – Clasificador Testimonios (GUI)"
$form.Size = New-Object System.Drawing.Size(780, 640)
$form.StartPosition = "CenterScreen"
$form.Topmost = $false

# ========================================
# LABEL – TEXTO MANUAL
# ========================================
$labelText = New-Object System.Windows.Forms.Label
$labelText.Text = "Texto a clasificar:"
$labelText.Location = New-Object System.Drawing.Point(10, 10)
$labelText.AutoSize = $true
$form.Controls.Add($labelText)

# ========================================
# TEXTBOX – INPUT MANUAL
# ========================================
$textInput = New-Object System.Windows.Forms.TextBox
$textInput.Multiline = $true
$textInput.ScrollBars = "Vertical"
$textInput.Size = New-Object System.Drawing.Size(740, 120)
$textInput.Location = New-Object System.Drawing.Point(10, 30)
$form.Controls.Add($textInput)

# ========================================
# LABEL – ARCHIVO
# ========================================
$labelFile = New-Object System.Windows.Forms.Label
$labelFile.Text = "Archivo (.txt):"
$labelFile.Location = New-Object System.Drawing.Point(10, 165)
$labelFile.AutoSize = $true
$form.Controls.Add($labelFile)

# ========================================
# FILE PATH TEXTBOX
# ========================================
$filePathBox = New-Object System.Windows.Forms.TextBox
$filePathBox.Size = New-Object System.Drawing.Size(620, 25)
$filePathBox.Location = New-Object System.Drawing.Point(10, 185)
$form.Controls.Add($filePathBox)

# ========================================
# BUTTON – BROWSE FILE
# ========================================
$browseButton = New-Object System.Windows.Forms.Button
$browseButton.Text = "Buscar..."
$browseButton.Size = New-Object System.Drawing.Size(120, 25)
$browseButton.Location = New-Object System.Drawing.Point(640, 185)
$form.Controls.Add($browseButton)

$browseButton.Add_Click({
    $dialog = New-Object System.Windows.Forms.OpenFileDialog
    $dialog.Filter = "Archivos de texto (*.txt)|*.txt"
    if ($dialog.ShowDialog() -eq "OK") {
        $filePathBox.Text = $dialog.FileName
    }
})

# ========================================
# CHECKBOX – GUARDAR EN BD
# ========================================
$saveToDB = New-Object System.Windows.Forms.CheckBox
$saveToDB.Text = "Guardar resultado en base de datos"
$saveToDB.Location = New-Object System.Drawing.Point(10, 225)
$saveToDB.Checked = $true
$form.Controls.Add($saveToDB)

# ========================================
# BUTTON – CLASIFICAR
# ========================================
$classifyButton = New-Object System.Windows.Forms.Button
$classifyButton.Text = "Clasificar"
$classifyButton.Size = New-Object System.Drawing.Size(140, 40)
$classifyButton.Location = New-Object System.Drawing.Point(10, 260)
$classifyButton.Font = New-Object System.Drawing.Font("Segoe UI", 11)
$form.Controls.Add($classifyButton)

# ========================================
# OUTPUT BOX
# ========================================
$outputBox = New-Object System.Windows.Forms.TextBox
$outputBox.Multiline = $true
$outputBox.ScrollBars = "Vertical"
$outputBox.Font = New-Object System.Drawing.Font("Consolas", 10)
$outputBox.Size = New-Object System.Drawing.Size(740, 280)
$outputBox.Location = New-Object System.Drawing.Point(10, 320)
$form.Controls.Add($outputBox)

# ========================================
# VALIDATE API KEY
# ========================================
if (-not $env:OPENAI_API_KEY) {
    [System.Windows.Forms.MessageBox]::Show(
        "La variable OPENAI_API_KEY no está definida. Configura la API key antes de ejecutar.",
        "Error",
        "OK",
        "Error"
    )
}

# ========================================
# LOGIC – CLASSIFY
# ========================================
$classifyButton.Add_Click({

    $text = $textInput.Text.Trim()
    $file  = $filePathBox.Text.Trim()

    if (-not $text -and -not $file) {
        [System.Windows.Forms.MessageBox]::Show(
            "Debe ingresar texto o seleccionar un archivo.",
            "Error",
            "OK",
            "Error"
        )
        return
    }

    if ($file -and -not (Test-Path $file)) {
        [System.Windows.Forms.MessageBox]::Show(
            "El archivo indicado no existe.",
            "Error",
            "OK",
            "Error"
        )
        return
    }

    $cmd = $PythonCmd

    if ($text) {
        $escaped = $text.Replace('"', '\"')
        $cmd += " --text `"$escaped`""
    }

    if ($file) {
        $cmd += " --file `"$file`""
    }

    if (-not $saveToDB.Checked) {
        $cmd += " --no-db"
    }

    # Mostrar comando en el output
    $outputBox.Text = "Ejecutando: `n$cmd`n`n"

    # Ejecutar
    try {
        $result = Invoke-Expression $cmd
        $outputBox.AppendText($result)
    }
    catch {
        $outputBox.AppendText("ERROR: $_")
    }
})

# ========================================
# SHOW GUI
# ========================================
$form.Add_Shown({ $form.Activate() })
[void]$form.ShowDialog()
