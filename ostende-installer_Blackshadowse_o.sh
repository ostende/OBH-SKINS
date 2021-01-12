#!/bin/bash -e
opkg update
sleep 3
opkg install https://bitbucket.org/ostend/feeds/raw/197b3786cb58245af91c0bda54dd75e3b0c43bde/all/enigma2-plugin-ostende_3.0%2Bgit12%2Bcf31a23-r2_all.ipk
echo "************************"
echo "*** **** ***** **** ****"
echo "***     done ...    ****"
echo "***                 ****"
echo "*** **** ***** **** ****"
echo "************************"
sleep 3
opkg install https://bitbucket.org/ostend/feeds/raw/197b3786cb58245af91c0bda54dd75e3b0c43bde/all/enigma2-plugin-skins-blackshadowseo_3.0%2Bgit12%2Bcf31a23-r2_all.ipk

echo "#########################################################"
echo "#          Skin BlackShadowSE Mod Ostende               #"
echo "#                INSTALLED SUCCESSFULLY                 #"
echo "#                                                       #"
echo "#########################################################"
echo "#           your Device will RESTART Now                #"
echo "#########################################################"
sleep 3
killall -9 enigma2
exit 0
exit 0
