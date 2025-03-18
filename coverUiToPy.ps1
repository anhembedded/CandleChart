Get-ChildItem -Recurse -Filter "*.ui" | ForEach-Object {
    $BaseName = $_.BaseName
    $DirName = $_.Directory
    Write-Host "Processing: $($_.FullName)"


    # Remove existing AutoGen file
    $autoGenFile = Join-Path $DirName "autoGen_${BaseName}.py"
    Remove-Item $autoGenFile -ErrorAction SilentlyContinue


    # Generate new UI Python file
    pyside6-uic.exe $_.FullName -o $autoGenFile -g python --postfix "_autoGen_T"


    # Ensure init file exists
    $initFile = Join-Path $DirName "${BaseName}_init.py"
    if (-not (Test-Path $initFile)) {
        $initContent = @"
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget
from utility.log import Logger_T, logging
from views.${BaseName}.autoGen_${BaseName} import Ui_${BaseName}_autoGen_T


class ${BaseName}_init_T(QWidget,Ui_${BaseName}_autoGen_T):
    def __init__(self):
        super().__init__()
        self.log = Logger_T()
        self.setupUi(self)
        self.__addWidget()


    def __addWidget(self):
        pass
"@
        Write-Host "Creating: $initFile"
        New-Item $initFile -ItemType File -Force -Value $initContent


    # Ensure base file exists
    $baseFile = Join-Path $DirName "${BaseName}_T.py"
    if (-not (Test-Path $baseFile)) {
        $TContent = @"
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget
from utility.log import Logger_T, logging
from views.${BaseName}.${BaseName}_init import ${BaseName}_init_T

class ${BaseName}_T(${BaseName}_init_T):
    def __init__(self):
        super().__init__(self)
        self.log = Logger_T()
        self.log.log(message="Initializing [${BaseName}_T]", level=logging.INFO)
        self.__signalAndSlot()
    def __signalAndSlot(self):
        pass
"@
        Write-Host "Creating: $baseFile"
        New-Item $baseFile -ItemType File -Force -Value $TContent
    }
}
}









