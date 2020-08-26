import os
import sys

################################################################################
# This class Constants will contain any constants and magic numbers that we may
# wish to use in this code.  This will enforce the DRY principle of Python
################################################################################
class Constants:
    @property
    ####################
    # In our datascope data, we use the following Unix epoch date (a
    # day in 2286 as the end_date for stations, networks, and channel
    # epochs.  obspy and stationXML use Null as the end_date, so we
    # will replace our end_date below with Null in the stationXML
    # output
    ####################
    def BIG_END_DATE(self):
        return 9999999999.0
