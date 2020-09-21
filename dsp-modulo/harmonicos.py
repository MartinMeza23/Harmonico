import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import SquareSignal
from thinkdsp import decorate
import thinkplot
import numpy

señalRectangular = SquareSignal(freq=2, amp=1.0, offset=numpy.pi)
waveRectangular = señalRectangular.make_wave(duration=1, start=0, framerate=44100)

señalSenoidal = SinSignal(freq=2, amp=1.0, offset=0)
harmonico1 = SinSignal(freq=señalSenoidal.freq*3, amp= 0.3, offset=0)
harmonico2 = SinSignal(freq=señalSenoidal.freq*5, amp=0.25, offset=0)
harmonico3 = SinSignal(freq=señalSenoidal.freq*7, amp=0.2, offset=0)
harmonico4 = SinSignal(freq=señalSenoidal.freq*9, amp=0.15, offset=0)
harmonico5 = SinSignal(freq=señalSenoidal.freq*11, amp=0.1, offset=0)
harmonico6 = SinSignal(freq=señalSenoidal.freq*13, amp=0.05, offset=0)
mezcla = señalSenoidal + harmonico1 + harmonico2 + harmonico3 + harmonico4+ harmonico5 + harmonico6
waveMezcla = mezcla.make_wave(duration=1, start=0, framerate=44100)


waveRectangular.plot()
waveMezcla.plot()
thinkplot.show()

espectroRectangular = waveRectangular.make_spectrum()
espectroMezcla = waveMezcla.make_spectrum()

espectroRectangular.plot()
espectroMezcla.plot()
thinkplot.show()


