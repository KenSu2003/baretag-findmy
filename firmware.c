export LC_CTYPE=C
xxd -p -c 100000 4LH8EO_keyfile | xxd -r -p | dd of=nrf51_firmware.bin skip=1 bs=1 seek=$(grep -oba OFFLINEFINDINGPUBLICKEYHERE! nrf51_firmware.bin | cut -d ':' -f 1) conv=notrunc