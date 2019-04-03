#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Es'hailsat-2 Beacon tracker
# Author: W.J. Ubbels PE4WJ
# Description: Es'hailsat-2 Beacon tracker
# Generated: Wed Apr  3 13:11:32 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sip
import sys
import threading
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Es'hailsat-2 Beacon tracker")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Es'hailsat-2 Beacon tracker")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.lnb_corr_ppm = lnb_corr_ppm = 24.8
        self.ref_freq = ref_freq = 25*1e6*(1+lnb_corr_ppm*1e-6)
        self.mult = mult = 390
        self.tpx_center_freq = tpx_center_freq = 10489675000
        self.LNB_LO_freq = LNB_LO_freq = ref_freq*mult
        self.variable_function_probe_0 = variable_function_probe_0 = 0
        self.decimation = decimation = 10
        self.RX_frequency = RX_frequency = tpx_center_freq-LNB_LO_freq
        self.variable_function_probe_1 = variable_function_probe_1 = 0
        self.var_freq_fine = var_freq_fine = 0
        self.var_freq = var_freq = 0
        self.upper_int = upper_int = -40
        self.tracked_bcn_freq_textbox = tracked_bcn_freq_textbox = variable_function_probe_0*-1*(48000/decimation)
        self.track_beacon = track_beacon = 0
        self.samp_rate = samp_rate = 480000
        self.rx_freq_textbox_0 = rx_freq_textbox_0 = RX_frequency/1e6
        self.rx_audio_rate = rx_audio_rate = 44200
        self.ref_freq_textbox = ref_freq_textbox = ref_freq/1e6
        self.lower_int = lower_int = -84
        self.loop_bw = loop_bw = 0.01
        self.level_tone = level_tone = 0
        self.expected_beacon_freq = expected_beacon_freq = 125000
        self.beacontrack_bw = beacontrack_bw = 20000
        self.RX_gain = RX_gain = 50
        self.AF_gain = AF_gain = 0.01

        ##################################################
        # Blocks
        ##################################################
        self.analog_probe_avg_mag_sqrd_x_0 = analog.probe_avg_mag_sqrd_c(0, 0.001)

        def _variable_function_probe_1_probe():
            while True:
                val = self.analog_probe_avg_mag_sqrd_x_0.level()
                try:
                    self.set_variable_function_probe_1(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (4))
        _variable_function_probe_1_thread = threading.Thread(target=_variable_function_probe_1_probe)
        _variable_function_probe_1_thread.daemon = True
        _variable_function_probe_1_thread.start()

        self._var_freq_fine_range = Range(-1250, 1250, 10, 0, 200)
        self._var_freq_fine_win = RangeWidget(self._var_freq_fine_range, self.set_var_freq_fine, 'SSB receiver fine tune (Hz)', "counter_slider", float)
        self.top_layout.addWidget(self._var_freq_fine_win)
        self._var_freq_range = Range(-200000, 200000, 100, 0, 200)
        self._var_freq_win = RangeWidget(self._var_freq_range, self.set_var_freq, 'SSB receiver coarse tune (Hz)', "counter_slider", float)
        self.top_layout.addWidget(self._var_freq_win)
        self._upper_int_range = Range(-40, 40, 1, -40, 200)
        self._upper_int_win = RangeWidget(self._upper_int_range, self.set_upper_int, 'wfall upper intensity', "counter_slider", float)
        self.top_layout.addWidget(self._upper_int_win)
        _track_beacon_check_box = Qt.QCheckBox('Beacon track enable')
        self._track_beacon_choices = {True: 1, False: 0}
        self._track_beacon_choices_inv = dict((v,k) for k,v in self._track_beacon_choices.iteritems())
        self._track_beacon_callback = lambda i: Qt.QMetaObject.invokeMethod(_track_beacon_check_box, "setChecked", Qt.Q_ARG("bool", self._track_beacon_choices_inv[i]))
        self._track_beacon_callback(self.track_beacon)
        _track_beacon_check_box.stateChanged.connect(lambda i: self.set_track_beacon(self._track_beacon_choices[bool(i)]))
        self.top_layout.addWidget(_track_beacon_check_box)
        self._lower_int_range = Range(-150, -80, 1, -84, 200)
        self._lower_int_win = RangeWidget(self._lower_int_range, self.set_lower_int, 'wfall lower intensity', "counter_slider", float)
        self.top_layout.addWidget(self._lower_int_win)
        self._loop_bw_range = Range(0, 0.1, 0.0001, 0.01, 200)
        self._loop_bw_win = RangeWidget(self._loop_bw_range, self.set_loop_bw, 'Beacon track Costas loop BW (rad/sample)', "counter_slider", float)
        self.top_layout.addWidget(self._loop_bw_win)
        _level_tone_check_box = Qt.QCheckBox('Audible beacon strength')
        self._level_tone_choices = {True: 1, False: 0}
        self._level_tone_choices_inv = dict((v,k) for k,v in self._level_tone_choices.iteritems())
        self._level_tone_callback = lambda i: Qt.QMetaObject.invokeMethod(_level_tone_check_box, "setChecked", Qt.Q_ARG("bool", self._level_tone_choices_inv[i]))
        self._level_tone_callback(self.level_tone)
        _level_tone_check_box.stateChanged.connect(lambda i: self.set_level_tone(self._level_tone_choices[bool(i)]))
        self.top_layout.addWidget(_level_tone_check_box)
        self._expected_beacon_freq_tool_bar = Qt.QToolBar(self)
        self._expected_beacon_freq_tool_bar.addWidget(Qt.QLabel('Expected beacon frequency (Hz)'+": "))
        self._expected_beacon_freq_line_edit = Qt.QLineEdit(str(self.expected_beacon_freq))
        self._expected_beacon_freq_tool_bar.addWidget(self._expected_beacon_freq_line_edit)
        self._expected_beacon_freq_line_edit.returnPressed.connect(
        	lambda: self.set_expected_beacon_freq(eng_notation.str_to_num(str(self._expected_beacon_freq_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._expected_beacon_freq_tool_bar)
        self.blocks_probe_signal_x_0 = blocks.probe_signal_f()
        self._beacontrack_bw_range = Range(1000, 40000, 100, 20000, 200)
        self._beacontrack_bw_win = RangeWidget(self._beacontrack_bw_range, self.set_beacontrack_bw, 'beacon track receiver IF bandwidth (Hz)', "counter_slider", float)
        self.top_layout.addWidget(self._beacontrack_bw_win)
        self._AF_gain_range = Range(0, 1, 0.01, 0.01, 200)
        self._AF_gain_win = RangeWidget(self._AF_gain_range, self.set_AF_gain, 'RX AF gain ', "counter_slider", float)
        self.top_layout.addWidget(self._AF_gain_win)

        def _variable_function_probe_0_probe():
            while True:
                val = self.blocks_probe_signal_x_0.level()
                try:
                    self.set_variable_function_probe_0(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _variable_function_probe_0_thread = threading.Thread(target=_variable_function_probe_0_probe)
        _variable_function_probe_0_thread.daemon = True
        _variable_function_probe_0_thread.start()

        self._tracked_bcn_freq_textbox_tool_bar = Qt.QToolBar(self)
        self._tracked_bcn_freq_textbox_tool_bar.addWidget(Qt.QLabel('Tracked beacon freq (Hz)'+": "))
        self._tracked_bcn_freq_textbox_line_edit = Qt.QLineEdit(str(self.tracked_bcn_freq_textbox))
        self._tracked_bcn_freq_textbox_tool_bar.addWidget(self._tracked_bcn_freq_textbox_line_edit)
        self._tracked_bcn_freq_textbox_line_edit.returnPressed.connect(
        	lambda: self.set_tracked_bcn_freq_textbox(eng_notation.str_to_num(str(self._tracked_bcn_freq_textbox_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._tracked_bcn_freq_textbox_tool_bar)
        self._rx_freq_textbox_0_tool_bar = Qt.QToolBar(self)
        self._rx_freq_textbox_0_tool_bar.addWidget(Qt.QLabel('USRP center frequency [MHz]'+": "))
        self._rx_freq_textbox_0_line_edit = Qt.QLineEdit(str(self.rx_freq_textbox_0))
        self._rx_freq_textbox_0_tool_bar.addWidget(self._rx_freq_textbox_0_line_edit)
        self._rx_freq_textbox_0_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq_textbox_0(eng_notation.str_to_num(str(self._rx_freq_textbox_0_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._rx_freq_textbox_0_tool_bar)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(RX_frequency, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)

        self._ref_freq_textbox_tool_bar = Qt.QToolBar(self)
        self._ref_freq_textbox_tool_bar.addWidget(Qt.QLabel('LNB reference freuency [MHz]'+": "))
        self._ref_freq_textbox_line_edit = Qt.QLineEdit(str(self.ref_freq_textbox))
        self._ref_freq_textbox_tool_bar.addWidget(self._ref_freq_textbox_line_edit)
        self._ref_freq_textbox_line_edit.returnPressed.connect(
        	lambda: self.set_ref_freq_textbox(eng_notation.str_to_num(str(self._ref_freq_textbox_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._ref_freq_textbox_tool_bar)
        self.rational_resampler_xxx_4 = filter.rational_resampler_ccc(
                interpolation=8000,
                decimation=samp_rate/decimation,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=480000,
                decimation=480000/decimation,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=rx_audio_rate,
                decimation=samp_rate,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	'Corrected input spectrum', #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(True)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['test', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(lower_int, upper_int)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	8000, #bw
        	'Costas loop output', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	'Corrected input spectrum', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_1 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate/decimation, 1000, 4000, firdes.WIN_HAMMING, 6.76))
        self._lnb_corr_ppm_range = Range(-40, 40, 0.1, 24.8, 200)
        self._lnb_corr_ppm_win = RangeWidget(self._lnb_corr_ppm_range, self.set_lnb_corr_ppm, 'LNB frequency correction (ppm)', "counter_slider", float)
        self.top_layout.addWidget(self._lnb_corr_ppm_win)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(decimation, (firdes.complex_band_pass(1, samp_rate, -samp_rate/(2*decimation), samp_rate/(2*decimation), beacontrack_bw)), expected_beacon_freq, samp_rate)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(loop_bw, 2, False)
        self.blocks_vco_c_0 = blocks.vco_c(480000, -1*(480000/decimation), 1)
        self.blocks_multiply_xx_1_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((AF_gain, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((track_beacon, ))
        self.blocks_conjugate_cc_0_0 = blocks.conjugate_cc()
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, rx_audio_rate, 300, 2700, 200, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(44100, '', True)
        self.analog_sig_source_x_2_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, var_freq_fine, 1, 0)
        self.analog_sig_source_x_2_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, var_freq, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate/decimation, analog.GR_COS_WAVE, 500+variable_function_probe_1*200000000, level_tone*1, 0)
        self.analog_agc2_xx_0_0 = analog.agc2_cc(1e-2, 0.2, 1.0, 10)
        self.analog_agc2_xx_0_0.set_max_gain(65536)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-2, 0.2, 1.0, 10)
        self.analog_agc2_xx_0.set_max_gain(65536)
        self._RX_gain_range = Range(0, 80, 1, 50, 200)
        self._RX_gain_win = RangeWidget(self._RX_gain_range, self.set_RX_gain, 'RX RF gain (dB)', "counter_slider", float)
        self.top_layout.addWidget(self._RX_gain_win)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.qtgui_freq_sink_x_0, 'freq'), (self.analog_sig_source_x_2_0, 'freq'))
        self.msg_connect((self.qtgui_waterfall_sink_x_0, 'freq'), (self.analog_sig_source_x_2_0, 'freq'))
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.analog_agc2_xx_0_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_2_0, 0), (self.blocks_conjugate_cc_0, 0))
        self.connect((self.analog_sig_source_x_2_0_0, 0), (self.blocks_conjugate_cc_0_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_conjugate_cc_0, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.blocks_conjugate_cc_0_0, 0), (self.blocks_multiply_xx_1_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_probe_signal_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.blocks_multiply_xx_1_0_0, 1))
        self.connect((self.blocks_multiply_xx_1_0_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 1), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.rational_resampler_xxx_4, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_agc2_xx_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.low_pass_filter_1, 0), (self.analog_probe_avg_mag_sqrd_x_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.rational_resampler_xxx_4, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_lnb_corr_ppm(self):
        return self.lnb_corr_ppm

    def set_lnb_corr_ppm(self, lnb_corr_ppm):
        self.lnb_corr_ppm = lnb_corr_ppm
        self.set_ref_freq(25*1e6*(1+self.lnb_corr_ppm*1e-6))

    def get_ref_freq(self):
        return self.ref_freq

    def set_ref_freq(self, ref_freq):
        self.ref_freq = ref_freq
        self.set_ref_freq_textbox(self.ref_freq/1e6)
        self.set_LNB_LO_freq(self.ref_freq*self.mult)

    def get_mult(self):
        return self.mult

    def set_mult(self, mult):
        self.mult = mult
        self.set_LNB_LO_freq(self.ref_freq*self.mult)

    def get_tpx_center_freq(self):
        return self.tpx_center_freq

    def set_tpx_center_freq(self, tpx_center_freq):
        self.tpx_center_freq = tpx_center_freq
        self.set_RX_frequency(self.tpx_center_freq-self.LNB_LO_freq)

    def get_LNB_LO_freq(self):
        return self.LNB_LO_freq

    def set_LNB_LO_freq(self, LNB_LO_freq):
        self.LNB_LO_freq = LNB_LO_freq
        self.set_RX_frequency(self.tpx_center_freq-self.LNB_LO_freq)

    def get_variable_function_probe_0(self):
        return self.variable_function_probe_0

    def set_variable_function_probe_0(self, variable_function_probe_0):
        self.variable_function_probe_0 = variable_function_probe_0
        self.set_tracked_bcn_freq_textbox(self.variable_function_probe_0*-1*(48000/self.decimation))

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation
        self.set_tracked_bcn_freq_textbox(self.variable_function_probe_0*-1*(48000/self.decimation))
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate/self.decimation, 1000, 4000, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.complex_band_pass(1, self.samp_rate, -self.samp_rate/(2*self.decimation), self.samp_rate/(2*self.decimation), self.beacontrack_bw)))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/self.decimation)

    def get_RX_frequency(self):
        return self.RX_frequency

    def set_RX_frequency(self, RX_frequency):
        self.RX_frequency = RX_frequency
        self.set_rx_freq_textbox_0(self.RX_frequency/1e6)
        self.rtlsdr_source_0.set_center_freq(self.RX_frequency, 0)

    def get_variable_function_probe_1(self):
        return self.variable_function_probe_1

    def set_variable_function_probe_1(self, variable_function_probe_1):
        self.variable_function_probe_1 = variable_function_probe_1
        self.analog_sig_source_x_0.set_frequency(500+self.variable_function_probe_1*200000000)

    def get_var_freq_fine(self):
        return self.var_freq_fine

    def set_var_freq_fine(self, var_freq_fine):
        self.var_freq_fine = var_freq_fine
        self.analog_sig_source_x_2_0_0.set_frequency(self.var_freq_fine)

    def get_var_freq(self):
        return self.var_freq

    def set_var_freq(self, var_freq):
        self.var_freq = var_freq
        self.analog_sig_source_x_2_0.set_frequency(self.var_freq)

    def get_upper_int(self):
        return self.upper_int

    def set_upper_int(self, upper_int):
        self.upper_int = upper_int
        self.qtgui_waterfall_sink_x_0.set_intensity_range(self.lower_int, self.upper_int)

    def get_tracked_bcn_freq_textbox(self):
        return self.tracked_bcn_freq_textbox

    def set_tracked_bcn_freq_textbox(self, tracked_bcn_freq_textbox):
        self.tracked_bcn_freq_textbox = tracked_bcn_freq_textbox
        Qt.QMetaObject.invokeMethod(self._tracked_bcn_freq_textbox_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.tracked_bcn_freq_textbox)))

    def get_track_beacon(self):
        return self.track_beacon

    def set_track_beacon(self, track_beacon):
        self.track_beacon = track_beacon
        self._track_beacon_callback(self.track_beacon)
        self.blocks_multiply_const_vxx_0.set_k((self.track_beacon, ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate/self.decimation, 1000, 4000, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.complex_band_pass(1, self.samp_rate, -self.samp_rate/(2*self.decimation), self.samp_rate/(2*self.decimation), self.beacontrack_bw)))
        self.analog_sig_source_x_2_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_2_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/self.decimation)

    def get_rx_freq_textbox_0(self):
        return self.rx_freq_textbox_0

    def set_rx_freq_textbox_0(self, rx_freq_textbox_0):
        self.rx_freq_textbox_0 = rx_freq_textbox_0
        Qt.QMetaObject.invokeMethod(self._rx_freq_textbox_0_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq_textbox_0)))

    def get_rx_audio_rate(self):
        return self.rx_audio_rate

    def set_rx_audio_rate(self, rx_audio_rate):
        self.rx_audio_rate = rx_audio_rate
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(1, self.rx_audio_rate, 300, 2700, 200, firdes.WIN_HAMMING, 6.76))

    def get_ref_freq_textbox(self):
        return self.ref_freq_textbox

    def set_ref_freq_textbox(self, ref_freq_textbox):
        self.ref_freq_textbox = ref_freq_textbox
        Qt.QMetaObject.invokeMethod(self._ref_freq_textbox_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.ref_freq_textbox)))

    def get_lower_int(self):
        return self.lower_int

    def set_lower_int(self, lower_int):
        self.lower_int = lower_int
        self.qtgui_waterfall_sink_x_0.set_intensity_range(self.lower_int, self.upper_int)

    def get_loop_bw(self):
        return self.loop_bw

    def set_loop_bw(self, loop_bw):
        self.loop_bw = loop_bw
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.loop_bw)

    def get_level_tone(self):
        return self.level_tone

    def set_level_tone(self, level_tone):
        self.level_tone = level_tone
        self._level_tone_callback(self.level_tone)
        self.analog_sig_source_x_0.set_amplitude(self.level_tone*1)

    def get_expected_beacon_freq(self):
        return self.expected_beacon_freq

    def set_expected_beacon_freq(self, expected_beacon_freq):
        self.expected_beacon_freq = expected_beacon_freq
        Qt.QMetaObject.invokeMethod(self._expected_beacon_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.expected_beacon_freq)))
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.expected_beacon_freq)

    def get_beacontrack_bw(self):
        return self.beacontrack_bw

    def set_beacontrack_bw(self, beacontrack_bw):
        self.beacontrack_bw = beacontrack_bw
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.complex_band_pass(1, self.samp_rate, -self.samp_rate/(2*self.decimation), self.samp_rate/(2*self.decimation), self.beacontrack_bw)))

    def get_RX_gain(self):
        return self.RX_gain

    def set_RX_gain(self, RX_gain):
        self.RX_gain = RX_gain

    def get_AF_gain(self):
        return self.AF_gain

    def set_AF_gain(self, AF_gain):
        self.AF_gain = AF_gain
        self.blocks_multiply_const_vxx_1.set_k((self.AF_gain, ))


def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
