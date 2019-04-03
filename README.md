# eshailsat2
Scripts and flowgraphs for the Es'hailsat-2 amateur transponder

Included are:

-beacongen.py - a Python script for generating wav files containing a CW beacon, specified by an input string. Basic pulseshaping is used to remove key clicks.

-beacontrack.grc - a GNU Radio flowgraph for receiving the QO-100 / Es'hailsat-2 narrowband amateur transponder and performing phaselocking to the PSK400 beacon for automatic LNB drift correction

-eshailuplinkgen.grc - a GNU Radio flowgraph for generating an USB signal at 2.4 GHz for uplinking to the QO-100 / Es'hailsat-2 narrowband amateur transponder. Uses Controlled Envelope SSB blocks from https://github.com/drmpeg/gr-cessb
# Project Purpose.
I was looking for a way to lock to the Beacon to allow me to still use a cheep LNB that do not have stable LO so the frequency can then be offset by the locking PLL.
This will allow me to expose a service to listen to specific frequency wile still using unstableness LNB LO.
I then found this project and witch locks to the beacon telemetry tracking the frequency. 
I think this is a grate project that would allow me to add my fetcheirs as listed below.
# Original Block diagram
![Eshail-2 QA-100 Beacon lock](beacontrack_2.grc.png)
Application screenshot
![Eshail-2 QA-100 Beacon lock](beacontrack_app_1.grc.png)
# Changes from original project
1) rCange input to rtl_sdr
2) Disabled null object.

# Planed changes.
1) Adding APRS decoder link to PLL lock Frequency
2) Adding PSK mail server Link to PLL Lock Frequency
3) Adding Voice regonition AI engin
4) Adding AI signal identification system
