import matplotlib.pyplot as plt
import obspy
from obspy.core.util import NamedTemporaryFile
from obspy.clients.fdsn import Client as FDSN_Client
from obspy.clients.iris import Client as OldIris_Client


respf = 'RESP/RESP.TJ.SHAA..HHZ'

st = obspy.read ('DATA/2018-11-17-05:21:18.0-37.58-57.11-10-3.80/DISPL.TJ.SHAA..HHZ')


# define a filter band to prevent amplifying noise during the deconvolution
pre_filt = (0.005, 0.007, 0.8, 0.9)


seedresp = {'filename': respf,  # RESP filename
            # Units to return response in ('DIS', 'VEL' or ACC)
            'units': 'DIS'
            }

# Remove instrument response using the information from the given RESP file
tr = st.simulate(paz_remove=None, pre_filt=pre_filt, seedresp=seedresp)
tr.write ("DATA/2018-11-17-05:21:18.0-37.58-57.11-10-3.80/DISP/DISPL.TJ.SHAA..HHZ.mseed", format='MSEED')

