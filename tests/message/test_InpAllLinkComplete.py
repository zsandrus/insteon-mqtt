#===========================================================================
#
# Tests for: insteont_mqtt/message/InpAllLinkComplete.py
#
#===========================================================================
import insteon_mqtt.message as Msg
import pytest

#===========================================================================
class Test_InpAllLinkComplete:
    #-----------------------------------------------------------------------
    def test_basic(self):
        b = bytes([0x02, 0x53, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
                   0x08])
        obj = Msg.InpAllLinkComplete.from_bytes(b)

        # TODO: check obj

        str(obj)

    #-----------------------------------------------------------------------


#===========================================================================