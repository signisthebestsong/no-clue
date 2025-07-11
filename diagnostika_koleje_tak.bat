@echo off
ECHO Sbiram udaje a provadim testy. Vyckejte, prosim.
echo Diagnostika koleje Tauferovy - %date% %time% > vystup.log
ipconfig /all >> vystup.log
echo ._
ping -n 10 10.151.0.1 >> vystup.log
echo ._
ping -n 10 aleph.mendelu.cz >> vystup.log
echo ._
arp -a >> vystup.log
echo .
tracert aleph.mendelu.cz >> vystup.log
ECHO Soubor %CD%\vystup.log odeslete v priloze zpravy na adresu internet@mendelu.cz. 
ECHO Toto okno muzete zavrit.
ECHO Dekujeme za spolupraci.
pause
